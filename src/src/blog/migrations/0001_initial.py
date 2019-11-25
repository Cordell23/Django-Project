# Generated by Django 2.0.7 on 2019-10-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.CharField(max_length=240)),
                ('date', models.DateField(auto_now=True)),
                ('article', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
    ]