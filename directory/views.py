from django.shortcuts import render, get_object_or_404, redirect
# We import our Category and Link models from the models file to retrieve database records.
# Category stores the topic sections; Link stores each individual resource bookmark.
# The dot (.) means we are importing from the models.py located in the same directory folder.
from .models import Category, Link

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


# ==========================================
# ANALOGY: Think of this category_filter view as a specialized librarian.
# Instead of showing the entire warehouse to the visitor, the visitor hands 
# the librarian a specific aisle identifier (category_id) in their URL path. 
# The librarian walks to that category shelving section. If that aisle doesn't exist, 
# they raise a polite 404 Page Not Found error sign ("Aisle not found!").
# If it exists, they gather ONLY the book cards (links) resting on that specific aisle shelf 
# that are marked as approved (is_approved=True), pack them in a context box, 
# and lay them out on our custom HTML display board (category_detail.html).
# ==========================================
def category_filter(request, category_id):
    # This view function handles requests to view approved links in a specific category.
    # 'category_id' represents the numeric ID of the category, passed dynamically from our URL path.
    
    # We fetch the specific Category object matching the given ID from the database.
    # If no category matches, Django automatically returns a clean 404 Page Not Found error page.
    # This acts like an automatic safety guard, preventing our application from crashing on bad IDs.
    category = get_object_or_404(Category, id=category_id)
    
    # We query our Link model to filter and grab only the approved bookmarks belonging to this category.
    # We specify 'category=category' to match our foreign key, and 'is_approved=True' to hide unapproved links.
    filtered_links = Link.objects.filter(category=category, is_approved=True)
    
    # We place the fetched category object and the list of filtered links into the context package.
    # This allows our HTML template to unpack the category's name and loop through its resource bookmarks.
    context = {
        'category': category,
        'links': filtered_links
    }
    
    # We render our new template 'directory/category_detail.html' and pass our context variables.
    # Rendering takes our static category layout and dynamically merges it with this filtered list of resources.
    return render(request, 'directory/category_detail.html', context)


# ==========================================
# ANALOGY: Think of this submit_link view as a community suggestion box.
# 1. When a visitor walks up to read the suggestion box (GET request), the librarian (view) 
#    reaches into the cabinet drawers, gathers all the Category names, and lays out 
#    a clean, beautiful form paper (submit_link.html) with a dropdown select listing the categories.
# 2. When the visitor fills out the form paper and drops it into the suggestion slot (POST request), 
#    the librarian catches it, validates the inputs, finds the selected Category drawer matching the ID, 
#    and writes down a new bookmark card (Link object) with the approval status box checked to 'False' 
#    by default. The librarian puts it in the pending tray for moderators to review and politely sends the visitor 
#    back to the main lobby hall (redirects to the global homepage).
# ==========================================
def submit_link(request):
    # This view function handles displaying our link submission form (GET) and processing the submitted form data (POST).
    
    # We check if the incoming request method is 'POST'. 
    # POST means the user has filled out the HTML form and clicked the submit button, sending their data to our server.
    if request.method == 'POST':
        # We extract each form input text value using the request.POST dictionary.
        # We target the 'name' attribute specified on each of our HTML input fields.
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        
        # We query the Category table to fetch the single Category object matching the chosen dropdown ID.
        # This connects our relational ForeignKey cleanly.
        category = get_object_or_404(Category, id=category_id)
        
        # We create a new Link database object and populate its fields.
        # Note: We do not set 'is_approved' because it defaults to 'False' automatically as defined in models.py.
        # This keeps the submission hidden on the feed until a moderator reviews and approves it in the admin dashboard!
        new_link = Link(
            title=title,
            url=url,
            description=description,
            category=category
        )
        
        # We write this new object record to our database tables.
        new_link.save()
        
        # Once successfully saved, we redirect the user back to the homepage.
        # Think of redirect() like a traffic cop telling the browser to transition immediately to another URL.
        return redirect('directory:global_feed')
        
    # If the request method is NOT 'POST' (which means it's a GET request when a user first visits the page),
    # we need to display a clean, blank form.
    # To populate the category select dropdown list, we fetch all categories from the database.
    categories = Category.objects.all()
    
    # We place the categories list inside the context box so the HTML select dropdown menu can render them.
    context = {
        'categories': categories
    }
    
    # We render our new 'submit_link.html' template with our context categories.
    return render(request, 'directory/submit_link.html', context)

