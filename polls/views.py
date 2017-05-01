from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Movies
from django.template import loader
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse



def index(request):
    data=Movies.objects.order_by('-pub_date')
    for movie in data:
        if movie.Total_Number_of_Votes==0:
            movie.avg="No one has voted for this yet be the first"
        else:
            movie.avg=movie.Total_Number_of_Stars/movie.Total_Number_of_Votes
    return TemplateResponse(request, 'polls/index.html', {"data": data})



def vote(request, pk):  
    movie=get_object_or_404(Movies, pk=pk)  
    thisVote=movie.choice_set.get(pk=request.POST['myvote'])
    movie.Total_Number_of_Stars=thisVote.Total_Number_of_Stars+ thisVote
    movie.Total_Number_of_Votes += 1
    movie.save() 
    return HttpResponseRedirect(reverse('polls:index.html'))
    

 