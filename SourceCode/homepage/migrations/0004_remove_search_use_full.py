# Generated by Django 4.1.3 on 2023-02-02 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_search_h_alter_search_w_alter_search_x_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='use_full',
        ),
    ]