from django.shortcuts import render
# We import our Link model from the models file to retrieve bookmark cards from the database.
# The dot (.) means we are importing from the models.py located in the same directory folder.
from .models import Link

# Create your views here.

# ==========================================
# ANALOGY: Think of views as the chefs in a restaurant kitchen. 
# The customer (user) sits at a table (browser) and orders a specific dish (requests a URL). 
# The waiter (URL router) brings that order to the chef (view). 
# The chef goes to the pantry (database), gathers the ingredients (approved links), 
# cooks/arranges them, puts them on a beautiful plate (HTML template), and sends it back to the customer!
# ==========================================
def global_feed(request):
    # This view function handles requests to our homepage and displays approved links.
    # 'request' is a parameter that holds all the incoming browser data (like headers, search queries, etc.).
    
    # We query the database to fetch all Link objects where 'is_approved' is True.
    # Think of this like pulling only the approved/passed inspection bookmark cards from our files.
    # We use .filter(is_approved=True) to make sure we filter out unapproved links from being displayed.
    approved_links = Link.objects.filter(is_approved=True)
    
    # We place the retrieved links into a dictionary called 'context'. 
    # The context is like a shipping box we use to send variables from our Python view 
    # to our HTML template so the template can unpack them and show them to the user.
    context = {
        'links': approved_links
    }
    
    # We render the template 'directory/link_list.html' and pass our context variables.
    # Rendering means taking our static HTML page and dynamically injecting our database content into it.
    return render(request, 'directory/link_list.html', context)
