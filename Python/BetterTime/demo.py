import BetterTime; from time import sleep

timer = BetterTime.Timer()
timer.start()
sleep(5)
timer.stop()
print(timer.get())