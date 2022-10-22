from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    genre_choice = (
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
        ("Horror", "Horror"),
        ("Mystery", "Mystery"),
        ("Romance", "Romance"),
        ("Thriller", "Thriller"),
        ("Sci-fi", "Sci-fi"),
        ("Others", "Others"),
    )

    gender = models.CharField(max_length=8, choices=gender_choice)
    genre = models.CharField(max_length=20, choices=genre_choice)
    image = models.ImageField(upload_to="images/profile", blank=True)
    pass