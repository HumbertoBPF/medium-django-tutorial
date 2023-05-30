from django.contrib import admin
from employee_registration.models import Company


class CompanyDisplay(admin.ModelAdmin):
    list_display = ("name", "address", "domain")
    list_display_links = ("name",)
    search_fields = ("name", "address")
    list_filter = ("domain",)
    ordering = ("name",)
    list_per_page = 10
    autocomplete_fields = ("employees",)


admin.site.register(Company, CompanyDisplay)
