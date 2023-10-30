# Вы можете запускать столько заданий из одного планировщика, сколько пожелаете.
# Однако для больших установок может быть желательно иметь несколько планировщиков.
# Это поддерживается:
import time
import schedule

def fooJob():
    print("Foo")

def barJob():
    print("Bar")

# Create a new scheduler
scheduler1 = schedule.Scheduler()
s
# Add jobs to the created scheduler
scheduler1.every().hour.do(fooJob)
scheduler1.every().hour.do(barJob)

# Create as many schedulers as you need
scheduler2 = schedule.Scheduler()
scheduler2.every().second.do(fooJob)
scheduler2.every().second.do(barJob)

while True:
    # run_pending needs to be called on every scheduler
    scheduler1.run_pending()
    scheduler2.run_pending()
    time.sleep(1)
