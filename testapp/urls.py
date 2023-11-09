from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('index/', views.index, name= 'index'),
    path('add/', views.add, name= 'add'),
    path('show/', views.show, name ='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),






]
