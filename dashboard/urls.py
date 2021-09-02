from django.urls import path 
from . import views  
urlpatterns = [
    path('',views.welcome,name='welcome_main_page'),

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminregistration',views.adminregistration,name='adminregistration'),

    path('supplierlogin',views.supplierlogin,name='supplierlogin'),
    path('supplierregistration',views.supplierregistration,name='supplierregistration'),

    path('userlogin',views.userlogin,name='userlogin'),
    path('userregistration',views.userregistration,name='userregistration'),

    path('checkuser',views.checkuser,name="checkuser"),
    path('checksupplier',views.checksupplier,name="checksupplier"),
    path('checkadmin',views.checkadmin,name="checkadmin"),

    path('adminhome',views.adminhome,name="adminhome"),

    path('viewusers',views.viewusers,name="viewusers"),
    path('viewsuppliers',views.viewsuppliers,name="viewsuppliers"),

    path('order',views.order,name="order"),
    path('vieworders',views.vieworders,name="vieworders"),

    path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
    path('deletesupplier/<int:id>',views.deletesupplier,name="deletesupplier"),

    path('viewsupplierorders',views.viewsupplierorders,name="viewsupplierorders"),
    path('userorders/<int:id>',views.userorders,name="userorders"),

    path('issuesupplier/<int:id>',views.issuesupplier,name="issuesupplier"),

    path('deliver/<int:id>',views.deliver,name="deliver"),
    path('userregisucc',views.userregisucc,name="userregisucc"),
    
    path('logintype',views.logintype,name="logintype"),



    path('ud',views.ud,name="ud"),
    path('md',views.md,name="md"),

    path('au',views.au,name="au"),
    path('ua',views.useranalysis,name="ua"),
    path('ua1/<int:id>',views.useranalysis1,name="ua1"),

    path('admin1',views.admin1,name="admin1"),
    path('checkadmin1',views.checkadmin1,name="checkadmin1"),


]