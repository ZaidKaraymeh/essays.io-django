# Generated by Django 3.2.5 on 2021-07-19 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_essay_essay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='essay',
            old_name='essay',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='essay',
            old_name='essayTitle',
            new_name='title',
        ),
    ]