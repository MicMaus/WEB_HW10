from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from collections import Counter

from .models import Quote, Author
from .forms import SignUpForm

from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


def quotes(request):
    quotes_list = Quote.objects.all()
    tag_counts = Counter()

    for quote in quotes_list:
        extracted_tags = [tag.strip("{}") for tag in quote.tags.split(",")]
        tag_counts.update(extracted_tags)

    top_tags = [tag for tag, _ in tag_counts.most_common(10)]

    return render(
        request,
        "polls/quotes.html",
        {"quotes_list": quotes_list, "top_tags": top_tags},
    )


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "polls/author_detail.html", {"author": author})


def quotes_by_tag(request, tag):
    quotes_by_tag_list = Quote.objects.filter(tags__icontains=tag)
    return render(
        request,
        "polls/quotes_by_tag.html",
        {"quotes_by_tag_list": quotes_by_tag_list, "clicked_tag": tag},
    )


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


def custom_login(request):
    password_reset_url = reverse_lazy("polls:password_reset")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("polls:quotes")
    else:
        form = AuthenticationForm()

    return render(
        request,
        "polls/custom_login.html",
        {"password_reset_url": password_reset_url, "form": form},
    )
