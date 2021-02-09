from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Newsletter(models.Model):
    email = models.EmailField(_('Email'))
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('index')

class Testimonial(models.Model):

    class PersonType(models.TextChoices):
        CLIENT = 'CLNT', _('Client')
        PRO_CLIENT = 'PCLT', _('Pro Client')
        STUFF = 'STFF', _('Stuff')

    description = models.TextField(_('Description'))
    name = models.CharField(_('Name'), max_length=100)
    person_type = models.CharField(_('Person Type'), max_length=4, choices=PersonType.choices, default=PersonType.CLIENT)
    created_date = models.DateTimeField(_('Created Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.created_date}'
