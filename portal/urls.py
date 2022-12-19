from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.parcels, name='parcels'),
    path('routes/', views.routes, name = 'routes'),
    path('tracker/', views.tracker, name = 'tracker'),
    path('dispatch/', views.readyDispatch, name = 'dispatch'),
    path('dispatch/<str:pk>', views.send_dispatch, name = 'submitDispatch'),
    path('customers/', views.customer, name = 'customers'),
    path('customer/<str:pk>', views.updateCustomer, name = 'updateCustomer'),
    path('parcels/updates/<str:pk>', views.updateParcel, name = 'updateParcel'),
    path('partner/driver', views.addPartner, name = 'addPartner'),
    path('rank/', views.addTaxiRank, name = 'addTaxiRank'),
    path('parcels/partner/<str:pk>', views.updatePartner, name = 'updatePartner'),
    path('parcels/submit/', views.send_parcel, name = 'send_parcel'),
    path('delete_parcel/<str:pk>', views.deleteParcel, name = 'deleteParcel'),
    path('register/', views.register, name = 'register'),
    path('signup/', views.signupPage, name = 'signup'),
    path('login/', views.signinPage, name = 'login'),
    path('logout/', views.signinPage, name = 'logout'),
    path('application/', views.users, name = 'userProfile'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='resetPasswordSent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='resetPasswordForm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetPasswordDone.html'), name='password_reset_complete'),
    
]