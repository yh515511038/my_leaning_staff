from django.urls import path
from . import views

urlpatterns = [
    ## Single, alone path definitions
    path("", views.index),
    # path('january/', views.january),
    # path('february/', views.february),
    
    ## Dynamic path definitions
    path("<int:month>/", views.monthly_challenge_by_number),
    path("<str:month>/", views.monthly_challenge, name="monthly-challenge"),
]
