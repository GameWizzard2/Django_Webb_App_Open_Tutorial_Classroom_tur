from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    # creates a view
    bands = Band.objects.all()
    return HttpResponse(f"""
                        <h1>Hello Django</h1>
                        <p> A list of bands:<p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                            <li>{bands[3].name}</li>
                            <li>{bands[4].name}</li>
                        """)

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
