def p(n, k):

    if ( k == 1 or n == k ):

        return (1)

    elif (k> n):

        return (0)

    elif (k==2):

        return (int (n/2))

    else:

        return (p(n-1, k-1)+p(n-k, k))



def s(n, k):

    if ( k == 1 or n == k ):

        return (1)

    else:

        return (s(n-1, k-1)+k*s(n-1, k))



while (1) :

    usr_sel=input( "P or S?: " )

    usr_n=int (input ("n: "))

    usr_k=int (input ( "k: "))

    

    if (usr_sel.lower()=='p'):

        print (p(usr_n, usr_k))

    elif ( usr_sel.lower()=='s'):

        print (s(usr_n, usr_k))

    else:

        print ( "wrong input \n " )


def division(n, k):
    if(k==1 or n==k):
        return 1
    elif(k>n):
        return 0
    else:
        return(division(n-1,k-1) + k*division(n-1,k))

#main
x = int(input("S(n,k)에서 n을 입력하시오:"))
y = int(input("S(n,k)에서 k을 입력하시오:"))

print(  "S(%d, %d) = %d"%(x,y,division(x,y))  )


