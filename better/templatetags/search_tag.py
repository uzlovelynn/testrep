from django import template
from django.views.generic import ListView
register = template.Library()

from ..models import front,content,com_section,com_section_content,mod_faq


@register.filter()
def search_tag(value):
	return value.__class__.__name__
