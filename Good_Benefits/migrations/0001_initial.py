# Generated by Django 4.0.6 on 2022-09-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('profile_image', models.TextField()),
                ('user_id', models.TextField()),
                ('view_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecommendPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('profile_image', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
    ]