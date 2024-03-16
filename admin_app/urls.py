from django.urls import path
from .import views



urlpatterns=[
    path('admin_signin', views.admin_signin, name='admin_signin'),
    path('viewCaterings',views.viewCaterings,name="viewCaterings"),
    path('admin_signout',views.admin_signout,name='admin_signout'),
    path('approveCatering/<int:m_id>/',views.approveCatering,name="approveCatering"),
    path('removeCatering/<int:m_id>/',views.removeCatering,name="removeCatering"),
]