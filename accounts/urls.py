from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<slug>/', views.UpdateProfileView.as_view(), name='profile'),
    path('release_of_liability/', views.ReleaseOfLiablityView.as_view(), name='release-of-liability'),
    path('my_skaters/add/', views.CreateChildSkaterView.as_view(), name='my-skaters-add'),
    path('my_skaters/remove/<pk>/', views.DeleteChildSkaterView.as_view(), name='my-skaters-remove'),
    path('user_credit/purchase/<slug>/', views.UpdateUserCreditView.as_view(), name='purchase-credit'),
]