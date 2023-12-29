from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login

from .models import Quote, Author
from .forms import SignUpForm


def quotes(request):
    quotes_list = Quote.objects.all()
    return render(request, "polls/quotes.html", {"quotes_list": quotes_list})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "polls/author_detail.html", {"author": author})


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("polls:quotes")
    else:
        form = SignUpForm()

    return render(request, "polls/register.html", {"form": form})
