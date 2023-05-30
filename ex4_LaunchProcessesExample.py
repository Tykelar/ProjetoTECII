#!/usr/bin/env python
import os
import time
import random
import multiprocessing  # the module we will be using for multiprocessing

def work(Run):

	WORKING_DIRECTORY=os.getcwd()
<<<<<<<< HEAD:ex1_LaunchProcessesExample.py
	os.system("python3 ex1_read_project_files.py AmberTarget_Run_"+str(Run)+".root")
========
	os.system("python3 ex4_read_project_files.py AmberTarget_Run_"+str(Run)+".root")
>>>>>>>> 0b3f5087e00e23df5dc06ff71b7afb973bcc7e40:ex4_LaunchProcessesExample.py
	print ("Unit of work number %d" % Run ) # simply print the worker's number

if __name__ == "__main__":  # Allows for the safe importing of the main module
	print("There are %d CPUs on this machine" % multiprocessing.cpu_count())
	number_processes = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(number_processes)
	total_tasks = 4
	tasks = range(total_tasks)
	results = pool.map_async(work, tasks)
	pool.close()
	pool.join()

#adicionar aqui o hadd
	
os.system("rm finalResults4.root")
os.system("hadd finalResults4.root results4_*.root")
