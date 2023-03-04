from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes per day!",
    "march": "Learn python everyday!",
    "april": "Focus on good diet plans!",
    "may": "Learn django everyday!",
    "june": "Build a new project",
    "july": "Start learning AWS Cloud!",
    "august": "Deploy your project on Cloud!",
    "september": "Start contributing to open source!",
    "october": "Start spreadng your work in community",
    "november": "Launch a new product!",
    "december": "Get a new job!",
}


def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\"><h2>{capitalized_month}</h2></a></li>"

    
    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    print(monthly_challenges[month])
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"<h3>{challenge_text}<h3>")
    except:
        return HttpResponseNotFound("This is not a valid month!")
