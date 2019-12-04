from random import randint,choice
from time import sleep
from t2micro import cloud_2
from t2small import  cloud_3
from t2medium import cloud_4
from t2large import cloud_5



def cloud_1(p_memory,p_status,Failover,cloud_id):
    p_cpu_utilization=0 # the current CPU Utilization of the process in %
    Treshold_memory=2500 # the minimum requirement of the memory in the cloud for the process to get executed
    treshold_CPU=80 # the minimun CPU requirement for the process to execute
    print("Process Directed to t2.nano instance")
    print()
    sleep(1)
    print("Process is utilizing storage and CPU...")
    print()
    sleep(1)
    x=randint(0,1)
    if x==0:
        for i in range(1,41):
            p_memory=p_memory-75
            if p_memory >= Treshold_memory and p_cpu_utilization <= treshold_CPU and p_status>0:
                print("Storage Left: ",p_memory," GB")
                print()
                sleep(1)
                CPU_Utilization=randint(1,i)
                print("CPU Utilization: ",CPU_Utilization,"%")
                print()
                sleep(1)
                print("Process that is executed ",100-p_status,"%")
                print()
                sleep(1)
                p_status=p_status-5
            elif p_status<=0:
                print("Process executed without failover in t2.nano")
                print()
                sleep(1)
                break
            else:
                break 
        if p_status>0:
            print("Process is utilizing more Storage than anticipated")
            print()
            sleep(1)
            Failover="due to over utilization of memory "
            print("Process left , which has to be executed ",p_status,"%")
            print()
            sleep(2)
            choice([cloud_2,cloud_3,cloud_4,cloud_5])(p_memory,p_status,Failover,cloud_id)
       
    if x==1:
        for i in range(1,21):
            p_cpu_utilization=p_cpu_utilization+6
            p_memory=p_memory-50
            if p_cpu_utilization <= treshold_CPU and p_memory >= Treshold_memory and p_status>0:
                print("CPU_utilization: ",p_cpu_utilization,"%")
                print()
                sleep(1)
                print("Storage Left: ",p_memory," GB")
                print()
                sleep(1)
                print("Process that is executed ",100-p_status,"%")
                print()
                sleep(1)
                p_status=p_status-5
            elif p_status<=0:
                print("Process executed without failover in t2.nano")
                print()
                sleep(1)
                break
            else:
                break
        if p_status>0:
            print("Process is utilizing more CPU than anticipated")
            print()
            sleep(1)
            Failover="due to over utilization of CPU "
            print("Process left , which has to be executed ",p_status,"%")
            print()
            sleep(2)
            choice([cloud_2,cloud_3,cloud_4,cloud_5])(p_memory,p_status,Failover,cloud_id)
   