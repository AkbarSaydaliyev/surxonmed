# Generated by Django 4.1.3 on 2022-11-27 14:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_organization_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='category',
        ),
        migrations.AddField(
            model_name='specialist',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.specialistcategory'),
            preserve_default=False,
        ),
    ]
