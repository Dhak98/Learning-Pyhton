#Bubble Sort Algorithm
def bub_sort(our_list):
    for i in range(len(our_list)):
        for j in range (len(our_list)-1):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                print (our_list[j],",",our_list[j+1])

our_list = [23,98,1,6,47,69,11]

bub_sort(our_list)
print(our_list)