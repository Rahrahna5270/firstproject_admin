
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dash'),
    path('create',views.create,name='create'),
    path('view/<int:id>/',views.viewadmin,name='viewadmin'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    # path('logout',views.logout,name='logout')
    path('logout/', views.user_logout, name='logout'),
]    