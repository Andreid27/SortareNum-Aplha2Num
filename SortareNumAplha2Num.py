def arrange(intrare):
    v=[]
    nr_cifre=0
    nr_final=0
    while(int(intrare)>0):
        intrare_c=intrare
        nr_cifre=0
        while(int(intrare_c)>0):
            nr_cifre=nr_cifre+1
            intrare_c=intrare_c/10
            #print("Nr cifre", intrare_c)
        #print (nr_cifre)
        for i in range(nr_cifre):
            v.append(intrare%10)
            intrare=int(intrare/10)
        for i in range (nr_cifre):
            for k in range (nr_cifre-i-1):
                if (v[k] < v[k + 1]):
                    value = v[k]
                    v[k] = v[k + 1]
                    v[k + 1] = value
            
        for i in range(nr_cifre):
            nr_final=nr_final*10+v[i]
        print(nr_final)



arrange(7923)

def alpha_to_num(cuvinte):
    n = len(cuvinte) #numar litere
    char_v=[] #vector de litere
    #copying the contents of the
    #string to char array
    cuvinte.lower()#cuvinete lowercase
    for i in cuvinte:
        char_v.append(i)
    for i in range(n):
        if(ord(char_v[i])!=32 and ord(char_v[i])>95 and ord(char_v[i])<123):
         print(ord(char_v[i])-96)

alpha_to_num("The sunset sets at twelve o' clock.")
