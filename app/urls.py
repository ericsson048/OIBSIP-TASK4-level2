from django.urls import path,include
from .views import home,LoginView,SignupView


urlpatterns = [
    path('home/', home, name="home"),
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),

]
