from django.urls import path

from employee_registration.views import SignupView, CompaniesListView, EmployeeView

# A route is created using the path function,
# which receives the URL as the first argument and the view as the second one
urlpatterns = [
    path('signup', SignupView.as_view()),
    path('companies', CompaniesListView.as_view()),
    path('employees/add', EmployeeView.as_view())
]
