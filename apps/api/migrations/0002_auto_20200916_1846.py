# Generated by Django 3.1.1 on 2020-09-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='frequency',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='plant',
            name='watered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='watered_count',
            field=models.IntegerField(default=False),
        ),
    ]
