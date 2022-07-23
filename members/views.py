from django.shortcuts import render , get_object_or_404 
from django.core.mail import send_mail

from django.http import HttpResponse
from .models import Article 
from .forms  import Contact_Form 
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger  
# Create your views here.


def home(request) : 
	posts = Article.objects.all()
	paginator = Paginator(posts , 1 )
	page = request.GET.get('page')

	try : 
		posts = paginator.page(page)

	except PageNotAnInteger : 
		posts = paginator.page(1)

	except EmptyPage : 
		posts = paginator.page(paginator.num_pages)

  
	return render(request , 'site/index.html' , {'posts':posts , 'page':page} )


def post_list(request) : 
	pass 





def about(request) : 
	return render(request , 'site/about.html' , {} )


def detail_post(request , slug , id ) : 
	post = get_object_or_404(Article , slug = slug , id = id )

	

	return render(request , 'site/detail_post.html' , {'post' : post })

def forms_contact_me(request ) : 
	form1 = Contact_Form(request.POST or None )
	if form1.is_valid() : 
		full_name = form1.cleaned_data['full_name'] 
		title = form1.cleaned_data['title']
		email = form1.cleaned_data['email']
		message = form1.cleaned_data['message']
		file = form1.cleaned_data['file']

		add_Contact = Contact.objects.create(full_name = full_name , 
			title  = title , email = email , message = message , file = file )

		add_Contact.save()
		form1 = Contact_Form()

	return render(request , 'site/contact.html' , {'form':form1})