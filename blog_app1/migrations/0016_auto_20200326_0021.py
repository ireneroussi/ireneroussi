# Generated by Django 3.0.4 on 2020-03-25 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app1', '0015_com'),
    ]

    operations = [
        migrations.AlterField(
            model_name='com',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app1.Entry'),
        ),
    ]