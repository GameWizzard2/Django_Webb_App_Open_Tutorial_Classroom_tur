from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # creates a view
    return HttpResponse('<h1>Hello Django</h1>')

def about(request):
    """ 
    Returns the about page 
    """
    return HttpResponse('<h1>About us</h1> <p>We love merch!</p>')

def contact(request):
    """ 
    Returns the contact page 
    """
    return HttpResponse('<h1>Contact</h1>' +
                        '<p>Phone:000-000-0000<br>Email:Placeholder</p>')

def merch(request):
    """ 
    Returns the merch page 
    """
    return HttpResponse('<h1>Work in progress</h1>')
