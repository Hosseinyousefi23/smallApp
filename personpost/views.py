from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Person, Post


def personPage(request, id):
    person = get_object_or_404(Person, id=id)
    full_name = person.name + ' ' + person.last_name
    post_list = Post.objects.filter(author=full_name).order_by('-publish_time')
    return render(request, 'persons/person.html', {
        'person': person,
        'post_list': post_list,

    })


def mainPage(request):
    post_list = Post.objects.all()
    post_form = PostForm()
    return render(request, 'main/index.html', {
        'post_list': post_list,
        'post_form': post_form,
    })


def post(request):
    post = PostForm(request.POST)
    post.save()
    return HttpResponseRedirect('/post/')