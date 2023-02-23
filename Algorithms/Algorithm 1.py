print(".....Welcome to Bubble Sort.....")
pn=int(input("Select any one of these to perform:\n1.Ascending\n2.Desecending"'\n'))
if pn == 1 :
    our_list = []

    num_ele_flist =int(input("Enter the Number of element for First List (Ascending Order): "))
    for i in range(num_ele_flist):
        fele = int(input("Enter the Elements: "))
        our_list.append(fele)
    
    print("Befor Sorting",our_list)
        
    #Bubble Sort Algorithm (Ascending Order)
    def bub_asort(our_list):
        for i in range(len(our_list)):
            for j in range (len(our_list)-1):
                if our_list[j] < our_list[j+1]:
                    our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                    print (our_list[j],",",our_list[j+1])
    
    bub_asort(our_list)
    print("After Sorting",our_list)

else:
    our_slist = []

    num_ele_slist = int(input("Enter the Number of element for Second List (Descending Order): "))

    for i in range(num_ele_slist):
        sele = int(input("Enter the Elements: "))
        our_slist.append(sele)
    
    print("Befor Sorting",our_slist)
        
    #Bubble Sort Algorithm (Desending Order)
    def bub_dsort(our_slist):
        for i in range(len(our_slist)):
            for j in range (len(our_slist)-1):
                if our_slist[j] > our_slist[j+1]:
                    our_slist[j], our_slist[j+1] = our_slist[j+1], our_slist[j]
                    print (our_slist[j],",",our_slist[j+1])
    
    bub_dsort(our_slist)
    print("After Sorting",our_slist)
    

