from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField('Имя тега', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField('Текст поста', blank=True, db_index=True)
    image = models.ImageField('Изображение', upload_to='images-of-posts')
    # author = models.CharField('Автор', max_length=150, db_index=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    date_pub = models.DateTimeField('Дата публикации')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_change = models.DateTimeField('Дата изменения', auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date_pub']


