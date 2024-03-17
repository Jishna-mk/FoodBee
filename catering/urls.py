from django.urls import path
from .import views


urlpatterns=[
    path('food_view',views.food_view,name="food_view"),
    path("cateringsignup",views.cateringsignup,name="cateringsignup"),
    path("cateringsignin",views.cateringsignin,name="cateringsignin"),
    path("cateringsignout",views.cateringsignout,name="cateringsignout"),
    path('add_food',views.add_food,name="add_food"),
    path('delete_food/<int:pk>/', views.delete_food, name='delete_food'),
    path('edit_food/<int:food_id>/', views.edit_food, name='edit_food'),
    path('book_item/<int:food_id>/', views.book_item, name='book_item'),
    path('delete_booking/<int:food_id>/', views.delete_booking, name='delete_booking'),
    path('user_bookings/',views.user_bookings,name='user_bookings'),
  
   
]