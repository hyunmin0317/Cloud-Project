from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from place.models import Place

register = template.Library()

@register.simple_tag
def confirm_like(username, post_id):
    try:
        user = User.objects.get(username=username)
        place = get_object_or_404(Place, id=post_id)
        if (user in place.voter.all()):
            return 'like'
        return 'unlike'
    except:
        return 'unlike'