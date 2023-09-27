import datetime

from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

statuses = ((0, "Полностью отбыл наказание"),
            (1, "Отбывает наказание"))


class Student(models.Model):
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30)
    image = models.ImageField('Фото', upload_to="students/", blank=True, default="students/student-default.png")
    date_of_birth = models.DateField('Дата Рождения')
    date_of_conclusion = models.DateField('Дата заключения')
    accused = models.TextField('Обвиняется')
    judgment = models.TextField('Присудили', max_length=200)
    description = models.TextField('Описание')
    status = models.SmallIntegerField('Статус заключения', choices=statuses)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f'{self.name}, {self.surname}'

    def get_absolute_url(self):
        return reverse('kraty_detail', kwargs={'kraty_slug': self.slug})

    class Meta:
        verbose_name = 'Студэнт'
        verbose_name_plural = 'Студэнты'

    def get_status_txt(self):   # TODO добавить тут перевод (не придумал пока как реализовать)
        if self.status:
            return _("Дзён за кратамi: ") + str((datetime.date.today()-self.date_of_conclusion).days)
        return _("Цалкам адбыў пакаранне")
