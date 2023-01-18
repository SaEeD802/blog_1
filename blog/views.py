from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import NewPost, SearchForm
from django.db.models import Q

# Create your views here.
def home(request):
    articles = Post.objects.filter(status='pub').order_by('-date_modified')
    form_search = SearchForm()
    if 'search' in request.GET:
        form_search = SearchForm(request.GET)
        if form_search.is_valid():
            s = form_search.cleaned_data['search']
            articles = articles.filter(Q(title__contains= s) | Q(text__contains=s))
    context = {
        'articles': articles,
        'form_search': form_search,
        }
    return render(request, 'blog/home.html', context)


def detail(request, pk):
    article = get_object_or_404(Post, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'blog/detail.html', context)


def create(request):
    if request.method == 'POST':
        forms = NewPost(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = NewPost()
    context = {'forms': forms}
    return render(request, 'blog/addpost.html', context)


def edit(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    forms = NewPost(request.POST or None, instance=posts)
    if forms.is_valid():
        forms.save()
        return redirect('home')
    context = {'forms': forms}
    return render(request, 'blog/addpost.html', context)


def delete(request, pk):
    articles = get_object_or_404(Post, pk=pk)
    articles.delete()

    return redirect('home')

