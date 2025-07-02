from django.shortcuts import render

# Create your views here.
def show_phography(request):
    return render(request, 'photography/php_list.html')

def create_photography(request):
    return render(request, 'photography/php_form.html')
