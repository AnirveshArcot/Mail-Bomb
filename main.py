import threading 
import yagmail
import os
import time 

def mail(sm,pwd,rm,sub,mes):
    yag = yagmail.SMTP(user=sm,password=pwd)
    yag.send(to=rm,subject=sub,contents=mes)

user_file=open("user.json","r")
sendermail=user_file.readline()
password=user_file.readline()
receivemail=input("Enter target: ")
subject=input("Enter subject: ")
message=input("Enter message: ")
thread_count=int(input("Enter number of threads (Recommended=10): "))
times=int(input("Enter number of times the threads have to run: "))
atat=input("Enter attachment file name with extention: ")
direc=os.getcwd()
fulldirec=direc+"\\"+atat
contents=[message,fulldirec]

for j in range (times):
    threads = []
    for i in range (thread_count):
        x= threading.Thread(target=mail,args=(sendermail,password,receivemail,subject,contents))
        x.daemon=True
        threads.append(x) 
    for i in range (thread_count):
        threads[i].start()
    for i in range (thread_count):
        threads[i].join()

print("Done!")
user_file.close()
