
from django.db import models

class Article(models.Model):        
    title = models.CharField(max_length=100)
    content = models.TextField()
    #image = models.ImageField(default='null')
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True) #Para obtener la fecha de creacion
    update_date = models.DateTimeField(auto_now = True) #Para obtener la fecha de actualización

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['id']

    def __str__(self):
        if self.public:
            publico = "(Publicado)"
        else:
            publico = "(Privado)"
        return f"{self.title} -> {publico}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    create_date = models.DateField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']