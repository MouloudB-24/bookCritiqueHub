from django.db import models

from bookcritique import settings


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'followed_user'], name='unique_follow')]

    def __str__(self):
        return f"{self.user.username} suits {self.followed_user.username}"
