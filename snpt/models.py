from django.db import models
from django.urls import reverse
import random, string

def gen_slug():
    chars = string.ascii_lowercase + string.digits
    rand = random.choices(chars, k=6)
    return ''.join(rand)


class CodeSnippet(models.Model):
    slug = models.SlugField(max_length=6, default=gen_slug, unique=True)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
    

