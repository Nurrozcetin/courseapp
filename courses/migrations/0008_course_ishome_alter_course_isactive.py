# Generated by Django 5.0.7 on 2024-08-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_remove_course_category_course_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isHome',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
