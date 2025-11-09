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
    tags = ["обучение","программирование","python","oop"]
    return render(
        reques,
        "about.html",
        context={"tags": tags}
    )