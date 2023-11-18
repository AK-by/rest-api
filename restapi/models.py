from django.db import models


class SimpleMessages(models.Model):
    # Простые сообщения (тестовая модель)
    title = models.CharField(name="title", max_length=20, null=False)
    message = models.CharField(name="message", max_length=100, null=True)
    created = models.DateTimeField(name="created", null=False, auto_now_add=True)
    image = models.ImageField(upload_to="messages/", null=True, blank=True)

    # Представление в админке
    class Meta:
        verbose_name = "Простое сообщение"
        verbose_name_plural = "Простые сообщения"

    def __str__(self):
        return self.title
