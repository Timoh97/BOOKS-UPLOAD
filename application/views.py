from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movies


# Create your views here.


def upload(request):
	if request.method == "POST":
		form = MovieForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("application:upload")
	form = MovieForm()
	movies = Movies.objects.all()
	return render(request=request, template_name="main/upload.html", context={'form':form, 'movies':movies})