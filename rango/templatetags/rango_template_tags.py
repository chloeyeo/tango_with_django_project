from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    # if parameter isn't passed along, None is used instead,
    # i.e. None is the default value for the parameter,
    # implying there is no currently selected category.
    return {'categories': Category.objects.all(),
            'current_category': current_category}
