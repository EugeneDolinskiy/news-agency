from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from news_management.models import Redactor, Newspaper, Topic
from news_management.forms import (
    RedactorCreateForm,
    NewspaperForm,
    NewspaperTitleSearchForm,
    RedactorUsernameSearchForm,
    TopicNameSearchForm,
)


class IndexView(generic.TemplateView):
    template_name = "news_management/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_redactors"] = Redactor.objects.count()
        context["num_newspapers"] = Newspaper.objects.count()
        context["num_topics"] = Topic.objects.count()

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits + 1

        return context


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "news_management/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("name", "")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset.order_by("name")


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news_management:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news_management:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news_management:topic-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "news_management/newspaper_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperTitleSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("title", "")
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset.order_by("title")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperRedactorUpdateView(LoginRequiredMixin, generic.View):
    def post(self, request, pk, action):
        newspaper = get_object_or_404(Newspaper, pk=pk)

        if action == "add":
            newspaper.publishers.add(request.user)
        elif action == "remove":
            newspaper.publishers.remove(request.user)

        return redirect("news_management:newspaper-detail", pk=pk)


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("news_management:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse(
            "news_management:newspaper-detail", kwargs={"pk": self.object.pk}
        )


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news_management:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("username", "")
        if search_query:
            queryset = queryset.filter(username__icontains=search_query)
        return queryset.order_by("username")


class RedactorRegisterView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("news_management:index")

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            "Your registration was successful! You can now log in."
        )
        return super().form_valid(form)


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("news_management:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspaper_set__topic")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorCreateForm

    def get_success_url(self):
        return reverse(
            "news_management:redactor-detail", kwargs={"pk": self.object.pk}
        )
