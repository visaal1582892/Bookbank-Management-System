# Generated by Django 5.0.3 on 2024-03-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bauth',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
