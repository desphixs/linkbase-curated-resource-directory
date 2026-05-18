from django.db import models

# Create your models here.

# ==========================================
# ANALOGY: Think of a Category as a drawer in a filing cabinet. 
# Inside this drawer, we can store multiple files (which will be our Links).
# For example, we might have a drawer labeled "Python Tutorials" or "Web Design Tools".
# ==========================================
class Category(models.Model):
    # This class represents a table in our database. It inherits from models.Model, 
    # which is Django's way of saying: "Hey, make this class a database table!"
    
    # We define a field 'name' to store the name of the category.
    # Think of this as the label on the outside of our filing cabinet drawer.
    # We use models.CharField because category names are short pieces of text.
    # max_length=100 restricts the name to 100 characters so users don't write novels here.
    name = models.CharField(max_length=100)

    # The __str__ method is a special Python method that defines how an object is displayed.
    # Without this, Django would display our category as something ugly like "Category object (1)".
    # With this, it displays the actual name, like "Python Tutorials", which is much friendlier!
    def __str__(self):
        # We return the category's name when someone asks to represent this object as a string.
        return self.name


# ==========================================
# ANALOGY: Think of a Link as a specific bookmark card placed inside one of our drawers (Categories).
# Each bookmark card has a title, the web address (URL), a short description, and a stamp showing 
# if a moderator has approved it to be displayed.
# ==========================================
class Link(models.Model):
    # This class creates a "Link" table in our database to store all the shared bookmarks.
    
    # We use a ForeignKey to link this bookmark card to a specific drawer (Category).
    # on_delete=models.CASCADE means if we delete the category (drawer), 
    # all the links (bookmark cards) inside it will also be deleted automatically.
    # related_name='links' lets us easily find all bookmark cards inside a drawer by typing category.links.all().
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='links')
    
    # The title of the link. This is the readable text people click on, like "Django Official Docs".
    # We use CharField for short text, capped at 200 characters.
    title = models.CharField(max_length=200)
    
    # The actual web address where the user will be redirected when they click the link.
    # We use URLField, which is a specialized text field that automatically validates 
    # that the user entered a real, properly formatted website URL (like https://google.com).
    url = models.URLField()
    
    # A longer text field to describe what the link is about.
    # We use TextField because descriptions can be long paragraphs, and TextField 
    # doesn't require a strict max length limit like CharField does.
    description = models.TextField()
    
    # A Boolean field (True/False toggle) to check if a moderator has approved the link.
    # It defaults to False because when a user first submits a link, we want to hide it 
    # until an admin reviews it and approves it (changes it to True).
    is_approved = models.BooleanField(default=False)

    # Just like Category, we define the __str__ method to make our Link objects readable.
    # In the admin panel, Django will now display the title of the bookmark (e.g., "Django Docs").
    def __str__(self):
        # Return the link's title representation
        return self.title
