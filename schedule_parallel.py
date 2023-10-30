"""
I am trying to execute 50 items every 10 seconds,
but from the my logs it says it executes every item in 10 second schedule serially, is there a work around?

By default, schedule executes all jobs serially.
The reasoning behind this is that it would be difficult to find a model for parallel execution that makes everyone happy.

You can work around this limitation by running each of the jobs in its own thread:

Я пытаюсь выполнять 50 элементов каждые 10 секунд,
но в моих журналах говорится,
что он последовательно выполняет каждый элемент в 10-секундном расписании, есть ли обходной путь?

По умолчанию расписание выполняет все задания последовательно.
Причина этого в том, что было бы трудно найти модель параллельного выполнения, которая устраивала бы всех.
Это ограничение можно обойти, запустив каждое задание в отдельном потоке:
"""
import threading
import time
import schedule

def job():
    print("I'm running on thread %s" % threading.current_thread())

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)


while 1:
    schedule.run_pending()
    time.sleep(1)

# Если вы хотите более жестко контролировать количество потоков,
# используйте общую очередь заданий и один или несколько рабочих потоков:
def job():
    print("I'm working")


def worker_main():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()

jobqueue = queue.Queue()

schedule.every(10).seconds.do(jobqueue.put, job)
schedule.every(10).seconds.do(jobqueue.put, job)
schedule.every(10).seconds.do(jobqueue.put, job)
schedule.every(10).seconds.do(jobqueue.put, job)
schedule.every(10).seconds.do(jobqueue.put, job)

worker_thread = threading.Thread(target=worker_main)
worker_thread.start()

while 1:
    schedule.run_pending()
    time.sleep(1)

# Эта модель также имеет смысл для распределенного приложения,
# где рабочие процессы — это отдельные процессы, получающие задания из распределенной рабочей очереди.
# использовать beanstalkd с библиотекой beanstalkc Python.
# This model also makes sense for a distributed application
# where the workers are separate processes that receive jobs from a distributed work queue.
# I like using beanstalkd with the beanstalkc Python library.
