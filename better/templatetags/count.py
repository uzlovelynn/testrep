from django import template

register = template.Library()

from ..models import content

@register.simple_tag
def total_count():
	return front.objects.all().count()


# @register.inclusion_tag('report/recent_post.html')
# def show_updated_post(count=4):
# 	updated_post= introduction.objects.order_by('-time')[:count]
# 	return {"updated_post":updated_post}