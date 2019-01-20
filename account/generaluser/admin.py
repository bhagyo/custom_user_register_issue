from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

'''
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    form = UserAdminChangeForm  # For updating the View
    add_form = UserAdminCreationForm  # For creating the View

    class Meta:
        model = User
'''


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm  # For updating the View
    add_form = UserAdminCreationForm  # For creating the View

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'admin', 'doctor',)
    list_filter = ('admin', 'doctor',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('username',)}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
        ('Permissions', {'fields': ('doctor',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email', 'doctor',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
