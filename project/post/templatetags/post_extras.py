from django import template

register = template.Library()

@register.filter
def add_link(value):
    content = value.content
    tags = value.tag_set.all()
    for tag in tags:
        content = content.replace('#'+tag.name, '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>')
    return content
