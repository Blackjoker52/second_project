from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date

from home.models import Message
from users.models import CustomUser

#                   The Home Page.
def home(request):
    if request.user.is_anonymous:
        # return redirect("registerClient")
        return render(request, "index.html")
    try:
        myUser = CustomUser.objects.get(user = request.user)
    except Exception as e:
        return redirect("login")
    # User sent a message
    if request.method == "POST":
        allMessages = Message.objects.all()
            
        ''' Adding DATE MARKS '''
        if allMessages.last() == None: # if First Message
            # Adding the first date mark
            dateMessage = Message(text=date.today() , sender="system").save()
        # Else adding Date mark if more than a day has passed after the last message
        elif (date.today() - allMessages.last().date).days != 0:
            dateMessage = Message(text=date.today() , sender="system").save()
   

        # Storing the message in the Database
        text = request.POST.get("sent_message")
        newMessage = Message(text=text, sender="user").save()

        if text.__contains__("hi") or text.__contains__("hello"):
            text = "yes hello, how can I help you"
            newMessage = Message(text=text, sender="bot").save()

        return redirect("home")
        # return render(request, 'home.html', param)

    # Fetching data from the Database
    allMessages = Message.objects.all()

    param = {"allMessages": allMessages, "myUser":myUser}
    return render(request, 'home.html', param)


