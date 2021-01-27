#!/usr/bin/env python
# coding: utf-8

# In[15]:


##################################  Answer Number 01    ######################################
def sum_of_list1(list1):
    sum=0
    for i in range(0 , len(list1)):
        sum=sum+list1[i]
    return sum
list1 = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    el = int(input()) 
  
    list1.append(el) 
print("Sum of the list1 is :",sum_of_list1(list1))
    


# In[ ]:





# In[16]:


##################################  Answer Number 02   ######################################
Dict1={
   "1" : "name1",
   "2" : "name2",
   "3" : "name3"
} 
Dict2={
   "1" : 50,
   "2" : 60,
   "3" : 70
}
Dict3={}
def get_max_key(data):
    max_value = None
    for key in data:
        if max_value is None or max_value < data[key]:
            max_value = data[key]
            max_key = key
    return max_key
def get_max_val(data):
    max_value = None
    for key in data:
        if max_value is None or max_value < data[key]:
            max_value = data[key]
            max_key = key
    return max_value
max_key=get_max_key(Dict2)
max_value=get_max_val(Dict2)
Dict3[max_key]=max_value
print(Dict3)


# In[ ]:





# In[17]:


##################################  Answer Number 03    ######################################
def max_length(arr, n): 

    count = 0 
      
   
    result = 0 
  
    for i in range(0, n): 
        if (arr[i] == 0): 
            count = 0
        else: 
             count+= 1 
        result = max(result, count)  
    return result  
  
arr = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
n = len(arr)  
  
print(max_length(arr, n)) 
        
        


# In[ ]:





# In[ ]:





# In[ ]:





      


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




