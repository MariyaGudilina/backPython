# Generated by Django 4.1.7 on 2023-03-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('tank', 'Танк'), ('healers', 'Хилы'), ('dd', 'ДД'), ('traders', 'Торговцы'), ('guild_masters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('leatherworkers', 'Кожевники'), ('alchemists', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], default='tank', max_length=64),
        ),
    ]
