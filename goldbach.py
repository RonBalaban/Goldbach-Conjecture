#******************************************************************************
# goldbach.py
#******************************************************************************
# Name: Ron Balaban
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# None
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

def is_prime(integer):
    prime=False
    factor_count=0
    for factor in range(1,integer+1):
        if (integer%factor == 0): 
            factor_count+=1
            if factor_count ==2:        # We're only interested in if a number's factor themselves are prime(thus having 2 factors itself.)
                 prime=True
            else:                       # If they're not, then that factor isn't prime and we won't use it.
                prime=False
    return prime            

def decompose(another_integer):         # This decompose function is what we really want. It checks if some # satisfies the Goldbach Conjecture
    for a in range(2,another_integer):  # It does this by looking at a range of all of it's factors, and if it finds 2 prime factors that sum 
        b=another_integer-a             # to our input value, then that # is good.
        my_list=[]
        if is_prime(a) and is_prime(b):        
            my_list.append(a)           # These 2 terms store the 2 prime factors of our #, and once a pair is found, the loop breaks.
            my_list.append(b)
            break
    return my_list
      
for even in range(4,1001,2):            # Only want to check even numbers from 4-1000
    x=decompose(even)
    print("{0}={1}+{2}".format(even,x[0],x[1]))
    
    