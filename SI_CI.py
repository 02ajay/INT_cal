def SI_CI(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
    ci =p*(1+r/100)*t
    print('The Simple Interest is', si)
    print('The Compoun Interest is', ci)