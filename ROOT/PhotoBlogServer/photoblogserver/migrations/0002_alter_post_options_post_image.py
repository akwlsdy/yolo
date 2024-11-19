# Generated by Django 5.1.1 on 2024-11-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoblogserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]