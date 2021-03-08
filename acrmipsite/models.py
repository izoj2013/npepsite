from django.db import models
class Page(models.Model):
    title = models.CharField(max_length=64)
    #picLeft = models.ImageField(width_field=48, height_field=48)
    briefSummary = models.TextField(max_length=256)
    #picRight = models.ImageField(width_field=48, height_field=48)
    content = models.TextField(blank=True)

    class Meta:
        db_table = 'ACR_Page'
