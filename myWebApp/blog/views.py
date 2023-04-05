from django.shortcuts import render

# dummy posts
posts = [
    {
        'author': 'anAuthor',
        'title': 'First Blog!',
        'content': 'First!',
        'date_posted': '3/22/23'
    },
    {
        'author': 'newGuy',
        'title': '2nd Blog!',
        'content': '2ND!',
        'date_posted': '3/23/23'
    }
]

# handle traffic from home page of blog
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': "about"
    }
    return render(request, 'blog/about.html', context)
# Create your views here.
