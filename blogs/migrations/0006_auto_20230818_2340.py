# Generated by Django 3.2 on 2023-08-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20230814_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='addition_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blogs',
            name='contextthird',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='titlethird',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
