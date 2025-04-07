from django.shortcuts import render # type: ignore

from django.http import HttpResponse # type: ignore

# Create your views here.
def home(request):
    #data from the database
    peoples=[
        {"name":"Mahadev","age":34},
        {"name":"Akash","age":44},
        {"name":"vinod","age":38},
        {"name":"Sandeep","age":15},
    ]
    #Context
    
    return render(request,"index.html",context={'peoples':peoples})

def admin_panel(request):
    return HttpResponse("""<h1>This is admin pannel</h1>""")

