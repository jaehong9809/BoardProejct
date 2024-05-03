from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from boardapp import models


@csrf_exempt
def board_home(request):
    articles = models.Article.objects.all().values()

    context = {
        "articles": articles
    }
    return render(request, 'index.html', context)


def one_board(request, id):
    article = models.Article.objects.get(pk=int(id))

    context = {
        "article": article
    }
    return render(request, "one_article.html", context)


@csrf_exempt
def add_one_board(request):
    if request.method == 'GET':
        return render(request, "add.html")

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        models.Article(title=title, body=content).save()

        return redirect("/")


def delete_one_board(request, id):
    article = get_object_or_404(models.Article, pk=int(id))
    article.delete()

    return redirect("/")


@csrf_exempt
def update_one_board(request, id):
    if request.method == 'GET':
        article = models.Article.objects.get(pk=int(id))

        context = {
            "article": article
        }

        return render(request, 'update.html', context)

    else:
        title = request.POST['title']
        content = request.POST['content']
        article = models.Article.objects.get(pk=int(id))

        article.title = title
        article.body = content
        article.save()

        return redirect("/")
