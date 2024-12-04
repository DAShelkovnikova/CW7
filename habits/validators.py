from datetime import timedelta

from rest_framework.exceptions import ValidationError


class AssociatedWithoutRewardValidator:
    """
    Исключаем одновременный выбор связанной привычки и указания вознаграждения.
    """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('associted_habit') and habit.get('reward'):
            raise ValidationError(f'Оба поля не могут быть заполнены одновременно.')


class LeadTimeValidator:
    """
    Время выполнения должно быть не больше 120 секунд.
    """

    duration_time = timedelta(seconds=120)

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, habit):
        if habit.get('time_to_complete') and habit.get('time_to_complete') > 120:
            raise ValidationError('Время не должно превышать  120 секунд.')


class NiceHabitInAssociatedValidator:
    """
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('associted_habit'):
            if not habit.get('nice_habit'):
                raise ValidationError(f'В связанные привычки могут попадать только приятные привычки.')


class NiceHabitWithoutValidator:
    """
    У приятной привычки не может быть вознаграждения или связанной привычки.
    """
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, habit):
        if habit.get('nice_habit'):
            if habit.get('reward') or habit.get('associted_habit'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class PeriodicityValidator:
    """
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    """
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, habit):
        periodicity = habit.get('periodicity')
        if 7 < periodicity or periodicity < 1:
            raise ValidationError(f'Для формирования привычки частота выполнения не должна быть не реже 1 раза в '
                                  f'неделю.')