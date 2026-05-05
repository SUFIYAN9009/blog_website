from django.contrib import admin
from .models import TravelPost,Guide,Booking

# Register your models here.

@admin.register(TravelPost)
class TravelPostAdmin(admin.ModelAdmin):
    list_display = ['picture','title','description','created_at']

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty', 'experience', 'location']
    list_filter = ['specialty', 'location']
    search_fields = ['name']


# =========================
# BOOKING ACTIONS
# =========================

@admin.action(description="Approve selected bookings")
def approve_bookings(modeladmin, request, queryset):
    queryset.update(status='approved')


@admin.action(description="Reject selected bookings")
def reject_bookings(modeladmin, request, queryset):
    queryset.update(status='rejected')


# =========================
# BOOKING ADMIN PANEL
# =========================
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ['user', 'guide', 'date', 'status', 'created_at']

    list_filter = ['status', 'date', 'guide']

    search_fields = ['user__username', 'guide__name']

    list_editable = ['status']

    ordering = ['-created_at']

    actions = [approve_bookings, reject_bookings]    