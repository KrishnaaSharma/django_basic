
# We are in urls.py file of core app

from django.urls import path
from . import views

#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------------------

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('suits_categories/',views.SuitCategoriesView.as_view(),name='suitscategories'),

    #------- shirt View Functions ------------
    path('shirts_categories/',views.ShirtCategoriesView.as_view(),name='shirtcategories'),

    #------- sherwani View Functions ------------
    path('sherwani_categories/',views.sherwani_categories.as_view(),name='sherwanicategories'),

    path('products',views.products,name='products'),
    path('productdetails/<int:id>/',views.product_details, name='productdetails'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.log_in,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logoutpage/', views.logout_page, name='logoutpage'),  # confirmation page

    path('logout/',views.log_out, name="logout"),

    path('changepassword/',views.changepassword, name="changepassword"),
    path('add_to_cart/<int:id>',views.add_to_cart, name="addtocart"),
    path('view_cart/',views.view_cart, name="viewcart"),
    path('add_quantity/<int:id>',views.add_quantity, name="add_quantity"),
    path('delete_quantity/<int:id>',views.delete_quantity, name="delete_quantity"),
    path('delete_cart/<int:id>',views.delete_cart, name="deletecart"),
    path('address/',views.address,name='address'),
    path('delete_address/<int:id>',views.delete_address,name='deleteaddress'),
    path('checkout/',views.checkout,name='checkout'),
    path('payment_success/<int:selected_address_id>',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
    path('payment/',views.payment,name='payment'),
    path('order/',views.order,name='order'),
    path('buynow/<int:id>',views.buynow,name='buynow'),
    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),
    path('buynow_payment_success/<int:selected_address_id>/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
    path('forgotpassword/',views.forgot_password, name="forgotpassword"),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='resetpassword'),
    path('password_reset_done/', views.password_reset_done, name='passwordresetdone'),
]




#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)