from .models import Service, Staff
from django import forms
from .models import (
    Service,
    Staff,
    Appointment,
    Feedback,
    Product,
    Purchase,
    Gallery,
    Attendance,
)


class AppointmentForm(forms.ModelForm):
    service = forms.ModelMultipleChoiceField(
        label="select service",
        label_suffix="",
        required=False,
        widget=forms.SelectMultiple(),
        queryset=Service.objects.all(),
    )
    staff = forms.ModelChoiceField(
        label="select staff member",
        label_suffix="",
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=Staff.objects.all(),
    )

    class Meta:
        model = Appointment
        fields = (
            "name",
            "surname",
            "phone",
            "app_date",
            "app_time",
            "service",
            "staff",
        )
        labels = {
            "name": "Customer name",
            "surname": "Enter surname",
            "phone": "Enter phone number",
            "app_date": "Select Appointment Date",
            "app_time": "Select Appointment Time",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "enter customer name"}
            ),
            "surname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "enter customer name"},
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "enter phone number"},
            ),
            "app_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date", "id": "date_picker"},
            ),
            "app_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"},
            ),
        }
        error_messages = {
            "name": {"required": "customer name is required"},
            "surname": {"required": "surname is required"},
            "phone": {"required": "phone number is required"},
            "app_date": {"required": "select app**nt date"},
            "app_time": {"required": "select app**nt time"},
        }


class ServiceForm(forms.ModelForm):
    # img = forms.ImageField(label_suffix="", label="", required=False)

    class Meta:
        model = Service
        fields = "__all__"
        labels = {
            "name": "Enter service name",
            "cost": "Enter product cost",
            "text": "something about product",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cost": forms.NumberInput(attrs={"class": "form-control"}),
            "text": forms.TextInput(attrs={"class": "form-control"}),
        }
        errror_messages = {
            "name": {"required": "required service name"},
            "cost": {"required": "required cost"},
        }


class StaffForm(forms.ModelForm):
    # profile = forms.ImageField(
    #     label="Select member pic",
    #     label_suffix="",
    #     required=False,
    # )

    class Meta:
        model = Staff
        # fields = ["profile", "name", "surname", "phone", "email", "specialization"]
        fields = "__all__"
        labels = {
            "name": "Enter member name",
            "surname": "Enter surname",
            "phone": "Enter phone number",
            "email": "Enter member email-id",
            "specialization": "what's the specialization",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "surname": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "enter phone number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "enter Email id"}
            ),
            "specialization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "what's the specialization",
                }
            ),
        }
        errror_messages = {
            "name": {"required": "required member name"},
            "surname": {"required": "required surname"},
            "phone": {"required": "required phone number"},
            "specialization": {"required": "required specialization"},
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "phone", "feedback"]
        labels = {
            "name": "Enter Your Name",
            "phone": "Phone Number",
            "feedback": "Your Feedback",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "feedback": forms.Textarea(attrs={"class": "form-control"}),
        }
        error_messages = {
            "name": {"required": "enter your name"},
            "phone": {"required": "must be phone number"},
            "feedback": {"required": "write your Feedback"},
        }


class GalleryForm(forms.ModelForm):
    img = forms.FileField(
        label="Select Image", label_suffix="", widget=forms.ImageField(), required=False
    )
    file = forms.FileField(
        label="Select File", label_suffix="", widget=forms.FileInput(), required=False
    )

    class Meta:
        model = Gallery
        fields = ["name", "img", "file", "about"]
        labels = {"name": "Enter post name", "about": "Something about post"}
        widgets = {"about": forms.TextInput(attrs={"class": "form-control"})}
        error_messages = {
            "name": {"required": "enter image name"},
        }


class ProductForm(forms.ModelForm):
    img = forms.ImageField(
        label="select pic", label_suffix="", required=False, widget=forms.FileInput()
    )

    class Meta:
        model = Product
        fields = ["img", "name", "price", "stock", "note"]
        labels = {
            "name": "Enter name",
            "price": "Enter price",
            "stock": "Enter total product",
            "note": "Note about product",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "note": forms.TextInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "name": {"required": "enter product"},
            "price": {"required": "enter price"},
            "stock": {"required": "enter total product"},
        }


class PurchaseForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        label="select staff member",
        label_suffix="",
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=Product.objects.all(),
    )

    class Meta:
        model = Purchase
        fields = ["product", "name", "phone", "qty"]
        labels = {"phone": "Enter customer phonenumber", "qty": "Enter quantity"}
        widgets = {
            "name": forms.Textarea(attrs={"class": "form-control"}),
            "qty": forms.NumberInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "name": {"required": "enter customer name"},
            "qty": {"required": "enter product quantity"},
        }


class AttedanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["in_date", "in_time", "out_date", "out_time", "check_out"]
        labels = {
            "in_date": "Today's date ",
            "in_time": "Current time",
            "out_date": "Off date",
            "out_time": "Off time",
        }
        widgets = {
            "in_date": forms.DateInput(attrs={"class": "form-control"}),
            "in_time": forms.TimeInput(attrs={"class": "form-control"}),
            "out_date": forms.DateInput(attrs={"class": "form-control"}),
            "out_time": forms.TimeInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "in_date": {"required": "required in_date"},
            "in_time": {"required": "required in_time"},
            "out_date": {"required": "required out_date"},
            "out_time": {"required": "required out_time"},
        }
