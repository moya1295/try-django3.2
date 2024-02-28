from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random

def home_view(request, *args, **kwargs):

    random_id = random.randint(1,2)

    article_obj = Article.objects.get(id=random_id)

    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    HTML_STRING = render_to_string('home_view.html',context=context)
    return HttpResponse(HTML_STRING)