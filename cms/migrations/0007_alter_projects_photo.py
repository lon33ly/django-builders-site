# Generated by Django 3.2.5 on 2021-07-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_alter_projects_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='photo',
            field=models.ImageField(upload_to='media/projects-photo/', verbose_name='Фот'),
        ),
    ]