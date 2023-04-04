from django.shortcuts import render

# dummy posts
posts = [
    {
        'author': 'anAuthor',
        'title': 'First Blog!',
        'content': 'First!',
        'date_posted': '4/4/23'
    },
    {
        'author': 'newGuy',
        'title': '2ND Blog!',
        'content': '2ND!',
        'date_posted': '4/5/23'
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
        'title': About
    }
    return render(request, 'blog/about.html', context)
# Create your views here.
