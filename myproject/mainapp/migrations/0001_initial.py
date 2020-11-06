# Generated by Django 2.2 on 2020-11-06 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=128)),
                ('publication_year', models.CharField(max_length=10)),
                ('desc', models.TextField(blank=True)),
                ('age', models.CharField(max_length=5)),
                ('cover', models.CharField(max_length=50)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Publisher')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]