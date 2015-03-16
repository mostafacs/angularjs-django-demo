from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.views import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import PresentUser
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):


    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'mobile_number', 'gender')}),
        ('Permissions', {'fields': ('is_superuser', 'groups', 'user_permissions')}),

        )



    list_display = ('first_name', 'last_name', 'email', 'mobile_number', 'gender', 'created_date')
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)
    list_filter = ('is_superuser',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'password1', 'password2')}
        ),
        )




admin.site.register(PresentUser,CustomUserAdmin)
admin.site.unregister(Group)