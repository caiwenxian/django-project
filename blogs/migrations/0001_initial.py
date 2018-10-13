# Generated by Django 2.1.1 on 2018-09-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author_id', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('type', models.IntegerField(verbose_name=4)),
                ('browseAmount', models.IntegerField(verbose_name=8)),
                ('commentAmount', models.IntegerField(verbose_name=8)),
                ('create_date', models.DateTimeField(verbose_name='create date')),
                ('modify_date', models.DateTimeField(verbose_name='modify date')),
            ],
        ),
    ]