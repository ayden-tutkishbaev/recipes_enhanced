from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Cuisine(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Кухня')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'


class Difficulty(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Уровень сложности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'


class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    prep_time = models.TextField(verbose_name='Время приготовления ( A ч. B мин.)')
    image = models.ImageField(upload_to='recipes/', verbose_name='Фотография')
    cuisine = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Кухня')
    category = models.ForeignKey(Cuisine, on_delete=models.CASCADE, verbose_name='Категория')
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, verbose_name='Уровень сложности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Instruction(models.Model):
    title = models.TextField(verbose_name='Название')
    image = models.ImageField(upload_to='instructions/', verbose_name='Фотография')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'


class Ingredients(models.Model):
    title = models.TextField(verbose_name='Название')
    quantity = models.IntegerField(verbose_name='Количество')
    unit = models.CharField(max_length=50, verbose_name='Единица (шт, пучок, л, ложка)')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ингредиенты'


class CarouselImage(models.Model):
    first_image = models.ImageField(upload_to='carousel/')
    second_image = models.ImageField(upload_to='carousel/')
    third_image = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Фото карусели'
