# Cloud-Computing-Project

## Multi-cloud process failover:

Implementing a multi-cloud control solution for our applications makes it more robust and fault-tolerant. It assists the applications to have a seamless task.

Multi-cloud process failover is applications running out of resources such as Storage over the cloud or overutilization of processing power of cloud sever and getting redirected to another server to have its task done smoothly. 

Implementation of Multi-Cloud mechanism:

We run a process or an application firstly on a cloud. When a failover occurs due to various reasons, We dynamically redirect the entire application and its computation over to another potential cloud. By dynamically shifting the whole application, the end-user will not face any hassles in performing various tasks. This mechanism will act as an abstract to the clients.  

Predictive Mechanism:

Knowing when to shift to another potential server beforehand is also essential. We implemented a predictive mechanism to tackle this issue. For the Predictive mechanism,  We set a threshold value. The threshold value is a level below which the indication to shift to the next cloud server triggers and the shifting process commences. 

We simulated this entire project by generating faults in two resources that are common to get deprived of. The two resources are 1) Storage 2) Processor utilization. 

