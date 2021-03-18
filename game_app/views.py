from django.shortcuts import render, redirect
import random

def index (request):
    if 'computer_number' not in request.session:
        request.session ['computer_number'] = random.randint(1,100)

    return render(request, "index.html")

def result (request):
    request.session['too_high'] = False
    request.session['too_low'] = False
    request.session['just_right'] = False
    request.session['error'] = False

    if(len(request.POST['user_number']) != 0 ):
        if(request.session ['computer_number']>int(request.POST['user_number'])):
            print ('too low')
            request.session['too_low'] = True
        elif(request.session ['computer_number']<int(request.POST['user_number'])):
            print ('too high')
            request.session['too_high'] = True
        elif(request.session ['computer_number']==int(request.POST['user_number'])):
            request.session['just_right'] = True
    else:
        request.session['error'] = True
    return redirect("/")

def reset (request):
    request.session.flush()
    return redirect('/')