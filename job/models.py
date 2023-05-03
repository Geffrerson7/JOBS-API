from django.db import models
from django.contrib.auth.models import User
from webPortal.models import WebPortal


class Job(models.Model):
    @property
    def user_email(self):
        return self.user.email

    @property
    def portal_logo(self):
        return self.webPortal.logo

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    webPortal = models.ForeignKey(
        WebPortal, on_delete=models.CASCADE, related_name="webPortal"
    )
    name = models.CharField(max_length=200)
    url = models.URLField()
    company = models.CharField(max_length=200)
    applicationDate = models.DateField(auto_now_add=True)
    publicationDate = models.DateField()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "Job"