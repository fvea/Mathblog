# Generated by Django 3.1.2 on 2020-10-18 07:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_QA', '0004_auto_20201018_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
