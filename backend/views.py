from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ContactRequestForm, FeedbackForm
from .models import Project, Feedback, Post
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect


class HomePageView(TemplateView):
    template_name = 'backend/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactRequestForm()
        context['feedback_form'] = FeedbackForm()
        context['projects'] = Project.objects.all()
        context['feedback'] = Feedback.objects.all()
        context['posts'] = Post.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if 'submit_contact_form' in request.POST:
            context['contact_form'] = self.process_contact_form(request)
        elif 'submit_feedback_form' in request.POST:
            context['feedback_form'] = self.process_feedback_form(request)
        return render(request, self.template_name, context)

    def process_contact_form(self, request):
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
        return form

    def process_feedback_form(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return form


class PostListView(ListView):
    model = Post
    template_name = 'backend/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3


class CustomLoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Successfully logged in!')
        return response


class CustomLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Successfully logged out!')
        return response


class RegisterUserView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'backend/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully registered!')
        return response
