from audioop import reverse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from registration.forms import SignupForm
from user.models import Person, Studentity, University, Department, Tag

# registration is done in this view

# @transaction.atomic
def signup(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html', {'form': SignupForm()})

    # elif request.method == 'POST'

    form = SignupForm(request.POST)

    if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        p = Person()
        p.user = user

        user.save()
        p.save()

        s = Studentity()
        s.person = p
        s.student_id = form.cleaned_data['student_id']
        s.department = Department.objects.get(name='unknown')

        s.save()

        return HttpResponseRedirect(reverse('registration_select_initial_tags', args=[user.username, p.id]))

    else:
        return render(request, 'sign-up.html', {'form': form, 'status': 'Notice errors below:'})


# after signup, initial tags will be selected by the new user

def select_initial_tags(request, username, identifier):
    if request.method == 'GET':
        return render(request, 'sing-up-tags.html', {'super_tags': Tag.objects.filter(parent=None)})

    # elif request.method == 'POST'

    person = Person.objects.get(id=identifier)
    super_tags = Tag.objects.filter(parent=None)

    for tag in super_tags:
        if tag.name in request.POST:
            person.interested_tags.add(tag)

    return render(request, 'sing-up-tags.html', {'super_tags': Tag.objects.filter(parent=None)})
