from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from templated_email import send_templated_mail
# Create your views here.

class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["posts"] = Post.objects.all().order_by('create_date') 
		return context

def ContactView(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')

		send_templated_mail(
			template_name='email',
			from_email='email',
			recipient_list=['bmc3@cin.ufpe.br'],
			context={
				'nome': name,
				'email': email,
				'mensagem': message,
			}
		)
		return HttpResponseRedirect(reverse_lazy('contact'))

	return(render(request,'contact.html'))