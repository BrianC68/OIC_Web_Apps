from django.contrib import admin
from nacho_skate.models import NachoSkateDate, NachoSkateSession, NachoSkateRegular

# Register your models here.


class NachoSkateDateAdmin(admin.ModelAdmin):
    list_display = ['skate_date', 'start_time', 'end_time']


class NachoSkateSessionAdmin(admin.ModelAdmin):
    list_display = ['skater_name', 'skate_date_display', 'goalie', 'paid']
    list_filter = ['skate_date']
    search_fields = ['skater__last_name', 'skater__first_name']

    def skater_name(self, obj):
        return f"{obj.skater.first_name} {obj.skater.last_name}"

    def skate_date_display(self, obj):
        return f"{obj.skate_date.skate_date} {obj.skate_date.start_time} to {obj.skate_date.end_time}"


class NachoSkateRegularAdmin(admin.ModelAdmin):
    list_display = ['skater_name']

    def skater_name(self, obj):
        return f"{obj.regular.first_name} {obj.regular.last_name}"


admin.site.register(NachoSkateDate, NachoSkateDateAdmin)
admin.site.register(NachoSkateSession, NachoSkateSessionAdmin)
admin.site.register(NachoSkateRegular, NachoSkateRegularAdmin)
