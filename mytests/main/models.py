from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tests(models.Model):
    title = models.CharField('Название', max_length=100)
    desc = models.TextField('Описание')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Tasks(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    desc = models.TextField('Задание')

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        order_with_respect_to = 'test'




class Answers(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    desc = models.TextField('Ответ')
    true = models.BooleanField('Верный ответ', default=False)

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата/время', default=timezone.now)
    test = models.ForeignKey(Tests, on_delete=models.DO_NOTHING, verbose_name='Тест')
    tr = models.IntegerField('Количество правильных ответов')
    fs = models.IntegerField('Количество неправильных ответов')
    comment = models.TextField('Комментарий', blank=True)
    id_tasks = models.TextField(default=False)
    def __str__(self):
        return 'Кол-во правильных: '+str(self.tr) + ', кол-во правильных: '+ str(self.fs)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
