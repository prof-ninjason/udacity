# imports
import time
import webbrowser

# variables
tot_breaks = 300
cnt_break  = 0

# end timestamp
print("Started: " + time.ctime())

def do_it():
    webbrowser.open("https://www.youtube.com/watch?v=X5X_i09-iZU")
    webbrowser.open("https://www.youtube.com/watch?v=Phvc5iPYF4M")
    webbrowser.open("https://www.youtube.com/watch?v=qh7fQFQHuPs")
    webbrowser.open("https://www.youtube.com/watch?v=hnqL8KS31I0")

while (cnt_break < tot_breaks):
    # perform action once
	do_it()
	
    # perform action every 3 mins
	time.sleep(3*60)
    
	cnt_break = cnt_break + 1

# end timestamp
print("Ended: " + time.ctime(1))
