from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from .tokens import email_verification_token

def send_verification_email(request, user):
    current_site = get_current_site(request)
    subject = 'Verificação de Email'
    
    message = render_to_string('accounts/verification_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_verification_token.make_token(user),
    })
    
    email = EmailMessage(
        subject,
        message,
        to=[user.email]
    )
    email.send()