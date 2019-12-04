from random import randint,choice
from time import sleep
from t2large import cloud_5



def cloud_4(p_memory,p_status,Failover,cloud_id):
    Treshold_memory=1000 # the minimum requirement of the memory in the cloud for the process to get executed
    treshold_CPU=80 # the minimun CPU requirement for the process to execute
    p_cpu_utilization=0 # the current CPU Utilization of the process in %
    print("Process Directed to t2.medium instance")
    print()
    sleep(1)
    print("Process is utilizing storage and CPU...")
    print()
    sleep(1)
    print("Process Failover occured ",Failover," in the cloud ",cloud_id)
    print()
    sleep(1)
    cloud_id="t2.medium"
    x=randint(0,1)
    if x==0:
        for i in range(1,41):
            p_memory=p_memory-90
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
                print("Process executed without failover in t2.medium")
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
            choice([cloud_2,cloud_3,cloud_5])(p_memory,p_status,Failover,cloud_id)
        
    if x==1:
        for i in range(1,21):
            p_cpu_utilization=p_cpu_utilization+7
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
                p_status=p_status-4
            elif p_status<=0:
                print("Process executed without failover in t2.medium")
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
            choice([cloud_2,cloud_3,cloud_5])(p_memory,p_status,Failover,cloud_id)
    