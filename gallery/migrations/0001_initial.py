# Generated by Django 3.2.9 on 2021-11-28 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.CharField(max_length=30)),
                ('descripton', models.TextField()),
                ('time_uloaded', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ManyToManyField(to='gallery.Category')),
                ('location_taken', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.location')),
            ],
        ),
    ]