import dramatiq

#broker is needed to reschedule the task or implement it in a different thread
#redis is  a broker
@dramatiq.actor
def factorial(n:int):
    factorial=1
    for i in range(2,n+1):
        factorial*=i
    return factorial
#print(factorial.send(5))
# when u use workers they gonna do the tasks u send them in a different process
# to create an image
#docker run -d --name redis -p 6379:6379 redis/redis-stack-server:latest
# to run redis CLI in the terminal
#docker exec -it redis redis-cli

#to send the task to a worker
#dramatiq main
#and then u have to create another terminal
# and another file the test_main1.py
# and then run it
# and u will get the answer