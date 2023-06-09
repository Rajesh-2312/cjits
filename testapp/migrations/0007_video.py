# Generated by Django 4.1.7 on 2023-04-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_document_filename_document_semister_document_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default=None, max_length=200)),
                ('description', models.TextField()),
                ('video_file', models.FileField(upload_to='events/')),
            ],
        ),
    ]
