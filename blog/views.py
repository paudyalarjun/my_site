from django.shortcuts import render
from django.http import HttpResponse

from datetime import date


all_posts = [
    {
        "slug": "f1-car-racing",
        "image": "F1_car.png",
        "author": "Arjun",
        "date": date(2022, 2, 9),
        "title": "Formula 1 Racing",
        "excerpt": "There's nothing like seeing the cars go around corners at more than 150kmph. And Formula 1 provides that exact scenario. Isn't it amazing?",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
            Lorem ipsum dolor sit amet consectetur adipisicing elit.

            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
            Lorem ipsum dolor sit amet consectetur adipisicing elit.

            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
        """
    },

    {
        "slug": "into-the-wild",
        "image": "into-the-wild.jpg",
        "author": "Arjun",
        "date": date(2022, 2, 8),
        "title": "An Amazing movie- Into the Wild",
        "excerpt": "Christopher McCandless, a young graduate, decides to renounce all his possessions and hitchhike across America. During his journey, he encounters several situations which change him as a person.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
            Lorem ipsum dolor sit amet consectetur adipisicing elit.

            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
            Lorem ipsum dolor sit amet consectetur adipisicing elit.

            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
        """
    },

    {
        "slug": "La-Liga-Football",
        "image": "la-liga.jpg",
        "author": "Arjun",
        "date": date(2022, 2, 8),
        "title": "La Liga",
        "excerpt": "The Campeonato Nacional de Liga de Primera División, commonly known simply as Primera División in Spain, and as La Liga in English-speaking countries and officially as LaLiga Santander for sponsorship reasons, stylized as LaLiga, is the men's top professional football division of the Spanish football league system.",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
            Lorem ipsum dolor sit amet consectetur adipisicing elit.

            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
            Lorem ipsum dolor sit amet consectetur adipisicing elit.

            Hic exercitationem debitis, reprehenderit quae odio itaque non consectetur officiis
            modi adipisci corporis obcaecati molestiae quos maxime fugit porro facere molestias vero!
        """
    }
]

def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",
    {"iposts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html")


def posts_detail(request, slug):
    return render(request, "blog/post-detail.html")
