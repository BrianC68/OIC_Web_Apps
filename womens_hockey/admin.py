from django.contrib import admin
from womens_hockey.models import WomensHockeySkateDate, WomensHockeySkateSession

# Register your models here.


class WomensHockeySkateDateAdmin(admin.ModelAdmin):
    list_display = ['skate_date', 'start_time', 'end_time']


class WomensHockeySkateSessionAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'skater', 'skate_date_display', 'goalie', 'paid']
    list_filter = ['skate_date']
    search_fields = ['user__first_name', 'user__last_name', 'skater__first_name', 'skater__last_name']

    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def skate_date_display(self, obj):
        return f"{obj.skate_date.skate_date} {obj.skate_date.start_time} to {obj.skate_date.end_time}"


admin.site.register(WomensHockeySkateDate, WomensHockeySkateDateAdmin)
admin.site.register(WomensHockeySkateSession, WomensHockeySkateSessionAdmin)
