a = map(int,raw_input().strip().split(' '))

#variables

#Current values
current_count = 0
current_start = 0

#Maximum values
max_count = 0
max_start = 0
max_end = 0

#Initial segment if starts with initial element
initial_index = 0
initial_end = 0

#Number of entries in the array .... 360/5 = 72
list_length = len(a)

for i in range(list_length):
    if(a[i]==1):
        if(i==0):
            initial_index = 1
        if(initial_index==1):
            initial_end += 1
        if(current_count==0):
            current_start = i
        current_count += 1
    elif(current_count>max_count):
        max_count = i-current_start
        max_start = current_start
        max_end = i-1
        current_count = 0
    if(a[i]==0):
        initial_index = 0
        current_count = 0

if(a[list_length-1]==1):
    if(list_length - current_start > max_count):
        max_count = list_length - current_start
        max_start = current_start
        max_end = list_length - 1

median = -1

print(list_length)
print(initial_end)
print(current_start)


if((a[0]==1 and a[list_length-1]==1) and initial_end!=list_length):
    if(initial_end+list_length-current_start > max_count):
        median = (current_start+(initial_end+list_length-current_start)/2)%list_length
else:
    median = max_start + (max_end-max_start)/2

print(median)
