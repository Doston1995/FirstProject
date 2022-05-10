from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=False, blank=True)
    slug = models.CharField(max_length=255, null=False, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/books/')
    price = models.BigIntegerField()
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('title',)