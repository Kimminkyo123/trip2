# Generated by Django 2.2.3 on 2019-07-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freeboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(blank=True, max_length=100, verbose_name='one Line description')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='up load Date')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'ordering': ['upload_date'],
            },
        ),
    ]
