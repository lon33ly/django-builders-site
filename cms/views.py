from django.shortcuts import render, redirect
from .models import Projects, IndexBadges, ContactBadges, Team
from django.contrib import messages
from .forms import RequestsForm


def start_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def team_page(request):
    team_list = Team.objects.all()
    context = {'team_list': team_list}

    return render(request, 'team.html', context)


def projects_page(request):
    projects_list = Projects.objects.all()
    context = {'projects_list': projects_list}

    return render(request, 'projects.html', context)


def contact_page(request):
    contact_badges_list = ContactBadges.objects.all()
    context = {'contact_badges_list': contact_badges_list}

    if request.method == 'POST':
        form = RequestsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                success_message = "Ваше сообщение было отправлено, спасибо за обращение!"
                messages.success(request, success_message)

                return redirect('/contact/#sended_form')
            except Exception:
                pass

    form = RequestsForm()
    context['form'] = form

    return render(request, 'contact.html', context)
