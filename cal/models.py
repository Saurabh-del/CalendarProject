from django.db import models
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    start_time = models.DateField()
    end_time = models.DateField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.title
