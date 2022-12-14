# Generated by Django 4.1.1 on 2022-09-11 15:50

import audio_validator.validator
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import sound.services.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=1024)),
                ('private', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=sound.services.services.get_album_cover_upload_path, validators=[django.core.validators.validate_image_file_extension, sound.services.services.validate_size_image])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('file', models.FileField(upload_to=sound.services.services.get_title_upload_path, validators=[audio_validator.validator.AudioValidator('mp3')])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('private', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=sound.services.services.get_playlist_cover_upload_path, validators=[django.core.validators.validate_image_file_extension, sound.services.services.validate_size_image])),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sound.album')),
                ('genre', models.ManyToManyField(related_name='title_genres', to='sound.genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Аудиозапись',
                'verbose_name_plural': 'Аудиозаписи',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('private', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=sound.services.services.get_playlist_cover_upload_path, validators=[django.core.validators.validate_image_file_extension, sound.services.services.validate_size_image])),
                ('titles', models.ManyToManyField(related_name='title_playlists', to='sound.title')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Плейлист',
                'verbose_name_plural': 'Плейлисты',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_comments', to='sound.title')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'subscriber'), name='follow_unique'),
        ),
    ]
