a=int(input('Enter a random number'))
n1=int("%s" %a)
n2=int("%s%s" %(a,a))
n3=int("%s%s%s" %(a,a,a))

print('Sum of digits:', n1+n2+n3)