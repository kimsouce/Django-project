from django.shortcuts import render

# Create your views here.

#sy-added

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

#List: 목록
#1) bookmark_list.html 파일로 자동적으로 연결
#2) html 파일로 object_list를 넘겨줌
class BookmarkLV(ListView):
    model = Bookmark

#1) bookmark_detail.html 파일로 자동적으로 연결
#2) html 파일로 object를 넘겨줌
#Detail: 상세페이지
class BookmarkDV(DetailView):
    model = Bookmark

#sy-added
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')