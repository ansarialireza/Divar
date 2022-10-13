import time

t_now=int(time.time())
print(t_now)
t_delay=t_now+88888888888888888888888
print(t_delay)
while t_now==int(time.time()):
    #print(time.time())
    pass
print("end")