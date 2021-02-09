from django.contrib import admin
from .models import Newsletter, Testimonial


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subscribed_date']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'person_type', 'created_date', 'updated_date']
