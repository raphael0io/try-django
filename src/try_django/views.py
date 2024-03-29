from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2 ,3 ,4, 5]}
    ##template_name = "title.txt"
    ##template_obj = get_template(template_name)
    ##rendered_string = template_obj.render(context)
    #doc = "<h1>{title}</h1>".format(title=title)
    #django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    #return HttpResponse("<h1>#bethebestyou</h1>")
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About us"})
    
def contact_page(request):
    return render(request, "about.html", {"title": "Contact us"})
     
#def example_page(request):              #returns "hello_world.html"
   # context = {"title": "Example"}
   # something_here = "hello_world.html"
   # return HttpResponse(something_here)

def example_page(request):              #returns an item"
    context         = {"title": "Example"}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)
     