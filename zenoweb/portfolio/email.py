from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Client

class EmailSender:
    def __init__(self):
        self.bookings_sender = settings.EMAIL_HOST_USER

    def send_email(self, sender, recipient_list, subject, template_name, context):

        html_template = render_to_string(template_name, context)
        text_content = "This is an HTML email. Please view it in an email client that supports HTML or contact support@zenoweb.co.ke for more info"

        msg = EmailMultiAlternatives(
            subject = subject,
            body = text_content,
            from_email = sender,
            to = recipient_list
        )
        msg.attach_alternative(html_template, 'text/html')

        try:
            msg.send(fail_silently=False)
            return True
        except Exception as e:
            print(e)
            return False

    def send_booking_and_admin_email(self, user_email):


        try:
            user = Client.objects.get(email=user_email)
        except Client.DoesNotExist:
            return False  


        user_email_sent = self.send_email(
            sender = self.bookings_sender,
            recipient_list = [user.email],
            subject = 'Service Request Confirmation Received',
            template_name = 'emails/booking.html',
            context = {
                'user' : user
            }
        )

        admin_email_sent = self.send_email(
            sender = self.bookings_sender,
            recipient_list = ['njugunajulius953@gmail.com'],
            subject = 'A New User Has Requested For Service',
            template_name = 'emails/booking_admin.html',
            context = {
                'user' : user
            }
        )

        return user_email_sent and admin_email_sent