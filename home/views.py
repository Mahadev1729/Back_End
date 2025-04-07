from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    #data from the database
    peoples=[
        {"name":"Mahadev","age":34},
        {"name":"Akash","age":44},
        {"name":"vinod","age":38},
        {"name":"Sandeep","age":45},
    ]
    #Context
    
    return render(request,"index.html",context={'peoples':peoples})

def admin_panel(request):
    return HttpResponse("""<h1>This is admin pannel</h1>""")

