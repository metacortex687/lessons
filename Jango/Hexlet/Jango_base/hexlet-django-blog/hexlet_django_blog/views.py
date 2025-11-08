from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World",
        }
    )


def about(reques):
    return render(
        reques,
        "about.html"
    )