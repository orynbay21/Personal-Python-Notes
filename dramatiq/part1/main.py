import dramatiq

#broker is needed to reschedule the task or implement it in a different thread
#redis is  a broker
@dramatiq.actor
def factorial(n:int):
    factorial=1
    for i in range(2,n+1):
        factorial*=i
    return factorial
print(factorial(5))