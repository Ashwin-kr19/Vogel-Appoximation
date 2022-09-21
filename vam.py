# Vogel's Approximation Method Calculator

# This program computes the Initial Basic Feasible Solution to a given
# transportation problem using VAM method.


#importing the necessary libraries
import numpy as np



def check_s_d(s, d):
    for i in s:
        if i != 0:
            return 1
    for i in d:
        if i != 0:
            return 1
    return 0

#function to implement VAM
def vam(r, c, s, d, cc, a, maxi):
    
    while check_s_d(s, d):
        dc = []
        dr = []
   
        if r != 1:
            for i in range(c):
                l = []
                for j in range(r):
                    l.append(cc[j][i])
                m1 = min(l)
                l.remove(m1)
                m2 = min(l)
                dr.append(m2-m1)
   
        if c != 1:
            for i in range(r):
                l = []
                for j in range(c):
                    l.append(cc[i][j])
                m1 = min(l)
                l.remove(m1)
                m2 = min(l)
                dc.append(m2-m1)
   
        if r == 1:
            for i in range(c):
                dr = [0]
            for i in range(r):
                if cc[i] == cc[0]:
                    z = i
            for i in range(c):
                a[z][i] = d[i]
        if c == 1:
            for i in range(r):
                dc = [0]
            for i in range(c):
                if cc[0][i] != cc[i]:
                    break
                z = i
            for i in range(r):
                a[i][z] = s[i]
   
        if len(dc) == 0 or len(dr) == 0:
            break
        q1 = max(dc)
        q2 = max(dr)
        m = max(q1, q2)
   
        w = 0
        if m in dc:
            w = 1
        else:
            w = 2
   
        if w == 1:
            for i in range(r):
                if m == dc[i]:
                    index = i
   
            k = 0
            mi = cc[index][0]
            for i in range(c):
                if mi > cc[index][i]:
                    mi = cc[index][i]
                    k = i
   
            a[index][k] = min(s[index], d[k])
            s[index] -= a[index][k]
            d[k] -= a[index][k]
   
            if s[index] == 0:
                for i in range(c):
                    cc[index][i] = maxi
                #del cc[index]
            elif d[k] == 0:
                for i in range(r):
                    cc[i][k] = maxi
                    #del cc[i][k]
   
        if w == 2:
            for i in range(c):
                if m == dr[i]:
                    index = i
   
            k = 0
            mi = cc[0][index]
            for i in range(r):
                if mi > cc[i][index]:
                    mi = cc[i][index]
                    k = i
   
            a[k][index] = min(s[k], d[index])
            s[k] -= a[k][index]
            d[index] -= a[k][index]
   
            if s[k] == 0:
                for i in range(c):
                    cc[k][i] = maxi
                #del cc[k]
            elif d[index] == 0:
                for i in range(r):
                    cc[i][index] = maxi
   
        r = len(cc)
        if r == 0:
            break
        c = len(cc[0])
   
        #print("dc = ", dc)
        #print("dr = ", dr)
        #print("\ns  = ", s)
        #print("d  = ", d)
        #print("\ncc = ", cc)
        #print("\na  = ", a)



#start of main function
def main():

    print("\n\n\t\t\tVogel's Approximation Method Calculator\n\n")

    r = int(input("\n\nEnter the Number of Rows     : "))
    c = int(input("Enter the Number of Columns  : "))

    cc = []
    print("\nEnter the Cost Matrix Elements : \n")
    for i in range(r):
        temp=[]
        for j in range(c):
            temp.append(int(input()))
        cc.append(temp)   

    s=[]
    d=[]
    print("\nEnter the Supply Values: \n")
    for i in range(r):
        s.append(int(input()))
    print("\nEnter the Demand Values: \n")
    for i in range(c):
        d.append(int(input()))

    if sum(s) != sum(d):
        print("\nGiven Transportation Problem is Unbalanced!\n")
        if sum(s) < sum(d):
            cc = np.append(cc, [np.zeros(len(cc[0]))], axis=0)
            s = np.append(s, [sum(d)-sum(s)], axis=0)

        elif sum(d) < sum(s):
            for i in range(len(cc)):
                cc[i].append(0)
            d = np.append(d, [sum(d)-sum(s)], axis=0)


    # a = allocation matrix
    a = np.zeros((r, c))
    copyocopy = np.zeros((r, c))

    for i in range(r):
        for j in range(c):
            copyocopy[i][j] = cc[i][j]



    maxi = cc[0][0]
    for i in range(r):
        for j in range(c):
            if maxi < cc[i][j]:
                maxi = cc[i][j]
    maxi += 1

    print("\n\nThe Given Cost Matrix is : \n", copyocopy)
    print("\nSupply Matrix : ", s)
    print("\nDemand Matrix   : ", d)


    #print("\ns  = ", s)
    #print("d  = ", d)
    #print("\ncc = ", cc)
    #print("\na  = ", a)


    vam(r, c, s, d, cc, a, maxi)

    c_vam = 0
    for i in range(r):
        for j in range(c):
            c_vam += a[i][j]*copyocopy[i][j]

    print("\n\nThe Final Allocation Matrix is : \n", a)
    print("\nThe Cost of Given Transportation Problem is : ", c_vam)


main()    

