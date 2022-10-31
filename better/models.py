from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class front(models.Model):	
	title=models.CharField(max_length=300)
	name=models.CharField(max_length=300)
	image=models.ImageField(upload_to='images/%Y/%m/%d')
	time=models.DateTimeField(default=timezone.now)
	body=models.TextField()

	def __str__(self):
		return self.title



class content(models.Model):	
	title=models.CharField(max_length=300)
	name=models.CharField(max_length=300, null="true")
	image=models.ImageField(upload_to='images/%Y/%m/%d')
	time=models.DateTimeField(default=timezone.now)
	sub_body=models.CharField(max_length=1000)
	body=models.TextField()

	def __str__(self):
		return self.title



class mod_faq(models.Model):
	Question=models.TextField()
	active=models.BooleanField(default=True)
	name=models.CharField(max_length=300)
	time=models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering=("time",)

	def __str__(self):
		return "Question by {} on  {}". format(self.name)


class com_section(models.Model):
	# post=models.ForeignKey(content,related_name="comment", on_delete=models.CASCADE)
	grace=models.ForeignKey(front,related_name="comment", on_delete=models.CASCADE)
	message=models.TextField()
	active=models.BooleanField(default=True)
	name=models.CharField(max_length=300)
	time=models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering=("time",)

	def __str__(self):
		return "comment by {} on  {}". format(self.name,self.post)	



class com_section_content(models.Model):
	# post=models.ForeignKey(content,related_name="comment", on_delete=models.CASCADE)
	joy=models.ForeignKey(content,related_name="comment", on_delete=models.CASCADE)
	message=models.TextField()
	active=models.BooleanField(default=True)
	name=models.CharField(max_length=300)
	time=models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering=("time",)

	def __str__(self):
		return "comment by {} on  {}". format(self.name,self.joy)						





