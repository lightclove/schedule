# Schedule записывает сообщения в Python logger с именем schedule на уровне DEBUG.
# Чтобы получать журналы из расписания, установите уровень ведения журнала DEBUG.
import schedule
import logging

logging.basicConfig()
schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.DEBUG)

def job():
    print("Hello, Logs")

schedule.every().second.do(job)

schedule.run_all()

schedule.clear()

#This will result in the following log messages:
"""
DEBUG:schedule:Running *all* 1 jobs with 0s delay in between
DEBUG:schedule:Running job Job(interval=1, unit=seconds, do=job, args=(), kwargs={})
Hello, Logs
DEBUG:schedule:Deleting *all* jobs
"""
# Кастомизация логгера:
# Самый простой способ добавить многократное ведение журнала к заданиям —
# реализовать декоратор, который обрабатывает ведение журнала.
# В качестве примера ниже код добавляет декоратор print_elapsed_time:
import functools
import time
import schedule

# This decorator can be applied to any job function to log the elapsed time of each job
def print_elapsed_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_timestamp = time.time()
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed in %d seconds' % (func.__name__, time.time() - start_timestamp))
        return result

    return wrapper


@print_elapsed_time
def job():
    print('Hello, Logs')
    time.sleep(5)

schedule.every().second.do(job)

schedule.run_all()

# This outputs:
"""
LOG: Running job "job"
Hello, Logs
LOG: Job "job" completed in 5 seconds
"""
########################################################################################################################