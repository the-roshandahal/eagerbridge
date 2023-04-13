# Generated by Django 4.0.3 on 2023-04-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homecontent',
            options={'verbose_name_plural': '09.Home Page Content'},
        ),
        migrations.RenameField(
            model_name='homecontent',
            old_name='about_content',
            new_name='intro_text',
        ),
        migrations.RenameField(
            model_name='homecontent',
            old_name='about_sub_text',
            new_name='intro_title',
        ),
        migrations.RenameField(
            model_name='homecontent',
            old_name='about_title',
            new_name='message_title',
        ),
        migrations.RemoveField(
            model_name='homecontent',
            name='about_image',
        ),
        migrations.AddField(
            model_name='homecontent',
            name='message',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
