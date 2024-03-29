from django import forms
from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class AboutAdminForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)