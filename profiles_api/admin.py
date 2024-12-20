from django.contrib import admin
from profiles_api import models

# Define the UserProfileAdmin
class UserProfileAdmin(admin.ModelAdmin):
    # These fields should correspond to the fields used for the `autocomplete_fields`
    search_fields = ['name', 'email']  # Replace with actual fields in your UserProfile model
    list_display = ['email', 'is_staff']
    list_filter = ['is_staff',]
# Register the UserProfile model and associate it with UserProfileAdmin
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Hobbies)
admin.site.register(models.Position)
