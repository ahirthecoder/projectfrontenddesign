from django.contrib import admin
from django import forms
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserAccount
        fields = ('email', 'password', 'daily_limit', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]


# Register your models here.
class UserAdminConfig(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email','api_key','daily_limit',)
    search_fields = ('email',)
    readonly_fields = ('date_joined','last_login','api_key')
    ordering = ()
    list_filter = ()
    filter_horizontal = ()
    
    fieldsets = (
        (None, {'fields': ('email', 'api_key', 'daily_limit', 'password','date_joined','last_login', 'is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(UserAccount, UserAdminConfig)
admin.site.unregister(Group)