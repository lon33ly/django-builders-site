# Generated by Django 3.2.5 on 2021-07-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_alter_projects_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='photo',
            field=models.ImageField(upload_to='media/projects-phot/', verbose_name='Фот'),
        ),
    ]
