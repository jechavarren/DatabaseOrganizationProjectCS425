from django.urls import path
from . import views
from .views import custom_user_creation_view


urlpatterns = [
    path('signup/', views.custom_user_creation_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('home/', views.home, name='home'),
    path('renter/', views.renter, name='renter'),
    path('agentview/', views.agentview, name='agentview'),
    path('payinfomod/', views.payinfomod, name='payinfomod'),
    path('billingsuccess/', views.billingsuccess, name='billingsuccess'),
    path('addinfomod/', views.addinfomod, name='addinfomod'),
    path('addsuccess/', views.addsuccess, name='addsuccess'),
    path('propertyview/', views.add_property, name='propertyview'),
    path('propertysuccess/', views.propertysuccess, name='propertysuccess'),
    path('propertyselection/', views.propertyselection, name='propertyselection'),
    path('housesearch/', views.housesearch, name='housesearch'),
    path('apartmentsearch/', views.apartmentsearch, name='apartmentsearch'),
    path('commercialsearch/', views.commercialsearch, name='commercialsearch'),
    path('book/', views.book, name='book'),
    path('successfulbooking/', views.successfulbooking, name='successfulbooking'),
    path('managebookinga/', views.managebookinga, name='managebookinga'),
    path('managebookingsr/', views.managebookingsr, name='managebookingsr'),
    path('bookrent/', views.bookrent, name='bookrent'),
    path('bookdeleter/', views.bookdeleter, name='bookdeleter'),
    path('bookview/', views.bookview, name='bookview'),
    path('bookagent/', views.bookagent, name='bookagent'),
    path('agentcancel/', views.agentcancel, name='agentcancel'),




    # other URL patterns go here
]
