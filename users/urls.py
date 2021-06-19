from django.urls import path
from users import views
from .views import login_page,logout_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup.html',views.signup,name='signup'),
    path('home.html',views.home,name='home'),
    path('contactus.html',views.contactus,name='contactus'),
    path('Aboutus.html',views.Aboutus,name='Aboutus'),
    path('signup2.html',views.signup2,name='signup2'),
    
]
