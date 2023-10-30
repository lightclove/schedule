# Обработка исключений¶
# Расписание не отлавливает исключения, возникающие во время выполнения задания.
# Поэтому любые исключения, возникающие во время выполнения задания, будут всплывать и прерывать функцию run_xyz расписания.
# Если вы хотите защититься от исключений, вы можете обернуть свою функцию работы в декоратор следующим образом:
import functools

from util.schedule import schedule


def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob
        return wrapper
    return catch_exceptions_decorator

@catch_exceptions(cancel_on_failure=True)
def bad_task():
    return 1 / 0

schedule.every(5).minutes.do(bad_task)

