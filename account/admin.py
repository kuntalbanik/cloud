from django import forms
from django.contrib import admin
from django.contrib.auth import password_validation
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User


#################################
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html(),)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, strip=False, help_text="Enter the same password as before, for verification.",)
     
    class Meta:
        model = User
        fields = ('email',)
 
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
 
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','date_joined','is_admin', 'is_active', 'is_staff',
                          'is_superuser', 'is_accounts', 'is_support', 'is_service', 'is_sales',)
    list_filter = ('is_admin', 'is_active', 'is_staff',
                          'is_superuser', 'is_accounts', 'is_support', 'is_service', 'is_sales',)
    
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (('Personal info'), {'fields': ('username',)}),
#         (('Permissions'), {
#             'fields': ('is_admin','is_active','is_staff',
#                           'is_superuser','is_student','is_teacher','is_sales', 'user_permissions'),
#         }),
# #         (('Important dates'), {'fields': ('last_login', )}),
#     )
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'groups',)}),
        ('Permissions', {'fields':('user_permissions', 'is_admin', 'is_active', 'is_staff',
                          'is_superuser', 'is_accounts', 'is_support', 'is_service', 'is_sales',)}),
        ('Important dates', {'fields': ('date_joined','last_login', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2', 'group',)}
#         ),
#     )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.site_header = 'ORBIT - Admin Panel'