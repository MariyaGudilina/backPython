from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    Type = (
        ('tank', "Танк"),
        ('healers', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('guild_masters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('leatherworkers', 'Кожевники'),
        ('alchemists', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний'),
    )
    name = models.CharField(max_length=64, choices=Type, default='tank')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    Type = (
        ('tank', "Танк"),
        ('healers', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('guild_masters', 'Гилдмастеры'),
        ('quest_givers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('leatherworkers', 'Кожевники'),
        ('alchemists', 'Зельевары'),
        ('spell_masters', 'Мастера заклинаний'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', related_name='ads')
    category = models.CharField(max_length=64, choices=Type, default='tank')
    name = models.CharField('заголовок', max_length=80)
    description = models.TextField('текст', max_length=500)
    image = models.ImageField('изображение', upload_to='images/items/%Y/%m/%d')
    content = models.TextField('дополнительный контент', null=True, blank=True)
    url = models.URLField('ссылка', blank=True)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='online: ')
    created = models.DateTimeField(default=timezone.now, verbose_name='дата создания: ')

    # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с постами
    def get_absolute_url(self):
        return f'/post/{self.id}'

    def __str__(self):
        return f'{self.category}, {self.name}, {self.description[:50]}, {self.image}, {self.content}, {self.created}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created']


class Comment(models.Model):
    name = models.CharField('имя', max_length=64)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='объявление', related_name='comments')
    body = models.TextField('комментарий', max_length=120)
    email = models.EmailField('E-Mail')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания: ')
    active = models.BooleanField('принято', default=False)

    def __str__(self):
        return 'комментарий {} от {}'.format(self.name, self.post)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ('active', '-created')
