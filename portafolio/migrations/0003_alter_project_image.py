# Generated by Django 4.2.4 on 2023-08-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portafolio/images/'),
        ),
    ]
