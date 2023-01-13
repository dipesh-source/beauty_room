from django.shortcuts import render, redirect
from account.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.decorators import login_required, user_passes_test
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
from .forms import (
    AppointmentForm,
    StaffForm,
    ServiceForm,
    ProductForm,
    PurchaseForm,
    GalleryForm,
    FeedbackForm,
    AttedanceForm,
)

# Create your views here.
@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def home(request):
    print(request, "#############")
    data = Appointment.appobject.get_all_user_appointment(request.user)
    print("dataaaaaaaaaa", data)
    context = {"data": data}
    return render(request, "myclient/main.html", context)


def register(request):
    return render(request, "myclient/register.html")


def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(data=request.POST, request=request)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                auth = authenticate(request, username=username, password=password)
                if auth is not None:
                    login(request, auth)
                    if request.user.is_superuser:
                        return HttpResponseRedirect("/admin-dash/admin-dashboard/")
                    return HttpResponseRedirect("/dashboard/")
            else:
                messages.warning(
                    request,
                    "Please enter a correct email address and password. Note that both fields may be case-sensitive.",
                )
        else:
            form = LoginForm()
        context = {"form": form}
        return render(request, "myclient/signin.html", context)
    else:
        return redirect("/dashboard/")


def signout(request):
    logout(request)
    return redirect("/")


# todo_list = todo_list_form.save(commit=False)
# todo_list.save()
# todo_list_form.save_m2m()


@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            phone = form.cleaned_data["phone"]
            app_date = form.cleaned_data["app_date"]
            app_time = form.cleaned_data["app_time"]
            service = form.cleaned_data["service"]
            staff = form.cleaned_data["staff"]

            apps = Appointment(
                user=request.user,
                name=name,
                surname=surname,
                phone=phone,
                app_date=app_date,
                app_time=app_time,
            )
            apps.save()
            AppointmentForm.save_m2m()

            messages.success(request, f"""{name} appointment is booked""")
            form = AppointmentForm()
    else:
        form = AppointmentForm()
    context = {"form": form}
    return render(request, "myclient/create_appointment.html", context)


@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def add_staff_member(request):
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.cleaned_data["profile"]
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            specialization = form.cleaned_data["specialization"]
            print(request.user, request.user.username, "##################")
            Staff(
                user=request.user,
                profile=profile,
                name=name,
                surname=surname,
                phone=phone,
                email=email,
                specialization=specialization,
            ).save()
            form = StaffForm()
            messages.success(request, f"{name} profile is created successfully")
    else:
        form = StaffForm()
    data = Staff.staffobj.get_staff_limit(request.user)
    print(data, "##################")
    context = {"form": StaffForm, "data": data}
    return render(request, "myclient/add_staff.html", context)


@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def update_staff(request, upid):
    if request.method == "POST":
        sff = Staff.objects.filter(pk=upid).first()
        fm = StaffForm(request.POST, request.FILES, instance=sff)
        if fm.is_valid():
            fm.save()
            messages.success(request, "staff updated successfully")
    else:
        sff = Staff.objects.filter(pk=upid).first()
        print(sff, "***********************", sff.profile)
        fm = StaffForm(instance=sff)
    profile = Staff.objects.get(pk=upid)
    print("profileeeeeeeeeeeeeeeee", profile)
    context = {"form": fm, "profle": profile}
    return render(request, "myclient/update_staff.html", context)


@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def add_service(request):
    """
    it will save the all the salon service
    """
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data["img"]
            name = form.cleaned_data["name"]
            cost = form.cleaned_data["cost"]
            text = form.cleaned_data["text"]
            Service(user=request.user, img=img, name=name, cost=cost, text=text).save()
            form = ServiceForm()
            messages.success(request, f"Added {name} service")
    else:
        form = ServiceForm()
    data = Service.serviceobj.get_service(request.user)
    print(data, "##############")
    context = {"form": form, "data": data}
    return render(request, "myclient/add_service.html", context)


@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data["img"]
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            stock = form.cleaned_data["stock"]
            note = form.cleaned_data["note"]
            Product(
                user=request.user,
                img=img,
                name=name,
                price=price,
                stock=stock,
                note=note,
            ).save()
            form = ProductForm()
            messages.success(request, f"{name} product created")
    form = ProductForm()
    data = Product.objectproduct.get_product(request.user)
    context = {"form": form, "data": data}
    return render(request, "myclient/add_product.html", context)


@user_passes_test(lambda u: u.is_authenticated, login_url="/")
def update_product(request, pro_id):
    print("update    e3", pro_id)
    if request.method == "POST":
        print("update    e3 pppooooooooosstttttt", pro_id)

        pro = Product.objects.filter(pk=pro_id).first()
        form = ProductForm(request.POST, request.FILES, instance=pro)
        if form.is_valid():
            form.save()
            messages.success(request, "staff updated successfully")
    else:
        pro = Product.objects.filter(pk=pro_id).first()
        form = ProductForm(instance=pro)
        print("update    e3 pppooooooooosstttttt", pro_id)

    product = Product.objects.get(pk=pro_id)
    print("profileeeeeeeeeeeeeeeee", product)
    context = {"form": form, "profle": product}
    return render(request, "myclient/update_product.html", context)
