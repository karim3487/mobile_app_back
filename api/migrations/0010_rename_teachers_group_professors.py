# Generated by Django 4.2 on 2023-05-22 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_groupprofessor_delete_groupteacher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='teachers',
            new_name='professors',
        ),
    ]
