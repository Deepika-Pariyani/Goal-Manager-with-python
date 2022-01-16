from datetime import date
import plyer 
def daytime():
   today = date.today()
   return today.strftime("%B %d , %Y")

def log_things():
    print("What have you done for your goal today explain --- ")
    n = input()
    return n

def retrive_things():
    with open("deepikagoals.txt") as f:
        print(f.read())

def notifyme():
    plyer.notification.notify(
        title = "LOG SUCCESSFULL",
        message = "Your log is succesfully written to your directory_",
        app_icon ="C:\\Users\\deepika.DESKTOP-8DR82AC\\.vscode\\download.ico",
        timeout = 10,
    )

while True:
  n = int(input("Enter\n1)log\n2)retrieve: "))
  if n == 1:
    with open("deepikagoals.txt","a") as f:
        f.write(str(daytime())+":\n"+str(log_things())+"\n")
        notifyme()
  elif n == 2:
    retrive_things()
  print("\nDo you want to continue?\npress 1 to continue\n2 to exit\n")
  n1 = int(input())
  if n1 == 2:
       break
print("See you next time ;)\nGood Bye :)")

