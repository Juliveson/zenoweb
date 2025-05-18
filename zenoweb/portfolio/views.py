from django.shortcuts import render
from django.http import JsonResponse
from .models import Client
from .email import EmailSender

def home(request):
    return render(request, 'portfolio/home.html')

def service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')
        details = request.POST.get('details')
        
        for client in Client.objects.all():
            if client.email == email:
                return JsonResponse({'error': 'A client with that email address exists. Please Choose another email.'},  status=400)
         
        client = Client.objects.create(name=name, email=email, service=service, service_date=date, project_details=details)
        client.save()

        emailer = EmailSender()
        emails_sent = emailer.send_booking_and_admin_email(email)

        if emails_sent:
            return JsonResponse({'success': 'Your request was submitted and confirmation sent to your email.'},  status=200)
        else:
            return JsonResponse({'error': 'Service booking failed. Please try again later'},  status=400)

    return JsonResponse({'message': 'Service endpoint'})
