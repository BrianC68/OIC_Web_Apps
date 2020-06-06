from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import FigureSkatingDate, FigureSkater, FigureSkatingSession
from .forms import CreateFigureSkaterForm, CreateFigureSkatingSessionForm
from programs.models import Program
from cart.models import Cart
from accounts.models import Profile
from datetime import date

class FigureSkatingView(LoginRequiredMixin, TemplateView):
    '''Page that displays index view for Figure Skating web app.'''

    template_name = 'figure_skating.html'
    fs_dates_model = FigureSkatingDate
    skater_model = FigureSkater
    session_model = FigureSkatingSession
    program_model = Program

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fs_dates = self.fs_dates_model.objects.filter(skate_date__gte=date.today()).annotate(num_skaters=Count('figureskatingsession'))
        context['fs_dates'] = fs_dates
        sessions = self.session_model.objects.filter(guardian=self.request.user, session__skate_date__gte=date.today()).order_by('session__skate_date')
        context['my_sessions'] = sessions
        skaters = self.skater_model.objects.filter(guardian=self.request.user)
        context['my_skaters'] = skaters
        max_skaters = self.program_model.objects.get(pk=3).max_skaters
        context['max_skaters'] = max_skaters
        return context

class CreateFigureSkaterView(LoginRequiredMixin, CreateView):
    '''Page where user adds Figure Skaters to the FigureSkater model.'''

    model = FigureSkater
    form_class = CreateFigureSkaterForm
    template_name = 'create_figure_skater_form.html'
    success_url = reverse_lazy('figure_skating:figure-skating')

    def form_valid(self, form):
        form.instance.guardian = self.request.user
        try:
            success = super().form_valid(form)
            messages.add_message(self.request, messages.SUCCESS, 'Skater has been added to My Skaters!')
            return success
        except IntegrityError:
            messages.add_message(self.request, messages.ERROR, 'This skater is already in My Skaters.')
            return render(self.request, template_name=self.template_name, context=self.get_context_data())


class DeleteFigureSkaterView(LoginRequiredMixin, DeleteView):
    '''Allows user to remove their skaters from FigureSkater model.'''
    model = FigureSkater
    success_url = reverse_lazy('figure_skating:figure-skating')

    def delete(self, *args, **kwargs):
        # Set success message and return
        messages.add_message(self.request, messages.SUCCESS, 'Skater has been removed from My Skaters!')
        return super().delete(*args, **kwargs)


class CreateFigureSkatingSessionView(LoginRequiredMixin, CreateView):
    '''Page that allows users to sign up for figure skating sessions.'''

    model = FigureSkatingSession
    skater_model = FigureSkater
    program_model = Program
    cart_model = Cart
    group_model = Group
    profile_model = Profile
    template_name = 'create_figure_skating_session_form.html'
    success_url = reverse_lazy('figure_skating:figure-skating')
    form_class = CreateFigureSkatingSessionForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        if self.request.method == 'GET':
            initial['session'] = self.kwargs['session']
            return initial
        else:
            return {}

    def form_valid(self, form):
        form.instance.guardian = self.request.user
        self.object = form.save(commit=False)
        try:
            # If skater spots are full, do not save object
            if self.model.objects.filter(session=form.instance.session.id).count() >= self.program_model.objects.get(pk=3).max_skaters:
                messages.add_message(self.request, messages.ERROR, 'Sorry, this session is now full!')
                return redirect('figure_skating:figure-skating')
        except:
            pass
        # Do the following and then save the Figure Skating Session
        self.add_to_cart(form.instance.skater)
        self.join_figure_skating_group()
        self.add_figure_skating_email_to_profile()
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Skater has been added to the session(s).\nYou must view your cart and pay for your session(s) to complete registration!')
        return super().form_valid(form)

    def add_to_cart(self, skater):
        '''Adds Open Figure Skating session to shopping cart.'''
        # Get price of Figure Skating program
        price = self.program_model.objects.get(id=3).skater_price
        cart = self.cart_model(customer=self.request.user, item='Figure Skating', skater_name=skater, event_date=self.object.session.skate_date, event_start_time=self.object.session.start_time, amount=price)
        cart.save()

    def join_figure_skating_group(self, join_group='Figure Skating'):
        '''Adds user to Figure Skating group "behind the scenes", for communication purposes.'''
        try:
            group = self.group_model.objects.get(name=join_group)
            self.request.user.groups.add(group)
        except IntegrityError:
            pass
        return

    def add_figure_skating_email_to_profile(self):
        '''If no user profile exists, create one and set figure_skating_email to True.'''
        # If a profile already exists, do nothing
        try:
            self.profile_model.objects.get(user=self.request.user)
            return
        # If no profile exists, add one and set open_hockey_email to True
        except ObjectDoesNotExist:
            profile = self.profile_model(user=self.request.user, slug=self.request.user.id, figure_skating_email=True)
            profile.save()
            return


class DeleteFigureSkatingSessionView(LoginRequiredMixin, DeleteView):
    '''Allows user to remove skater from a skate session.'''
    model = FigureSkatingSession
    skate_date_model = FigureSkatingDate
    skater_model = FigureSkater
    success_url = reverse_lazy('figure_skating:figure-skating')

    def delete(self, *args, **kwargs):
        '''Things that need doing once a session is removed.'''

        # Clear session from the cart
        skate_date = self.model.objects.filter(id=kwargs['pk']).values_list('session__skate_date', flat=True)
        skate_time = self.model.objects.filter(id=kwargs['pk']).values_list('session__start_time', flat=True)
        skater_id = self.model.objects.filter(id=kwargs['pk']).values_list('skater', flat=True)
        skater = self.skater_model.objects.get(id=skater_id[0])
        cart_item = Cart.objects.filter(event_date=skate_date[0], event_start_time=skate_time[0], skater_name=skater).delete()

        # Set success message and return
        messages.add_message(self.request, messages.SUCCESS, 'Skater has been removed from the figure skating session!')
        return super().delete(*args, **kwargs)