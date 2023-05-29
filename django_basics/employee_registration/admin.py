from django.contrib import admin
from employee_registration.models import Company


class CompanyDisplay(admin.ModelAdmin):
    # Record columns to be displayed
    list_display = ("name", "address", "branch")
    # Record columns that, when clicked, redirect to the edit page
    list_display_links = ("name",)
    # Fields that are used in the search bar
    search_fields = ("name", "address")
    # Filter that appears on the right side of the page, grouping records by certain category
    list_filter = ("branch",)
    # Fields to determine the order in which the records are displayed
    ordering = ("name",)
    # Number of records per page
    list_per_page = 10
    # Renders a widget allowing to search for Users
    autocomplete_fields = ("employees",)


# Call this method to bind a model and a display configuration class
admin.site.register(Company, CompanyDisplay)
