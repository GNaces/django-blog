# Generated by Django 4.2.16 on 2024-10-30 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='update_on',
            new_name='updated_on',
        ),
    ]
