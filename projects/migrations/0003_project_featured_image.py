# Generated by Django 4.2.7 on 2023-11-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
