# Generated by Django 3.2.7 on 2021-09-25 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('matn', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rasmlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='rasmlar/')),
                ('maqola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.maqola')),
            ],
        ),
    ]