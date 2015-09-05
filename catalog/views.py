#untuk merender template
from django.shortcuts import render

#modul untuk menggunakan class based view
from django.views.generic import TemplateView

#modul untuk autehtifikasi user, login dan logout user
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from catalog.form import UserForm, BrandForm, ProductForm, Product
#object user yang login

#untuk meredirect user dari satu view ke view lain

#modul untuk merubah nama URL menjadi URL yang digunakan untuk redirect


# Create your views here.
class HomeView(TemplateView):

    template_name = 'home/index.html'

    def get(self, request):
        return render(request,self.template_name)

class AboutView(TemplateView):

    template_name = 'home/about.html'

    def get(self, request):
        return render(request,self.template_name)

class FAQView(TemplateView):

    template_name = 'home/FAQ.html'

    def get(self, request):
        return render(request,self.template_name)

class ProductsView(TemplateView):

    template_name = 'home/products.html'

    def get(self, request):
        return render(request,self.template_name)

class AddProductsView(TemplateView):

    template_name = 'admin/add-products.html'

    def get(self, request):
        form = ProductForm()
        return render(request,self.template_name, {'form': form})

    def post(self, request):
        product = None
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid():
            new_product = form.save(commit= False)
            new_product.save()
            return HttpResponseRedirect(reverse('product-details', kwargs={'id': new_product.id}))

        else:
            return render(request,self.template_name, {'form': form})




class DetailsView(TemplateView):
    template_name = 'home/details.html'
    id = None

    def get(self, request, id):
       product = Product.objects.get(id=id)
       return render(request, self.template_name, {'product': product})




class RegisterView(TemplateView):

    template_name = 'home/register.html'

    def get(self, request,):
        form = UserForm()
        return render(request,self.template_name, {'form': form})

    def post(self, request):
        user = None
        form = UserForm(request.POST or None, instance=user)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('login'))

        else:
            return render(request, self.template_name, {'form: form'})



class DashboardView(TemplateView):

    template_name = 'home/dashboard.html'

    def get(self, request):
        user = request.user
        return render(request,self.template_name, {'user': user})




class LoginView(TemplateView):

    template_name = 'home/login.html'

    def get(self, request):
        return render(request,self.template_name)

    def post(self,request):
        #grab data from the web form
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticate the account
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))

        return render(request,self.template_name)

class ProfileView(TemplateView):
    template_name = 'home/profile.html'
    def get(self, request):
       return render(request,self.template_name)

class LogoutView(TemplateView):

    template_name = 'home/logout.html'
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))









