from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    from django.contrib.auth.admin import UserAdmin 
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

     
    #    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'address','start_date','end_date')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_editable = ['username','phone']
    list_display = ('email', 'username', 'phone', 'start_date', 'end_date','is_staff','is_superuser')
    search_fields = ('email', 'first_name', 'last_name','phone','username')
    ordering = ('email','username')


 
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # # list_filter = ('is_admin','email','username')
    # (None, {'fields': ('username','email', 'password')}),
    # (('Personal info'), {'fields': ('first_name', 'last_name','start_at','end_at')}),

    # # (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    # #                                    'groups', 'user_permissions')}),

    # (('Important dates'), {'fields': ('last_login', 'date_joined','phone')}),

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'password1', 'password2'),
    #     }),
    # )
    # # list_display = ('email', 'username', 'is_admin')
    # search_fields = ('email','username')
    # filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
