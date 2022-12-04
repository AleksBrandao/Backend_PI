# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

admin.site.site_header = "🍴 Kitchen Shop Administration 🥣"
admin.site.site_title = "Kitchen Shop Admin"


router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')
router.register(r'guardians', views.GuardianView, 'guardian')
router.register(r'roles', views.RolesView, 'role')
router.register(r'adresses', views.AddressView, 'adress')
router.register(r'students', views.StudentsView, 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('todo/', include('todo.urls'))
]
