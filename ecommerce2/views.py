from django.shortcuts import render


def about(request):
	return render(request, "about.html", {})


def find_library(request):
	return render(request, "find_library.html", {})