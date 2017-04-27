from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Movies
from django.template import loader
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse



def index(request):
    data=Movies.objects.order_by('-pub_date')
    return TemplateResponse(request, 'polls/index.html', {"data": data})
    
    
    
    
#    movie_list=Movies.objects.order_by('-pub_date')
# #movie=get_object_or_404(Movies,pk=1)
#    template=loader.get_template('polls/index.html')
#    context={
#        'movie_list': movie_list,
#    }
#    return HttpResponse(template.render(context,request))
   


   
    #return HttpResponse("Hello, world. You're at the polls index.")
    
 