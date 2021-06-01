import time

# define the countdown function 't' is equal to the time argument that is passed in
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
# syntax to structure the format of the timer itself with the minutes and seconds places using a f-string
        timer = '{:02d}:{:02}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
# decrement the unit of time by 1 second
        t -= 1
    print('Your Break is Over!')

t = input('Enter the time in seconds: ')

# changing the user defined input to a numerical value
countdown(int(t))