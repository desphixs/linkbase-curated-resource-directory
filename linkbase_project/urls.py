"""
URL configuration for linkbase_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# We import path and include from django.urls. 
# include allows us to reference another URL file so our project remains modular and scalable.
from django.urls import path, include

# ==========================================
# ANALOGY: Think of the main project urls.py as the primary train station switchboard.
# Trains (web requests) come in and read the master switchboard. If a request is headed 
# to 'admin/', it switches onto the admin track. If it's a general passenger, we switch it 
# onto the 'directory' app track using the include() switch!
# ==========================================
urlpatterns = [
    # Admin control room routing
    path('admin/', admin.site.urls),
    
    # Root path: we include the URLs defined inside our directory app.
    # When a visitor goes to the homepage (empty string ''), Django hands the request 
    # to the directory's urls.py mapping system.
    path('', include('directory.urls')),
]
