from django.db import models


class Comment(models.Model):
    body = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    last_updated_data = models.DateTimeField(auto_now=True)
    is_inappropriate = models.BooleanField(default=False)

    RANKING_CHOICES = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    ranking = models.IntegerField(choices=RANKING_CHOICES, default=0)

    def __str__(self):
        return "Comentario: " + self.body
