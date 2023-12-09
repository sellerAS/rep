# Generated by Django 4.0 on 2023-12-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='LOGIN')),
                ('firstname', models.CharField(max_length=20, verbose_name='FIO')),
                ('lastname', models.CharField(max_length=20, verbose_name='FAMILYA')),
                ('email', models.EmailField(max_length=50, verbose_name='EMAIL')),
            ],
            options={
                'db_table': 'autors',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=20, verbose_name='Заголовок')),
                ('content', models.TextField(default='', verbose_name='Содержание')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activity_flag', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='i', max_length=1)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor', verbose_name='автор')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['-published_at'],
                'permissions': [('can_publish', 'Может опубликовать новость')],
            },
        ),
    ]
