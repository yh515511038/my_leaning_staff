from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Learn Django for at least 20 minutes every day!",
    "march": "Walk for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Learn Django for at least 20 minutes every day!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september": "Walk for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Learn Django for at least 20 minutes every day!",
    "december": "Walk for at least 20 minutes every day!"
}

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello world!</h1>')

def january(request):
    return HttpResponse('<h1>January</h1>')

def february(request):
    return HttpResponse('<h1>February</h1>')

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f'<h1>{challenge_text}</h1>')
    except:
        return HttpResponseNotFound("Month is invalid!")


def monthly_challenge_by_number(request, month):
    if month < 0 or month >= 12:
        return HttpResponseNotFound("Month is invalid!")
    request_month = list(monthly_challenges.keys())[month - 1]
    redirect_path = reverse('monthly-challenge', args=[request_month])
    return HttpResponseRedirect(redirect_path)
