# Generated by Django 4.0.4 on 2022-07-25 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mood_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('Content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_mood', to='mood_app.content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_fave', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
