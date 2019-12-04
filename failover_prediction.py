from random import randint,choice
from time import sleep
from t2nano import cloud_1
from t2micro import cloud_2
from t2small import  cloud_3
from t2medium import cloud_4
from t2large import cloud_5


'''
Threshold in CPU and Storage is level below which cloud instances get directed to other instances
we set threshold value to implement the predictive mechanism. 
'''

if __name__== "__main__":

    ''' Initially the process will start executing in t2.nano
    If the resources like the CPU Utilization and Memory 
    gets exhausted then it will predict the shortage of
    the resources which leads to the process failover and 
    it will be redirected to another cloud for the execution
    '''

    print("Enter the process memory requirement and make sure that it is in the range of 0 to 5TB")
    print("Since the metrics are in GB the range should be 0 to 5000")
    p_memory=int(input()) #memory in GB that the process will use after starting its exeution 
    p_status=100  # % of process that is remained to execute
    Failover=''

    cloud_1(p_memory,p_status,Failover,"t2.nano")
