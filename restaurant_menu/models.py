from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    ("starters", "Starters"),
    ("main_course", "Main Course"),
    ("salads", "Salads"),
    ("drinks", "Drinks"),
    ("sides", "Sides"),
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available"),
    (2, "Cooking"),
)


class MenuItem(models.Model):
    meal = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    status = models.IntegerField(max_length=200, choices=STATUS, default=1)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn"
                                                     ":ANd9GcS5PTsuRj6pjDdRDNqaC27k705rxveiomd99w&s")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal} {self.status}"

