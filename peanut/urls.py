"""
URL configuration for peanut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views  as auth_views
from mainApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.user_login, name='login'),
    path('accounts/post_job/', views.post_job, name='post_job'),
    path('accounts/post_achievement/', views.post_achievement, name='post_achievement'),
    path('logout/', views.logout_view, name='logout'),
    path('social-auth', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
    path('question-page/', views.question_page, name='question_page'),
    path('start-match/', views.start_match, name='start_match'),
    path('check-room-status/', views.check_room_status, name='check_room_status'),
    path('accounts/profile/', views.profile,name='profile'),
    path('accounts/edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('accounts/community_page/', views.community_page, name='community_page'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('accounts/store/', views.store, name='store'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    
]
