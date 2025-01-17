from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.conf import settings

# Create your views here
x = datetime.datetime.now()
date = x.strftime("%x")
year = x.year

def index(request):
    return render(request, 'fanisi_atelier_app/index.html', {'year':year})

def about(request):
    return render(request, 'fanisi_atelier_app/about.html', {'year':year})

def services(request):
    return render(request, 'fanisi_atelier_app/services.html', {'year':year})

def portfolio(request):
    return render(request, 'fanisi_atelier_app/portfolio.html', {'year':year})

def blog(request):
    return render(request, 'fanisi_atelier_app/blog.html', {'year':year})

def top_5_interior_design_trends(request):
    return render(request, 'fanisi_atelier_app/top-5-interior-design-trends.html', {'date': date, 'year':year})

def how_to_choose_the_right_color_palette_for_your_home(request):
    return render(request, 'fanisi_atelier_app/how-to-choose-the-right-color-palette-for-your-home.html',{'date':date, 'year':year})

def maximazing_small_spaces_design_tips_and_tricks(request):
    return render(request, 'fanisi_atelier_app/maximazing-small-spaces-design-tips-and-tricks.html',{'date':date, 'year':year})

def the_importance_of_lighting(request):
    return render(request, 'fanisi_atelier_app/the-importance-of-lighting.html',{'date':date, 'year':year})

def terms_and_conditions(request):
    return render(request, 'fanisi_atelier_app/terms-and-conditions.html', {'year':year})

def privacy_policy(request):
    return render(request, 'fanisi_atelier_app/privacy-policy.html', {'year':year})

from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        from_email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')

        try:
            email = EmailMessage(
                subject='New Message from Fanisi Atelier',
                body=f"Name: {name}\n\nMessage: {message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[from_email],
            )
            email.send(fail_silently=False)
            return JsonResponse({'success': 'Email sent successfully'}, status=200)
        except Exception as e:
            print('Error sending email:', e)
            return JsonResponse({'error': 'Error sending email'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def custom_404(request, exception=None):
    return render(request, 'fanisi_atelier_app/404.html', status=404)

def custom_500(request, *args, **argv):
    return render(request, 'fanisi_atelier_app/500.html', status=500)
