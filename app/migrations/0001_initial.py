# Generated by Django 5.0.2 on 2024-02-22 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_image', models.ImageField(upload_to='carousel/')),
                ('second_image', models.ImageField(upload_to='carousel/')),
                ('third_image', models.ImageField(upload_to='carousel/')),
            ],
            options={
                'verbose_name': 'Фото карусели',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Кухня')),
            ],
            options={
                'verbose_name': 'Кухня',
                'verbose_name_plural': 'Кухни',
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Уровень сложности')),
            ],
            options={
                'verbose_name': 'Сложность',
                'verbose_name_plural': 'Сложности',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('prep_time', models.TextField(verbose_name='Время приготовления ( A ч. B мин.)')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Фотография')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cuisine', verbose_name='Категория')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Кухня')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.difficulty', verbose_name='Уровень сложности')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('image', models.ImageField(upload_to='instructions/', verbose_name='Фотография')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Инструкция',
                'verbose_name_plural': 'Инструкции',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('unit', models.CharField(max_length=50, verbose_name='Единица (шт, пучок, л, ложка)')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
    ]