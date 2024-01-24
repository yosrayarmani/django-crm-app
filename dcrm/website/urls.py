from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('login/', views.login_user, name='login'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_user, name='register'),
  # URL pattern that includes variable <int:pk> (primary key: id record in the DB table) and associates it with a view (views.customer_record)
  path('record/<int:pk>', views.customer_record, name='record'),
#   "record/<int:pk>" : this string is part of the url pattern that defines the url path (url: "record/"+ integer (value of integer will be holded by variable called 'pk')
# when user accesses url: "/record/2", django will capture 2 as the value of "pk" and pass it to the 'custumer_record' view
# in the view we use 'pk' to retrieve the corresponding record from the DB 
]