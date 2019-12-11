# Generated by Django 2.2.2 on 2019-12-10 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uploadartwork.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('subject', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('width', models.CharField(max_length=255)),
                ('height', models.CharField(max_length=255)),
                ('depth', models.CharField(max_length=255)),
                ('medium', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('styles', models.CharField(max_length=255)),
                ('is_framed', models.BooleanField(default=False)),
                ('is_copyright', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=uploadartwork.models.Images.get_user_image_folder, verbose_name='Image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadartwork.ArtWork')),
            ],
        ),
    ]