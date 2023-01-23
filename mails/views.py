from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def send_mails(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        sender = request.POST['sender']
        recipients = request.POST['recipients']
        send_mail(
            subject,
            message,
            sender,
            [recipients],
        )
        messages.success(request, 'Mail Sent Successfully !!!')
    return render(request, 'form.html')
