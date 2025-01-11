n,k,l,c,d,p,nl,np=map(int,input().split())
drink=k*l/nl
lemos=c*d
salt=p/np
toasts=int((min(drink,lemos,salt))//n)
print(toasts)