t=int(input("Enter no of test cases"))

for i in range (0,t):
    q,p=map(int,input("Enter quantity and price").split())
    if(q>1000):
        ori=q*p
        dis=ori*0.1
        print(ori-dis)
    else:
        print(q*p)