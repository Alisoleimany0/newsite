from nntplib import ArticleInfo
from typing import Any
from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponseRedirect , HttpResponseForbidden
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormMixin
from .models import Article
from django.views.generic.edit import UpdateView , DeleteView , CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin , UserPassesTestMixin)
from django.db import models
from .forms import CommentForm , ArticleForm
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from articles import forms






# class ArticleListView(ListView):
#     model = Article
#     template_name = "articles/article_list.html"
   
    
def article_list(request):
    articles = Article.objects.all()
    context = {
    'articles': articles ,
    }
    return render(request,"articles/article_list.html",context)

# class  ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse("article_detail",kwargs={"pk":self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={"article":self.object,"writer":self.request.user})
        return context


    def post(self,*args, **kwargs):
        self.object = self.get_object() 
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass

    def form_valid(self,form):
        form.save()
        return super(ArticleDetailView,self).form_valid(form)
    
def article_detail(request,pk):
    # article = Article.objects.get(id = pk)
    article = get_object_or_404(Article,id=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.writer = request.user
            obj.article = article
            obj.save()
            return HttpResponseRedirect(request.path_info)
        else:
            form = CommentForm()
    return render(request,'articles/article_detail.html',{"article":article , "form":form})





# class ArticleUpdateView(LoginRequiredMixin ,UserPassesTestMixin , UpdateView):
    model = Article
    fields = ('title','body')
    template_name = "articles/article_edit.html"
    def get_queryset(self):
        return Article.objects.all()
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
@login_required 
def article_update(request,pk):
    article = get_object_or_404(Article,id=pk)
    if request.user == article.author:
        form = ArticleForm(request.POST or None , instance=article)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/"+"articles/"+str(pk) )
            form = ArticleForm()
        return render(request,"articles/article_edit.html",{"form":form})
    else:
            return HttpResponseForbidden()

# class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')
    def get_queryset(self):
        return Article.objects.all()
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.user == article.author:
        if request.method == "POST":
            article.delete()
            return HttpResponseRedirect("/articles/")
        return render(request, "articles/article_delete.html", {"article": article})
    else:
        return HttpResponseForbidden()



# class ArticlecreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "articles/article_create.html"
    fields = ('title', 'body' )
    def get_queryset(self):
        return Article.objects.all()
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
@login_required
def article_create(request):
    form = ArticleForm()
    if request.method=="POST":
        form = ArticleForm (request.POST,)
        if form.is_valid():
            post_title = form.cleaned_data["title"]
            post_body = form.cleaned_data["body"]
            post_author = request.user
            obj = Article(title=post_title,body=post_body,author=post_author)
            obj.save()
            return HttpResponseRedirect("/"+"articles/")
        else:
            form = ArticleForm()
    return render(request,"articles/article_create.html",{"form":form})


