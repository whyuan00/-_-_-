from django.db import models
from django.conf import settings

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜

    def __str__(self):
        return f"{self.user.username} - comment {self.id}"
