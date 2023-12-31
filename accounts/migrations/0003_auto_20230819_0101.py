# Generated by Django 3.2 on 2023-08-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230815_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='fullname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='myuser',
            name='surname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
