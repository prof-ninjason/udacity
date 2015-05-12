import time
import webbrowser
  
tot_breaks = 300
cnt_break  = 0

print("Started: " + time.ctime())

def do_it():
    webbrowser.open("https://www.youtube.com/watch?v=X5X_i09-iZU")
    webbrowser.open("https://www.youtube.com/watch?v=Phvc5iPYF4M")
    webbrowser.open("https://www.youtube.com/watch?v=qh7fQFQHuPs")
    webbrowser.open("https://www.youtube.com/watch?v=hnqL8KS31I0")

do_it()

while (cnt_break < tot_breaks):
    do_it()
    time.sleep(3*60)
    cnt_break = cnt_break + 1

print("Ended: " + time.ctime())