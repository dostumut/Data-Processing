import json

from celery import current_task, task
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)


def lines_number():
    return sum(1 for line in open(settings.PATH_TO_DATA_FILE))


@task(name="do_amount_of_events_per_application_calculation")
def do_amount_of_events_per_application_calculation():
    """ Get some rest, asynchronously, and update the state all the time """
    total_lines = lines_number()
    count = {}
    with open(settings.PATH_TO_DATA_FILE) as f:
        for num, line in enumerate(f, 1):
            data = json.loads(line)
            app = data['application']['name']
            if app in count:
                count[app] += 1
            else:
                count[app] = 1
            # logger.info('lines processed: {} of {}'.format(num, total_lines))
            current_task.update_state(state='PROGRESS',
                                      meta={'current': num, 'total': total_lines})

    return count





@task(name="do_product_launched_calculation")
def do_product_launched_calculation():
    #Get some rest, asynchronously, and update the state all the time
    total_lines = lines_number()
    count_launch = {}
    with open(settings.PATH_TO_DATA_FILE) as f:
        for number, newline in enumerate(f, 1):
            newdata = json.loads(newline)
            appnew = newdata['type']
            if appnew in count_launch:
                count_launch[appnew] += 1
            else:
                count_launch[appnew] = 1
            # logger.info('lines processed: {} of {}'.format(num, total_lines))
            current_task.update_state(state='PROGRESS',
                                      meta={'current': number, 'total': total_lines})

    return count_launch



@task(name="do_duplicates_calculation")
def do_duplicates_calculation():
    #Get some rest, asynchronously, and update the state all the time
    total_lines = lines_number()
    count_duplicates = {}
    with open(settings.PATH_TO_DATA_FILE) as f:
        for number, newline in enumerate(f, 1):
            eventdata = json.loads(newline)
            appnew = eventdata['event_id']
            if appnew in count_duplicates:
                count_duplicates[appnew] += 1
            else:
                count_duplicates[appnew] = 1
            # logger.info('lines processed: {} of {}'.format(num, total_lines))
            current_task.update_state(state='PROGRESS',
                                      meta={'current': number, 'total': total_lines})
    count_duplicates = dict((k, v) for k, v in count_duplicates.items() if v >= 2)
    return count_duplicates






