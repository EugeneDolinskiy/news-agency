from django.shortcuts import render
from django.views import generic

from news_management.models import Redactor, Newspaper, Topic


def index(request):
    """View function for the home page of the News Agency site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "news_management/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news_management/topic_list.html"
    paginate_by = 5
