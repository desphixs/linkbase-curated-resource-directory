# directory/urls.py
from django.urls import path
# We import our views from the current directory. The dot (.) represents the current folder we are in.
from . import views

# We define app_name to support namespace and reverse URL lookups in our templates.
# Think of this like giving our application its own unique category code so its views don't collide with other apps.
app_name = 'directory'

# ==========================================
# ANALOGY: Think of urlpatterns as a directory map in a building lobby.
# When a visitor enters, they look at the directory guide to see which room matches 
# the path they want. If they want the root homepage (''), the guide points them to the 'global_feed' view chef!
# ==========================================
urlpatterns = [
    # We map the root URL path (empty string) to our global_feed view function.
    # When a user goes to the homepage (http://127.0.0.1:8000/), Django will run global_feed().
    # We give it a name 'global_feed' so we can reference it easily elsewhere in our templates.
    path('', views.global_feed, name='global_feed'),
]
