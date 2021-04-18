from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView,DetailView,ListView,View
from .models import theme,post,comment
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse
from django.http import Http404,HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.

class RedirectToPreviousMixin:

    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']


class HomepageView(ListView):
    template_name='main/home/index.html'
    context_object_name ='themes'
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q and q != '':
            return theme.objects.filter(name__icontains=q)
        else:
            return theme.objects.order_by('name')


def ThemeView(request,theme_slug):
    t=theme.objects.get(theme_slug=theme_slug)
    p = t.post_set.order_by('-id')
    context={
        'theme': t ,
        'posts':p
    }
    return render(request, 'main/home/theme.html',context)


def PostView(request,post_slug,theme_slug):
    p=post.objects.get(post_slug=post_slug)
    t=theme.objects.get(theme_slug=theme_slug)
    p.post_views=p.post_views+1
    p.save()
    c = p.comment_set.order_by('-id')
    context={
        'theme':t,
        'post':p ,
        'comments':c,

    }
    return render(request, 'main/home/post.html',context)

class ThemeCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView,):
    model = theme
    action = 'add theme'
    fields = ['name']
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_theme'
    success_message = '"%(name)s" was created successfully'

class PostCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView,):
    model = post
    action = 'add post to theme'
    fields = ['theme','name','description','link','file','video','audio','Img','Img2','Img3','Img4'
    ,'Img5','Img6','Img7','Img8','Img9','Img10']
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_post'
    success_message = '"%(name)s" was created successfully'

class PostCreateView2(PermissionRequiredMixin,SuccessMessageMixin,CreateView,):
    model = post
    action = 'add post to theme'
    fields = ['name','description','link','file','video','audio','Img','Img2','Img3','Img4'
    ,'Img5','Img6','Img7','Img8','Img9','Img10']
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_post'
    success_message = '"%(name)s" was created successfully'

    def form_valid(self, form):
        t = get_object_or_404(theme, theme_slug=self.kwargs['theme_slug'])
        form.instance.theme = t
        return super(PostCreateView2, self).form_valid(form)


class PostUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView,):
    model = post
    action = 'edit post'
    fields = ['theme','name','description','link','file','video','audio','Img','Img2','Img3','Img4'
    ,'Img5','Img6','Img7','Img8','Img9','Img10']
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_post'
    success_message = '"%(name)s" was created successfully'

class ThemeUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView,):
    model = theme
    action = 'edit theme'
    fields = ['name']
    success_url = reverse_lazy('main:home')
    permission_required = 'main.add_theme'
    success_message = '"%(name)s" was created successfully'

def leave_comment(request,post_slug,theme_slug):
    p=post.objects.get(post_slug=post_slug)
    t=theme.objects.get(theme_slug=theme_slug)
    p.comment_set.create(user = request.user, text = request.POST['TEXT'] )

    return HttpResponseRedirect( reverse('main:post',args=(t.theme_slug,p.post_slug) ) )

class CommentDeleteView(RedirectToPreviousMixin,DeleteView):
    model = comment
    action = 'delete comment'

class ThemeDeleteView(DeleteView):
    model = theme
    action = 'delete theme'
    success_url = reverse_lazy('main:home')

class PostDeleteView(DeleteView):
    model = post
    action = 'delete post'
    success_url = reverse_lazy('main:home')
