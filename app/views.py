from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Profile, Links, User
from .forms import ProfileForm, LinksForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_page')
    return render(request, 'app/index.html')


def page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.user.is_authenticated:
        prof = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=prof)
        links = Links.objects.filter(profile=prof)
        context = {
            "title": "Checking logic for the Profile Page",
            "user": request.user,
            'form': form,
            'links': links,
        }
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                prof = Profile.objects.get(user=request.user)
                prof.name = obj.name
                prof.github = obj.github
                prof.linkedin = obj.linkedin
                prof.twitter = obj.twitter
                prof.description = obj.description
                prof.template = obj.template
                prof.profile_picture = obj.profile_picture
                print(obj.template)
                prof.save()
                # prof.delete()
                # obj.user = User.objects.get(pk=request.user.id)
                # form.save()
                return redirect('profile_page')

        return render(request, 'app/page.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def add_link(request):
    form = LinksForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        link = LinksForm(request.POST)
        profile = Profile.objects.get(user=request.user)
        if link.is_valid():
            new_link = link.save(commit=False)
            new_link.profile = profile
            new_link.save()
            return redirect ('profile_page')
    return render(request, 'app/add_link.html', context)


def linktree_page(request, id):
    profile = Profile.objects.get(user=id)
    links = Links.objects.filter(profile=profile)
    template = get_template(profile.template)
    context = {
        'profile': profile,
        'links': links,
    }
    return render(request, template, context)


def signup_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.filter(username=username).exists()
        if not user:
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('profile_page')
        error = "username already taken"
    return render(request, 'app/signup-user.html', {'error': error})


def link_increment(request, pk):
    link = Links.objects.get(pk=pk)
    link.times_visited += 1
    link.save()
    return redirect(link.link)


def delete_link(request, id):
    link = Links.objects.get(id=id)
    link.delete()
    return redirect('profile_page')


def link_home(request):
    return render(request, 'app/linktree_home.html')


def get_template(template):
    if template == 'bl':
        return 'app/linktree.html'
    if template == 'gr':
        return 'app/linktree-green.html'
    if template == 're':
        return 'app/linktree-red.html'
    if template == 'pu':
        return 'app/linktree-purple.html'
