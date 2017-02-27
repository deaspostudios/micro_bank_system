# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# function to redirect to home
@login_required
def loan_home(request):
    return render(request, 'loan/home/loan_home.html')