from django.db import models

# Create your models here.

class member(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=70, unique=True)
    uicon = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    is_active = models.BooleanField(default=False)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'axf_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name