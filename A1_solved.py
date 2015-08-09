
# coding: utf-8

# In[142]:

def friends_req(smax, s_i):
    min_friends = 0
    n = 0
    aud_list = [int(i) for i in s_i]
    for i in range(int(smax)+1):
        if min_friends < i and n < i:
            min_friends = i - n
        n += aud_list[i]        
    return min_friends
input_file = open("A-small-attempt3.in", "r")
n = int(input_file.readline())
for line in range(n):
    inp_list = (input_file.readline()).split()
    no_of_friends = friends_req(inp_list[0], inp_list[1])
    #print inp_list
    print "Case #"+str(line+1)+": "+str(no_of_friends)


