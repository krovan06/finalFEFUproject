from django.urls import path, include
from .views import user_profile, register, CustomLoginView, redirect_to_profile,user_edit_profile

urlpatterns = [
    path('user/id/<int:id>/', user_profile, name='user_profile'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user/id/<int:id>/edit/', user_edit_profile, name='user_edit_profile'),
    path('', redirect_to_profile, name='redirect_to_profile'),
]
