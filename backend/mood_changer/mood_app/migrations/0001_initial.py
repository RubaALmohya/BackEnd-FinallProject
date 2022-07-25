

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='media/images/content_mood_img')),
                ('video', models.FileField(default='xxxx', null=True, upload_to='media/video')),
                ('description', models.CharField(max_length=450, null=True)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_mood', to='mood_app.mood')),
            ],
        ),
    ]
