# Generated by Django 5.0.4 on 2024-04-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0008_mang_arvatud'),
    ]

    operations = [
        migrations.AddField(
            model_name='mang',
            name='mang_labi',
            field=models.BooleanField(default=False),
        ),
    ]