from django.urls import path
from . import views


urlpatterns = [
        path('register/',views.signUpView.as_view(),name="singup"),
        # path('signup/', views.signup_view, name='signup')

]