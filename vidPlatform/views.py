from django.shortcuts import render, get_object_or_404
from .models import DateEntry, Choice, Vote
from .forms import VoteForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    todaysEntry = DateEntry.objects.filter(start_date__exact=datetime.date.today())
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterdaysEntry = DateEntry.objects.filter(start_date__exact=yesterday)
    latest_list = DateEntry.objects.order_by("start_date")[:24]
    #print(latest_list)
    template = loader.get_template("vidPlatform/index.html")
    context = {
        "latest_list": latest_list,
        "todays_Entry": todaysEntry,
        "yesterdays_Entry": yesterdaysEntry,
    }
    return HttpResponse(template.render(context, request))



@login_required
def detail(request, dateentry_id):
    user = request.user
    today = datetime.date.today()
    alreadyVotedChoice = None
    userVotetoday = []

    try:
        dateEntry = get_object_or_404(DateEntry, pk=dateentry_id)
        choices = Choice.objects.filter(question=dateEntry)
        userVoteToday = Vote.objects.filter(author = user.id).filter(choice__question__start_date=today)
        if userVoteToday:
            alreadyVotedChoice = userVoteToday[0].choice

    except DateEntry.DoesNotExist:
        raise Http404("date entry doesnt exist")

    


    if (dateEntry.isActive(today)):
        justVoted = False
        if request.method == "POST":
            selectedChoiceID = request.POST.__getitem__("choiceRadio")
            choice = Choice.objects.get(pk=selectedChoiceID)
            theVote = Vote(author=user, choice=choice)
            if userVoteToday:
                userVoteToday.delete()
            alreadyVotedChoice = theVote.choice
            theVote.save()
            justVoted = True

        context = {"entry": dateEntry,
                    "choices": choices,
                    "justVoted": justVoted,
                    }
        if alreadyVotedChoice:
            context["choosen"] = alreadyVotedChoice.id


        return render(request,"vidPlatform/detailPages/detailActive.html", context )
    
    elif(dateEntry.isInTheFuture(today)):
        print("is in future")
        return render(request,"vidPlatform/detailPages/detailFuture.html", {"entry":dateEntry} )
    
    elif (dateEntry.isOver(today)):
        print("is over")
        context = {"entry":dateEntry,
                    "choices":choices, 
                    }
        if userVotetoday:
            context["choosen"] = userVotetoday[0]

        return render(request,"vidPlatform/detailPages/detailOver.html", context=context)
    
    else:
        print("is fucked")
        return Http404("Entry does not exist ")
