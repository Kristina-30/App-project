from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import PostForm, EditProfileForm

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# from .forms import ImageForm
from .forms import ProfileUpdateForm





class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"

class CreateNewPost(CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        post = Post.objects.create(
            text = request.POST.get("text"),
            author = request.user,
        )
        return render(
            request,
            "includes/post.html",
            {
                "post": post,
                "show_detail_link": True,
            },
            content_type = "application/html"
        )
    
class AddPostView(FormView):
    template_name = "feed/new_post.html"
    form_class=PostForm
    success_url = "/"
    
    def form_valid(self, form):
        # Create a new Post
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image'],
            author = self.request.user
        )
        return super().form_valid(form)




def ViewProfile(request):
    args = {'user': request.user}
    return render(request, "feed/profile_view.html", args)

def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile_view')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'feed/profile_edit.html', args)
    

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile_view')
        else:
            return redirect('/profile_view/edit/change_password')
    
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'feed/change_password.html', args)
    

def change_image(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            # update_session_auth_hash(request, form.user)
            return redirect('/profile_view')
        else:
            return redirect('/profile_view/edit/change_image')
    
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
        args = {'form': form}
        return render(request, 'feed/change_image.html', args)



def search_venues(request):
    model = User
    # context_object_name = 'all_search_results'
    if request.method == 'POST':
        user_name = request.POST['user_name']
        usernames = User.objects.filter(username__contains=user_name)
        return render(request, 'feed/search_venues.html', {'user_name':user_name, 'usernames':usernames})
    else:
        return render(request, 'feed/search_venues.html', {})
    

