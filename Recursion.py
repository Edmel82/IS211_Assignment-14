#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Edwards Meliton IS-211 Assignment 14

#Part I-Fibonnaci sequence

def Fibonacci(n): 
    if n==1 or n==2: 
        return 1        
    else: 

        return Fibonacci(n-1)+Fibonacci(n-2) 

x = 10
print("Fibonacci Answer for %s: %s" % (x, Fibonacci(x)))

print('\n')

#Part II-Euclid's GCD algorithm: 

def gcd_non_recursive(a, b):
    while b: # Shorthand for is False or 0
        a, b = b, a % b
    return a
        
def gcd(a, b):  
    if a == 0 : 
        return b  
    else:  
        return gcd(b%a, a)

a, b = 1071, 462

print("With Loop (Non-Recursive): %s" % (gcd_non_recursive(a, b)))
print("With If/Else (Recursive): {%s}" % gcd(a, b))


print('\n')

#Part III- String Comparison:
    
def compareTo(s1, s2):
    if s1 == s2:
        return 0
    else: 
        return len(s1) - len(s2)
    
s1 = "Nintendo"
s2 = "Sony"

print("compareTo() Example #1")
print("The quantity of games of s1 (%s): %s" % (s1, len(s1)))
print("The quantity of games of s2 (%s): %s" % (s2, len(s2)))
print(compareTo(s1, s2))

s1 = "New Jersey"
s2 = "Connecticut"
print('\n')
print("compareTo() Example #2")
print("The population of s1 (%s): %s" % (s1, len(s1)))
print("The population of s2 (%s): %s" % (s2, len(s2)))
print(compareTo(s1, s2))


# In[ ]:




