# Generated by Django 2.0.2 on 2019-01-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('p_date', models.DateTimeField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
