# Generated by Django 3.0.4 on 2020-03-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app1', '0017_entry_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='com',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
