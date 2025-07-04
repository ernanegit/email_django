# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from .models import CustomUser
from .utils import send_verification_email
from .tokens import email_verification_token

class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        if not user.is_email_verified:
            messages.warning(
                self.request,
                'Por favor, verifique seu email antes de fazer login.'
            )
            return redirect('accounts:verify_email_sent')
        
        login(self.request, user)
        return redirect('accounts:dashboard')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(request, user)
            messages.success(
                request,
                'Conta criada! Verifique seu email para ativar a conta.'
            )
            return redirect('accounts:verify_email_sent')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    
    if user and email_verification_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Email verificado com sucesso!')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Link de verificação inválido.')
        return redirect('accounts:register')

def verify_email_sent(request):
    return render(request, 'accounts/verify_email_sent.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
# Create your views here.
