import numpy as np
import matplotlib.pyplot as plt
k=np.arange(6)
u=complex(0,1)
X=np.array([1,2,3,4,2,1])
X_k=np.zeros(len(X),dtype='complex')

for i in range(len(X)):
    sum=0
    for j in range(len(X)):
        sum=sum+X[j]*np.exp((-u*2*np.pi*i*j)/len(X))
    X_k[i]=sum
plt.figure(1)
plt.title("|X(k)|")
plt.xlabel("k")
plt.ylabel("|X(k)|")
plt.stem(k,np.absolute(X_k))
plt.show() 
plt.figure(2)
plt.title("<X(k)")
plt.xlabel("k")
plt.ylabel("<X(k)")
plt.stem(k,np.angle(X_k))
plt.show()



k=np.arange(0,15)
unit1=np.ones(15)
unit2=np.array([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
h=np.zeros(15)
sum=0
for i in range(15):
    h[i]=((-0.5)**i)*unit1[i] + ((-0.5)**(i-2))*unit2[i]
h_k=np.zeros(len(h),dtype='complex')
for i in range(len(h)):
    sum=0
    for j in range(len(h)):
        sum=sum+h[j]*np.exp((-u*2*np.pi*i*j)/len(h))
    h_k[i]=sum
plt.figure(3)
plt.title("|h(k)|")
plt.xlabel("k")
plt.ylabel("|h(k)|")
plt.stem(k,np.absolute(h_k))
plt.show() 
plt.figure(4)
plt.title("<h(k)")
plt.xlabel("k")
plt.ylabel("<h(k)")
plt.stem(k,np.angle(h_k))
plt.show()




