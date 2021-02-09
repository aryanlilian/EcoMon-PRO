import django_filters
from django import forms
from .models import Post


class PostFilterForm(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Search Keyword'}),
        label=''
    )

    class Meta:
        model = Post
        fields = ['title']
