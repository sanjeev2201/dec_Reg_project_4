from django.urls import path
from . import views
urlpatterns = [
    path('reg/', views.registration,name='registration'),
    path('list/',views.list_contact,name='list_contact'),
    path('edit/<int:pk>',views.customer_edit,name='edit-customer'),
    path('delete/<int:pk>',views.customer_delete,name='delete-customer'),
    path('create_user/',views.create_user,name='create-user'),
    path('login/',views.login_request,name='login'),
    path("logout/", views.logout_request, name= "logout")
]
