from django.urls import path
from . import views

urlpatterns = [
    path("signout/", views.signout, name="signout"),
    path("create-appointment/", views.create_appointment, name="create_appointment"),
    path("add-new-staff/", views.add_staff_member, name="add_staff"),
    path("update-staff-detail/<int:upid>/", views.update_staff, name="update_staff"),
    path("add-service/", views.add_service, name="add_service"),
    path("add-product/", views.add_product, name="add_product"),
    path("update-product/<int:pro_id>/", views.update_product, name="update_product"),
]
