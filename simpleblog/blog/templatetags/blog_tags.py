from django import template
from ..models import Tag, Post


register = template.Library()


@register.simple_tag()
def get_posts_by_tag(tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags=tag)
    return posts


