from django.shortcuts import render,redirect

from django.contrib import messages

from django.views.generic import View

from myapp.forms import MovieForm

from myapp.models import Movies




# Create your views here.


class MovieCreatview(View):

    def get(self,request,*args,**kwargs):

       form_instance=MovieForm()

       return render(request,"movie-add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.create(
                title=data.get("title"),
                genre=data.get("genre"),
                language=data.get("language"),
                year=data.get("year"),
                run_time=data.get("run_time"),
                director=data.get("director"),

            )

            messages.success(request,"movie hasbeen added")

            return redirect("movie-list")
        
        else:
           
           messages.error(request,"failed to add movie")
           
           return render(request,"movie-add.html",{"form":form_instance}) 
          
class MovieListview(View):

     def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movie-list.html",{"movies":qs})
     
     #moviedetailview
     #url:lh:8000/movies/<int:pk>/
     #method:get


class MovieDetailview(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,"movie-detail.html",{"movie":qs})

    
     #moviedeletelview
     #url:lh:8000/movies/<int:pk>/remove/
     #method:get


class MovieDeleteview(View):

    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id).delete()

        messages.success(request,"movie hasbeen removed")

        return redirect("movie-list")
    
    

class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id)

        data={
            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "director":movie_obj.director,
            "run_time":movie_obj.run_time,

        }
        
        form_instance=MovieForm(initial=movie_obj)

        return render(request,"movie-edit.html",{"form":form_instance})
        
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Movies.objects.filter(id=id).update(**data)

            return redirect("movie-list")
        
        else:
           
           return render(request,"movie-edit.html",{"form":form_instance})
    







