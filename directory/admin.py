from django.contrib import admin
# We import our Category and Link models from the current directory's models.py file.
# The dot (.) means "from the same folder we are currently in".
from .models import Category, Link

# Register your models here.

# ==========================================
# ANALOGY: Think of the Django Admin area as a secure control room or VIP dashboard.
# By registering our models here, we are telling Django to add two new control panels 
# to the VIP dashboard: one for managing our Categories (drawers) and one for our Links (bookmark cards).
# ==========================================

# We register the Category model so that we can create, update, delete, and view categories
# directly from the secure Django Admin web interface.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # This class customizes how the Category model behaves in the admin dashboard.
    
    # list_display defines which columns will be visible when viewing the list of categories.
    # We want to display the ID (database row number) and the name of the category.
    list_display = ('id', 'name')
    
    # search_fields adds a search bar at the top of the category list page,
    # allowing admins to search for categories by their name.
    search_fields = ('name',)

# We register the Link model and customize its look in the admin panel.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    # This class customizes how the Link model behaves in the admin dashboard.
    
    # list_display controls which columns are shown in the links list view.
    # This makes it super easy for an admin to see key information at a single glance:
    # the title, the category it belongs to, the web address, and whether it's approved.
    list_display = ('title', 'category', 'url', 'is_approved')
    
    # list_filter adds a sidebar on the right to let admins quickly filter links.
    # For example, they can view ONLY links that are approved, or ONLY links in a specific category.
    list_filter = ('is_approved', 'category')
    
    # search_fields adds a search bar that searches through the title, description, and URL
    # so admins can find specific bookmarks instantly.
    search_fields = ('title', 'description', 'url')
    
    # list_editable allows the admin to check/uncheck the 'is_approved' checkbox directly
    # from the list view without having to click into the link's detail edit page.
    # This is a massive time-saver for moderators!
    list_editable = ('is_approved',)
