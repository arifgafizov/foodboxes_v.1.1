# Generated by Django 3.1.5 on 2021-01-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('published_at', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('new', 'новый на модерации'), ('published', 'опубликован'), ('hidden', 'скрыт')], max_length=100)),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
            },
        ),
    ]
