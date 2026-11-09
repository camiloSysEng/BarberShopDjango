from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('email', ''),
            password=request.POST.get('password', ''),
        )
        if user is not None:
            login(request, user)
            return redirect('inicio')
        messages.error(request, 'El correo o la contraseña no son válidos.')

    return render(request, 'cuentas/login.html')