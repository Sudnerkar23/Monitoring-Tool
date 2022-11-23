#AUTH: SUDHANSHU NERKAR 
import os
import sys
import socket
import datetime
import time
import tkinter as tk
from random import randint, randrange
from tkinter import *
from PIL import Image,ImageTk
import threading
import subprocess
import datetime
import psutil
import datetime
import os


e = datetime.datetime.now()

e = datetime.datetime.now()

'''print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))'''

FILE = os.path.join(os.getcwd(), "networkinfo.log")
file1 = os.path.join(os.getcwd(), "cpuinfo.log")
file2 = os.path.join(os.getcwd(), "internetinfo.log")
file3 = os.path.join(os.getcwd(), "task-manager.log")


# creating log file in the currenty directory
# ??getcwd?? get current directory,
# os function, ??path?? to specify path

root = Tk()
root.title("SN monitoring tool")
root.geometry('550x750')
root.wm_attributes('-transparentcolor', '#ab23ff')

bg = PhotoImage(file = "network.png")
#bg= Image.open("network.png")
#resize_image = bg.resize((550, 600))
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
#root.config(bg='network.jpeg')
'''load= Image.open("8.png")
resize_image = load.resize((400, 350))
render = ImageTk.PhotoImage(resize_image)
img = Label(root, image=render, anchor=CENTER)
box1 = tk.Label(
    root,
    text="Box 1",
    bg="green",
    fg="white"
)'''




def ping():
  # to ping a particular IP
  try:
    socket.setdefaulttimeout(3)
    
    # if data interruption occurs for 3
    # seconds, <except> part will be executed

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET: address family
    # SOCK_STREAM: type for TCP

    host = "8.8.8.8"
    port = 53

    server_address = (host, port)
    s.connect(server_address)

  except OSError as error:
    return False
    # function returns false value
    # after data interruption

  else:
    s.close()
    # closing the connection after the
    # communication with the server is completed
    return True


def calculate_time(start, stop):

  # calculating unavailability
  # time and converting it in seconds
  difference = stop - start
  seconds = float(str(difference.total_seconds()))
  return str(datetime.timedelta(seconds=seconds)).split(".")[0]


def first_check():
  # to check if the system was already
  # connected to an internet connection

  if ping():
    # if ping returns true
    live = "\nCONNECTION ACQUIRED\n"
    print(live)

    connection_acquired_time = datetime.datetime.now()
    acquiring_message = "connection acquired at: " + \
      str(connection_acquired_time).split(".")[0]
    print(acquiring_message)

    with open(FILE, "a") as file:
    
      # writes into the log file
      file.write(live)
      file.write(acquiring_message)

    return True

  else:
    # if ping returns false
    not_live = "\nCONNECTION NOT ACQUIRED\n"
    print(not_live)

    with open(FILE, "a") as file:
    
      # writes into the log file
      file.write(not_live)
    return False


def network():
  print("\n\n\n\n===================NETWORK MONITORING======================")
  # main function to call functions
  monitor_start_time = datetime.datetime.now()
  monitoring_date_time = "monitoring started at: " + \
    str(monitor_start_time).split(".")[0]

  if first_check():
    # if true
    print(monitoring_date_time)
    
    # monitoring will only start when
    # the connection will be acquired

  else:
    # if false
    while True:
    
      # infinite loop to see if the connection is acquired
      if not ping():
        
        # if connection not acquired
        time.sleep(1)
      else:
        
        # if connection is acquired
        first_check()
        print(monitoring_date_time)
        break

  with open(FILE, "a") as file:
  
    # write into the file as a into networkinfo.log,
    # "a" - append: opens file for appending,
    # creates the file if it does not exist???
    file.write("\n")
    file.write(monitoring_date_time + "\n")

  while True:
  
    # infinite loop, as we are monitoring
    # the network connection till the machine runs
    if ping():
      
      # if true: the loop will execute after every 5 seconds
      time.sleep(5)

    else:
      # if false: fail message will be displayed
      down_time = datetime.datetime.now()
      fail_msg = "disconnected at: " + str(down_time).split(".")[0]
      print(fail_msg)

      with open(FILE, "a") as file:
        # writes into the log file
        file.write(fail_msg + "\n")

      while not ping():
      
        # infinite loop, will run till ping() return true
        time.sleep(1)

      up_time = datetime.datetime.now()
      
      # after loop breaks, connection restored
      uptime_message = "connected again: " + str(up_time).split(".")[0]

      down_time = calculate_time(down_time, up_time)
      unavailablity_time = "connection was unavailable for: " + down_time

      print(uptime_message)
      print(unavailablity_time)
      with open(FILE, "a") as file:
        
        # log entry for connection restoration time,
        # and unavailability time
        file.write(uptime_message + "\n")
        file.write(unavailablity_time + "\n")


#-------------------------------------------------------------------------------


import psutil

#measure cpu time

def monitor_cpu_times():
  #print("==========CPU/PC HEALTH MONITORING=============")
  c1 =Label(root,text="CPU/PC HEALTH MONITORING STATISTICS:",font=("Arial Bold", 12),anchor =CENTER)
  c1.place(x=70,y=130)
  #print("\n CPU TIMES")
  with open(file1, "a") as filec:
    filec.write("\n\n CPU TIMES")
  c2 =Label(root,text="CPU TIMES:",font=("Arial bold", 10),anchor =CENTER)
  c2.place(x=40,y=160)
  cpu_times = psutil.cpu_times()
  user_time = round(cpu_times.user/3600)
  system_time = round(cpu_times.system/3600)
  idle_time = round(cpu_times.idle/3600)
  c3 =Label(root,text="Time spent on processes by the User: {}".format(user_time),font=("Arial", 10),anchor =CENTER)
  c3.place(x=190,y=160) 

  c4 =Label(root,text="Time spent on processes by the System: {}".format(system_time),font=("Arial", 10),anchor =CENTER)
  c4.place(x=190,y=180)

  c5 =Label(root,text="Time spent on processes by Idle: {}".format(idle_time),font=("Arial", 10),anchor =CENTER)
  c5.place(x=190,y=200)
  with open(file1, "a") as filec:
    filec.write("\nTime spent on processes by the User: {}".format(user_time))
    filec.write("\nTime spent on processes by the System: {}".format(system_time))
    filec.write("\nTime spent on processes by Idle: {}".format(idle_time))

  #print("Time spent on processes by the User: {}".format(user_time))
  #print("Time spent on processes by the System: {}".format(system_time))
  #print("Time spent on processes by Idle: {}".format(idle_time))


#measure cpu util
def monitor_cpu_util():
  c6 =Label(root,text="CPU Utilisation:",font=("Arial bold", 10),anchor =CENTER)
  c6.place(x=40,y=240)

  c7 = Label(root,text=psutil.cpu_percent(),font=("Arial", 10),anchor =CENTER)
  c7.place(x=190,y=240)
  #print("\n CPU UTIL")
  #print(psutil.cpu_percent())
  with open(file1, "a") as filec:
    filec.write("\n\n CPU UTIL\n")
    filec.write(str(psutil.cpu_percent()))



#count working cpu cores
def monitor_cpu_cores():
  c8 =Label(root,text="Working CPU cores:",font=("Arial bold", 10),anchor =CENTER)
  c8.place(x=40,y=280)

  c9 = Label(root,text=psutil.cpu_count(),font=("Arial", 10),anchor =CENTER)
  c9.place(x=190,y=280)
  #print("\n CPU CORES")
  #print(psutil.cpu_count())
  with open(file1, "a") as filec:
    filec.write("\n\n CPU CORES\n")
    filec.write(str(psutil.cpu_count()))


#Measure CPU frequencies
def monitor_cpu_freq():
  c10 =Label(root,text="CPU frequencies :",font=("Arial bold", 10),anchor =CENTER)
  c10.place(x=40,y=320)

  c11 = Label(root,text="{} Mhz".format(psutil.cpu_freq().current),font=("Arial", 10),anchor =CENTER)
  c11.place(x=190,y=320)
  #print("\n CPU FRQUENCIES")
  #print("{} Mhz".format(psutil.cpu_freq().current))
  with open(file1, "a") as filec:
    filec.write("\n\n CPU FRQUENCIES\n")
    filec.write("\n{} Mhz".format(psutil.cpu_freq().current))

#Monitor RAM usage
def monitor_ram():
  #print("\n RAM USAGE")
  c10 =Label(root,text="RAM USAGE :",font=("Arial bold", 10),anchor =CENTER)
  c10.place(x=40,y=360)
  virtual_memory = psutil.virtual_memory()
  c11 = Label(root,text="Total Memory :{} bytes".format(virtual_memory.total),font=("Arial", 10),anchor =CENTER)
  c11.place(x=190,y=360)
  c12 = Label(root,text="Available Memory :{} bytes".format(virtual_memory.available),font=("Arial", 10),anchor =CENTER)
  c12.place(x=190,y=380)
  c13 = Label(root,text="Used Memory :{} bytes".format(virtual_memory.used),font=("Arial", 10),anchor =CENTER)
  c13.place(x=190,y=400)
  c14 = Label(root,text="Percentage Used :{}%".format(virtual_memory.percent),font=("Arial", 10),anchor =CENTER)
  c14.place(x=190,y=420)
  #print("Total Memory :{} bytes".format(virtual_memory.total))
  #print("Available Memory :{} bytes".format(virtual_memory.available))
  #print("Used Memory :{} bytes".format(virtual_memory.used))
  #print("Percentage Used :{}%".format(virtual_memory.percent))
  with open(file1, "a") as filec:
    filec.write("\n\n RAM USAGE\n")
    filec.write("Total Memory :{} bytes".format(virtual_memory.total))
    filec.write("\nAvailable Memory :{} bytes".format(virtual_memory.available))
    filec.write("\nUsed Memory :{} bytes".format(virtual_memory.used))
    filec.write("\nPercentage Used :{}%".format(virtual_memory.percent))
    

'''#Monitor disk partitions
def monitor_disk():
  print("\n DISK PARTITIONS")
  print(psutil.disk_paritions())
  '''

#disk utilisation
def monitor_disk_usage():
  c15 =Label(root,text="DISK UTILISATION :",font=("Arial bold", 10),anchor =CENTER)
  c15.place(x=40,y=460)
  #print("\n DISK USAGE")
  disk_usage = psutil.disk_usage('/')
  c14 = Label(root,text="Total Memory {} bytes".format(disk_usage.total),font=("Arial", 10),anchor =CENTER)
  c14.place(x=190,y=460)
  c15 = Label(root,text="Free Memory {} bytes".format(disk_usage.free),font=("Arial", 10),anchor =CENTER)
  c15.place(x=190,y=480)
  c16 = Label(root,text="Used Memory {} bytes".format(disk_usage.used),font=("Arial", 10),anchor =CENTER)
  c16.place(x=190,y=500)
  c17 = Label(root,text="Percentage used {}%".format(disk_usage.percent),font=("Arial", 10),anchor =CENTER)
  c17.place(x=190,y=520)
  #print("Total Memory {} bytes".format(disk_usage.total))
  #print ("Free Memory {} bytes".format(disk_usage.free))
  #print("Used Memory {} bytes".format(disk_usage.used))
  #print("Percentage used {}%".format(disk_usage.percent))
  with open(file1, "a") as filec:
    filec.write("\n\n DISK USAGE")
    filec.write("\nTotal Memory {} bytes".format(disk_usage.total))
    filec.write("\nFree Memory {} bytes".format(disk_usage.free))
    filec.write("\nUsed Memory {} bytes".format(disk_usage.used))
    filec.write("\nPercentage used {}%".format(disk_usage.percent))



  
  
#Monitor Network Requests
def monitor_network():
  c18 =Label(root,text="NETWORK REQUESTS :",font=("Arial bold", 10),anchor =CENTER)
  c18.place(x=40,y=560)
  #print("\n NETWORK REQUESTS")
  io_stats = psutil.net_io_counters()
  c19 = Label(root,text="Total Bytes Sent {}".format(io_stats.bytes_sent),font=("Arial", 10),anchor =CENTER)
  c19.place(x=190,y=560)
  c20 = Label(root,text="Total Bytes Received {}".format(io_stats.bytes_recv),font=("Arial", 10),anchor =CENTER)
  c20.place(x=190,y=580)
  #print("Total Bytes Sent {}".format(io_stats.bytes_sent))
  #print("Total Bytes Received {}".format(io_stats.bytes_recv))
  with open(file1, "a") as filec:
    filec.write("\n\n NETWORK REQUESTS")
    filec.write("\nTotal Bytes Sent {}".format(io_stats.bytes_sent))
    filec.write("\nTotal Bytes Received {}".format(io_stats.bytes_recv))

  
#Monitor battery
def monitor_battery():
  #print("\n MONITOR BATTERY")
  c21 =Label(root,text="MONITOR BATTERY :",font=("Arial bold", 10),anchor =CENTER)
  c21.place(x=40,y=620)
  battery_info = psutil.sensors_battery()
  battery = " Battery Percent : {}".format(battery_info.percent)
  #print(" Battery Percent : {}".format(battery_info.percent))
  secs_left =" Seconds Left : {}".format(battery_info.secsleft)
  #print(" Seconds Left : {}".format(battery_info.secsleft))
  c22 = Label(root,text=battery,font=("Arial", 10),anchor =CENTER)
  c22.place(x=190,y=620)
  c23 = Label(root,text=battery,font=("Arial", 10),anchor =CENTER)
  c23.place(x=190,y=640)
  #print(battery)
  #print(secs_left)
  with open(file1, "a") as filec:
    filec.write("\n\n MONITOR BATTERY\n")
    filec.write(" Battery Percent : {}".format(battery_info.percent))
    filec.write("\n Seconds Left : {}".format(battery_info.secsleft))

def cpu_health():
  with open(file1, "a") as filec:
    filec.write("\n\n\n\nCurrent date and time = %s\n" % e)
    filec.write("Today's date:  = %s/%s/%s\n" % (e.day, e.month, e.year))
    filec.write("The time is now: = %s:%s:%s\n" % (e.hour, e.minute, e.second))
    filec.write("==========CPU/PC HEALTH MONITORING  =============\n")
  monitor_cpu_times()
  monitor_cpu_util()
  monitor_cpu_cores()
  monitor_cpu_freq()
  monitor_ram()
  #monitor_disk()
  monitor_disk_usage()
  monitor_network()
  monitor_battery()
#------------------------------------------------------------------------------------
import speedtest
import datetime
import time
s = speedtest.Speedtest()


def internet():
  '''#img.place(x=60, y=140)
  box1.pack(
    ipadx=10,
    ipady=100
  )'''
  i1 =Label(root,text="INTERNET MONITORING STATISTICS:",font=("Arial Bold", 12),anchor =CENTER)
  i1.place(x=70,y=670)
  i2 =Label(root,text="Loading....:",font=("Arial", 10),anchor =CENTER)
  i2.place(x=140,y=690)
  #print("\n\n\n================INTERNET MONITORING===============")
  time_now = datetime.datetime.now().strftime("%H:%M:%S")
  downspeed = round((round(s.download()) / 1048576), 2)
  upspeed = round((round(s.upload()) / 1048576), 2)
  i3 =Label(root,text=f"time: {time_now}\ndownspeed: {downspeed} Mb/s\nupspeed: {upspeed} Mb/s ",font=("Arial", 10),anchor =CENTER)
  i3.place(x=140,y=690)
  with open(file2, "a") as filen:
    filen.write("\n================INTERNET MONITORING===============\n")
    filen.write(f"time: {time_now}\ndownspeed: {downspeed} Mb/s\nupspeed: {upspeed} Mb/s\n\n\n")
  #print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
  # 60 seconds sleep
  time.sleep(5)



#cpu_health()
#internet()
#network()
#-------------------------task manager-------------------------------------------------------------------------------------------
import subprocess
def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects
def process():
    print("\n\n=======================PROCESS MONITORING==========================")
    print("\n\n*** Iterate over all running process and print process ID & Name ***\n")
    print ("Current date and time = %s" % e)
    with open(file3, "a") as filep:
        filep.write("=======================PROCESS MONITORING==========================")
        filep.write("\n\n*** Iterate over all running process and print process ID & Name ***\n")
        filep.write("Current date and time = %s\n" % e)
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            #print(processName , ' ::: ', processID)
            print(str(processName)+' ::: '+ str(processID)+"\n")
            with open(file3, "a") as filep:
                filep.write(str(processName)+' ::: '+ str(processID)+"\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print('\n\n*** Create a list of all running processes ***')
    with open(file3, "a") as filep:
        filep.write('\n\n*** Create a list of all running processes ***\n')
    listOfProcessNames = list()
    # Iterate over all running processes
    for proc in psutil.process_iter():
       # Get process detail as dictionary
       pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
       # Append dict of process detail in list
       listOfProcessNames.append(pInfoDict)
    # Iterate over the list of dictionary and print each elem
    for elem in listOfProcessNames:
        print(elem)
        with open(file3, "a") as filep:
            filep.write(str(elem)+"\n")
    print('\n\n*** Top 5 process with highest memory usage ***')
    with open(file3, "a") as filep:
        filep.write('\n\n*** Top 5 process with highest memory usage ***\n')
    listOfRunningProcess = getListOfProcessSortedByMemory()
    for elem in listOfRunningProcess[:5] :
        print(elem)
        with open(file3, "a") as filep:
            filep.write(str(elem)+"\n")

def user():
    user_list = psutil.users()
    print("\n\n=========================USER DETAILS========================\n")
    print ("Current date and time = %s" % e)
    print("Users associated with this System are :")
    with open(file3, "a") as filep:
        filep.write("\n\n=========================USER DETAILS========================\n")
        filep.write("Current date and time = %s" % e)
        filep.write("\nUsers associated with this System are :\n")
    for user in user_list:
        username = user.name
        print(username)
        with open(file3, "a") as filep:
            filep.write(username)

import win32con
import win32service

def services():
    print("\n\n=====================SERVICE MONITORING==========================\n")
    print("Listing all services below:\n")
    with open(file3, "a") as filep:
            filep.write("\n\n=====================SERVICE MONITORING==========================\n")
            filep.write("Listing all services below:\n")

    resume = 0
    accessSCM = win32con.GENERIC_READ
    accessSrv = win32service.SC_MANAGER_ALL_ACCESS

    #Open Service Control Manager
    hscm = win32service.OpenSCManager(None, None, accessSCM)

    #Enumerate Service Control Manager DB
    typeFilter = win32service.SERVICE_WIN32
    stateFilter = win32service.SERVICE_STATE_ALL

    statuses = win32service.EnumServicesStatus(hscm, typeFilter, stateFilter)

    for (short_name, desc, status) in statuses:
        print(short_name, desc, status)
        with open(file3, "a") as filep:
            filep.write(str(short_name)+str(desc)+str(status)+"\n")




def taskmanager():
  process()
  user()
  services()
  


#-----------------------------------------------------------------------------------------------------------------------------------
lbl = Label(root, text="SN Monitoring Tool", font=("Arial Bold", 30), justify = 'center',foreground="brown",bg='white')
lbl.place(x=85,y=8)

lbx = Label(root, text="Developed by: Sudhanshu Nerkar", font=("Cascadia Code", 13), justify = 'center',foreground="purple",bg='white')
lbx.place(x=120,y=57)

button1 = tk.Button(text='Network Monitoring',command=threading.Thread(target=network).start,bg='#f5e1c9')
button1.place(x=20,y=93)

button2 = tk.Button(text='PC health monitoring',command=threading.Thread(target=cpu_health).start,bg='#f5e1c9')
button2.place(x=150,y=93)

button3 = tk.Button(text='Internet Monitoring',command=threading.Thread(target=internet).start,bg='#f5e1c9')
button3.place(x=280,y=93)

button4 = tk.Button(text='Task Manager details',command=threading.Thread(target=taskmanager).start,bg='#f5e1c9')
button4.place(x=410,y=93)


root.mainloop()
