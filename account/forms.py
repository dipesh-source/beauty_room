from django import forms
from account.models import CustomUser
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    AuthenticationForm,
    SetPasswordForm,
)


class CustomUserCreationForm(UserCreationForm):
    logo = forms.ImageField(
        label="Select Profile Pic",
        label_suffix="",
        widget=forms.FileInput(),
        # error_messages={"required": "Please, select image"},
    )
    email = forms.EmailField(
        label="",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter Email Id"}
        ),
        error_messages={"required": "enter your Email"},
    )
    username = forms.CharField(
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Create username"}
        ),
        error_messages={"required": "username is required"},
    )
    phone = forms.CharField(
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter phone number"}
        ),
        error_messages={"required": "username is required"},
    )
    address = forms.CharField(
        max_length=100,
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter salon address"}
        ),
        error_messages={"required": "address is required"},
    )
    first_name = forms.CharField(
        required=False,
        max_length=20,
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter First Name"}
        ),
    )
    last_name = forms.CharField(
        required=False,
        max_length=100,
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Last Name"}
        ),
    )
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()

    class Meta:
        model = CustomUser
        fields = (
            "logo",
            "email",
            "username",
            "phone",
            "address",
            "start_date",
            "end_date",
            "first_name",
            "last_name",
        )


class CustomUserChangeForm(UserChangeForm):
    logo = forms.ImageField(
        label="Select Profile Pic",
        label_suffix="",
        widget=forms.FileInput(),
        # error_messages={"required": "Please, select image"},
    )
    email = forms.EmailField(
        label="",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter Email Id"}
        ),
        error_messages={"required": "enter your Email"},
    )
    username = forms.CharField(
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Create username"}
        ),
        error_messages={"required": "username is required"},
    )
    phone = forms.CharField(
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter phone number"}
        ),
        error_messages={"required": "username is required"},
    )
    address = forms.CharField(
        max_length=100,
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter salon address"}
        ),
        error_messages={"required": "address is required"},
    )
    first_name = forms.CharField(
        required=False,
        max_length=20,
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter First Name"}
        ),
    )
    last_name = forms.CharField(
        required=False,
        max_length=100,
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Last Name"}
        ),
    )
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()

    class Meta:
        model = CustomUser
        fields = (
            "logo",
            "email",
            "username",
            "phone",
            "address",
            "start_date",
            "end_date",
            "first_name",
            "last_name",
        )


class LoginForm(AuthenticationForm):
    """
    will login to admin panel for admin Or normal user
    """

    username = forms.CharField(
        label="Enter Username",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your E-mail"}
        ),
        error_messages={"required": "Please, enter username"},
    )
    password = forms.CharField(
        label="Enter Password",
        label_suffix="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "*******"}
        ),
        error_messages={"required": "enter your password"},
    )

    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class ChangepasswordForm(PasswordChangeForm):
    """
    will change password from the own session (without Email)
    """

    old_password = forms.CharField(
        label="enter old password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        error_messages={"required": "old password required"},
    )
    new_password1 = forms.CharField(
        label="set new password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        error_messages={"required": "enter new password"},
    )
    new_password2 = forms.CharField(
        label="confirm password",
        label_suffix="",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        error_messages={"required": "confirm new password"},
    )

    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password1", "new_password2"]
