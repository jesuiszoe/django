from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.

def index(request):
    return HttpResponse("hello")

def test(request):
    return HttpResponse("<h2>Test</h2>")


def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        
       # if username == 'exit':
       #     return HttpResponse("나가기")
       # elif username == 'codingon' :
       #      return render(req, 'loginx.html')
    
    members = Members(
             username = username,
             useremail = email

        )
        members.save
        return HttpResponse("<h2>"+username+"</h2>")
    
    return render(req, 'index.html')
