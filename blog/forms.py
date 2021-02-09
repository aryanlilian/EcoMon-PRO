from django import forms
from .models import Post, Comment
from common.constants import help_texts, error_messages
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(),
        max_length=200,
        help_text=help_texts['post_title'],
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 25, 'cols': 50}),
        help_text=help_texts['any_character'],
    )
    full_image = forms.ImageField(
        widget=forms.FileInput(),
        help_text=help_texts['full_image'],
    )
    medium_image = forms.ImageField(
        widget=forms.FileInput(),
        help_text=help_texts['medium_image'],
    )
    small_image = forms.ImageField(
        widget=forms.FileInput(),
        help_text=help_texts['small_image'],
    )

    def clean_full_image(self):
        full_image = self.cleaned_data.get('full_image')
        if not full_image:
            raise ValidationError(
                error_messages['no_image'],
                code='full_image_empty'
            )
        else:
            width, height = get_image_dimensions(full_image)
            if width != 1920:
                raise ValidationError(
                    error_messages['full_image_width'] % width,
                    code='full_image_invalid_width'
                )
            if height != 1080:
                raise ValidationError(
                    error_messages['full_image_height'] % height,
                    code='full_image_invalid_height'
                )
        return full_image

    def clean_medium_image(self):
        medium_image = self.cleaned_data.get('medium_image')
        if not medium_image:
            raise ValidationError(
                error_messages['no_image'],
                code='medium_image_empty'
            )
        else:
            width, height = get_image_dimensions(medium_image)
            if width != 750:
                raise ValidationError(
                    error_messages['medium_image_width'] % width,
                    code='medium_image_invalid_width'
                )
            if height != 375:
                raise ValidationError(
                    error_messages['medium_image_height'] % height,
                    code='medium_image_invalid_height'
                )
        return medium_image

    def clean_small_image(self):
        small_image = self.cleaned_data.get('small_image')
        if not small_image:
            raise ValidationError(
                error_messages['no_image'],
                code='small_image_empty'
            )
        else:
            width, height = get_image_dimensions(small_image)
            if width != 60:
                raise ValidationError(
                    error_messages['small_image_width'] % width,
                    code='small_image_invalid_width'
                )
            if height != 60:
                raise ValidationError(
                    error_messages['small_image_height'] % height,
                    code='small_image_invalid_height'
                )
        return small_image


    class Meta:
        model = Post
        exclude = ['author', 'slug', 'published_date', 'updated_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError(
                error_messages['required'],
                code='title_invalid'
            )
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError(
                error_messages['required'],
                code='content_invalid'
            )
        return content


class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class' : 'form-control w-100', 'id' : 'commentContent', 'cols': 50, 'rows': 25}),
        help_text=help_texts['any_character'],
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
