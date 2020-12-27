from django.shortcuts import render

def open_register_template(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        pass
