# Generated by Django 3.0.6 on 2020-05-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200530_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='department',
            field=models.CharField(choices=[('HR', 'Human Resource'), ('ST', 'Software Testing'), ('JD', 'Junior Developer')], default='HR', max_length=50),
        ),
    ]
