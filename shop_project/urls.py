from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomeView.as_view() , name='home'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^about/',views.AboutView.as_view(), name='about'),
    url(r'^FAQ/',views.FAQView.as_view(), name='FAQ'),
    url(r'^products/$',views.ProductsView.as_view(), name='products'),
    url(r'^login/',views.LoginView.as_view(), name='login'),
    url(r'^register/',views.RegisterView.as_view(), name='register'),
    url(r'^dashboard/',views.DashboardView.as_view(), name='dashboard'),
    url(r'^profile/',views.ProfileView.as_view(), name='profile'),
    url(r'^logout/',views.LogoutView.as_view(), name='logout'),
    url(r'^products/(?P<id>\d+)/details',views.DetailsView.as_view(id=None), name='product-details'),
    url(r'^products/add/$',views.AddProductsView.as_view(), name='add-product'),

)


