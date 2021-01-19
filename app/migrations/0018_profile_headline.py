# Generated by Django 3.1 on 2021-01-17 23:56


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_profile_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='headline',
            field=models.CharField(default='', help_text='A headline for your profile', max_length=40, verbose_name='Headline'),
        ),
    ]
