# Generated by Django 5.0.7 on 2024-09-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0026_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subject',
            field=models.CharField(default='exit', max_length=105),
            preserve_default=False,
        ),
    ]
