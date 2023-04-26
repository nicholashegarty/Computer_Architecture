##Check Prime and Pool Processing functions from BrightSpace, removed the print statements from these funcs as they crowded the terminal
##Edited the main function to created a list of ints, and used this list of ints to create ranges for processing
##Tested each data set with 1,2,4,8,16 cores and copied results from terminal
##Works independently of any other files
import time
import math
import multiprocessing
from multiprocessing import Pool


# A naive function for check prime numbers
def check_prime(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                #print(num, "is not a prime number")
                #print(i, "times", num//i, "is", num)
                #print("Time:", int(time.time()-t1))
                break
        else:
            #print(num, "is a prime number")
            #print("Time:", time.time()-t1)
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res

# A function for timing a job that uses a pool of processes.
#  f is a function that takes a single argument
#  data is an array of arguments on which f will be mapped
#  pool_size is the number of processes in the pool.
def pool_process(f, data, pool_size):
    tp1 = time.time()
    pool = Pool(pool_size) # initialize the Pool.
    result = pool.map(f, data)       # map f to the data using the Pool of processes to do the work
    pool.close() # No more processes
    pool.join()  # Wait for the pool processing to complete.
    #print("Results", result)
    print("Overall Time:", int(time.time()-tp1))

##alternative task to test CPU
def fact(n): 
    return(math.factorial(n))  


if __name__ == '__main__':
    list = []
    
      ##alternative processing task, finding factorial using math library function
    for i in range(1,11):
        list.append(i*2500)

    for value in list:
        data_range = range(value)
        print("Data range for factorial is equal to " + str(value))
        print("1 core:", end = " ")
        pool_process(fact, data_range, 1)
        print("2 core:", end = " ")
        pool_process(fact, data_range, 2)
        print("4 core:", end = " ")
        pool_process(fact, data_range, 4)
        print("8 core:", end = " ")
        pool_process(fact, data_range, 8)
        print("16 core:", end = " ")
        pool_process(fact, data_range, 16)

    list = []
    for i in range(1,11):
        list.append(i*25000)
    for value in list:
        data_range = range(value)
        print("Data range for checkprime is equal to " + str(value))
        print("1 core:", end = " ")
        pool_process(check_prime, data_range, 1)
        print("2 core:", end = " ")
        pool_process(check_prime, data_range, 2)
        print("4 core:", end = " ")
        pool_process(check_prime, data_range, 4)
        print("8 core:", end = " ")
        pool_process(check_prime, data_range, 8)
        print("16 core:", end = " ")
        pool_process(check_prime, data_range, 16)

  
        
