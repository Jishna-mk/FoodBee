from django.urls import path
from .import views


urlpatterns=[
    path('',views.index,name="index"),
    path('user_login',views.user_login,name="user_login"),
    path('register',views.register,name="register"),
    path('signout',views.signout,name="signout"),
    path('food_list',views.food_list,name="food_list"),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
    path('sponsors/', views.view_sponsors, name='sponsors_page'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('view_feedbacks/', views.view_feedbacks, name='view_feedbacks'),
  

  
]