from django.db import models

from CW7.settings import AUTH_USER_MODEL


NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Пользователь",
        **NULLABLE
    )
    place = models.CharField(
        max_length=50,
        verbose_name="Место",
        help_text="Укажите из какой области будет привычка",
        **NULLABLE
    )
    time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время",
        help_text="Установите время выполнения привычки",
        **NULLABLE
    )
    action = models.CharField(
        max_length=50,
        verbose_name="Действие ",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    nice_habit = models.BooleanField(
        default=True,
        verbose_name="Признак приятной привычки",
        **NULLABLE
    )
    associted_habit = models.ForeignKey(
        "self", verbose_name="Связанная привычка", on_delete=models.CASCADE, **NULLABLE
    )
    periodicity = models.IntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Укажите периодичность выполнения привычки для напоминания в днях (по умолчанию ежедневная)",

    )
    reward = models.CharField(verbose_name="Вознаграждение", **NULLABLE)
    time_to_complete = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время на выполнение",
        **NULLABLE
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Признак публичности", **NULLABLE
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"