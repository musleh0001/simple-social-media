from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("Post Title"), max_length=100)
    content = models.TextField(_("Post Content"))
    date_posted = models.DateTimeField(_("Post Created At"), default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.title) < 30:
            return self.title
        else:
            return f"{self.title[:30]}..."

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.pk})
