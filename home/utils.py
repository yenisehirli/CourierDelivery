from datetime import timedelta
from django.utils import timezone
from .models import NavigationRecord


def get_last_points():
    threshold_time = timezone.now() - timedelta(hours=48)


    last_points = NavigationRecord.objects.filter(datetime__gte=threshold_time).order_by('vehicle',
                                                                                         '-datetime').distinct(
        'vehicle')

    return last_points
