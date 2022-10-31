from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import front, content,mod_faq,com_section,com_section_content
from .forms import new_user,user_login_form,faq_form,comment_section,comment_section_content
from django.contrib.auth import login, authenticate,logout
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from itertools import chain
from django.db.models import Q,Count




def soft(request):
	top= front.objects.all()
	return render(request,'COLLECTION/BOOKS.html', {"top":top})


def detail_view(request, id):
	grace = get_object_or_404(front, id=id)
	comment=grace.comment.filter(active=True)
	if request.method=="POST":
		comment_form=comment_section(data=request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.grace=grace
			new_comment.save()

		else:
			return redirect("detail_view", id=id)	
	else:
		# return redirect("detail_view", id=id)
		comment_form=comment_section()		
	return render(request,'COLLECTION/detail_view.html', {"grace":grace,"comment_form":comment_form, "comment":comment})



def blog_detail_view(request, id):
	joy = get_object_or_404(content, id=id)
	comment=joy.comment.filter(active=True)
	if request.method=="POST":
		comment_form=comment_section_content(data=request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.joy=joy
			new_comment.save()

		else:
			return redirect("blog_detail_view", id=id)	
	else:
		# return redirect("detail_view", id=id)
		comment_form=comment_section_content()		
	return render(request,'COLLECTION/blog_detail_view.html', {"joy":joy,"comment_form":comment_form, "comment":comment})



def blog(request):
	bottom= content.objects.all()
	return render(request,'COLLECTION/BLOG.html',{"bottom":bottom})

class blog_content(ListView):
	queryset=content.objects.all()
	context_object_name="bottom"
	paginate_by=3
	template_name="COLLECTION/BLOG.html"



def aboutus(request):
	return render(request,'COLLECTION/ABOUT_US.html')


def faq(request):
	faith = mod_faq.objects.all()
	frequent=faith.filter(active=True)
	if request.method=="POST":
		frequent_form=faq_form(data=request.POST)
		if frequent_form.is_valid():
			new_frequent=frequent_form.save(commit=False)
			new_frequent.faith=faith
			new_frequent.save()
			return redirect('faqs')
	else:
		frequent_form=faq_form()		
	return render(request,'COLLECTION/FAQs.html',{"faith":faith,"frequent_form":frequent_form, "frequent":frequent})


def registration(request):
	if request.method =="POST":
		form = new_user(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password_entry = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password_entry)
			# login(request,user)
			messages.success(request,"welcome... Thanks for registering on our website")
			return redirect("login")
		else:
			messages.warning(request,"incorrect details")	
	else:
		form=new_user()

	return render(request,'COLLECTION/REGISTRATION.html',{'form':form})





def login(request):
	if request.method=="POST":
		form=user_login_form(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			user=authenticate(username=cd["username"],password=cd["password"])
			if user is not None:
				if user.is_active:
					login(request,user)
					messages.success(request,"YOU'RE WELCOME")
				return redirect("soft")
			else:
				messages.error(request,"TRY AGAIN")
		else:
			messages.success(request,"YOU'RE WELCOME")
	else:
		form=user_login_form()
	return render(request,'COLLECTION/LOGIN.html',{'form':form})



class searchview(ListView):
	template_name = "COLLECTION/search.html"
	paginate_by=2
	count=0


	def get_context_data(self,**kwargs):
		cxt=super(searchview,self).get_context_data(**kwargs)
		cxt["count"]=self.count or 0
		cxt["query"]=self.request.GET.get("q")
		return cxt

	def get_queryset(self):
		request=self.request
		query=self.request.GET.get("q")

		if query is not None:
			front_result=front.objects.filter(title__icontains=query)
			mod_faq_result=mod_faq.objects.filter(name__icontains=query)
			content_result=content.objects.filter(title__icontains=query)
			com_section_content_result=com_section_content.objects.filter(name__icontains=query)
			com_section_result=com_section.objects.filter(name__icontains=query)
			# hrtbeat_result=hrtbeat.objects.filter(title__icontains=query)
			# emailsending_result=EmailSending.objects.filter(emailsubject__icontains=query)


			result=chain(front_result, content_result, com_section_result, com_section_content_result, mod_faq_result)

			q_result=sorted(result, key=lambda instance:instance.id, reverse=True)
			self.count=len(q_result)
			return q_result
		else:
			return front.objects.none()










	# def faq(request):
	# faith = mod_faq.objects.all()
	# return redirect('faqs')
# Create your views here.
