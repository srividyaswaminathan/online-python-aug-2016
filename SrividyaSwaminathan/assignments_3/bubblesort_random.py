#bubble sort with random numbers
import random
import time
random_num = random.sample(range(1, 10000), 100)
print random_num
for i in range(0,len(random_num)):
	for j in range(0,len(random_num)-1):
		if random_num[j]>random_num[j+1]:
			#swapping numbers
			temp = random_num[j+1]
			random_num[j+1] = random_num[j]
			random_num[j] = temp 
print "Sorted list of random numbers are:",random_num			
print "*******************************************************************************"
start_time = time.time()
print("--- Time taken for this sorting is %s seconds ---" % (time.time() - start_time))	   
