from django.db import models


class WebPortal(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    prefixe = models.CharField(max_length=200, default="")
    logo = models.URLField(max_length=500)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Web_Portal"
