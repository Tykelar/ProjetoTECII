#Ex2
import os
import time
import random
import multiprocessing  # the module we will be using for multiprocessing

def work(Run2):

	WORKING_DIRECTORY=os.getcwd()
	os.system("python3 ex2_read_project_files.py AmberTarget_Run_"+str(Run2)+".root")
	print ("Unit of work number %d" % Run2 ) # simply print the worker's number

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
	
os.system("rm finalResults2.root")
os.system("hadd finalResults2.root results_Run_*.root")
