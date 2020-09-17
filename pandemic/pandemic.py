import numpy as np
import matplotlib.pyplot as plt

D = 10
N = 100
r = 1
a = np.pi*r*r
rho = N/(D*D)
lam = 0.1
v = 0.1
mu = 0.05
t = 300
P = 0.01
time = 300

S = []
I = []
R = []

i_t = 5/(D*D)
r_t = 0/(D*D)
s_t = 95/(D*D)

#print((1-(1-(i_t*lam))**a))
#print(s_t)
#print(s_t*((1-(1-(i_t*lam))**a)))

for i in range(time):
    i_T = i_t + s_t*(1-(1-(i_t*lam))**a) - mu*i_t
    r_T = r_t + mu*i_t
    s_t = rho - i_T - r_T
    I.append(i_T)
    R.append(r_T)
    S.append(s_t)
    i_t = i_T
    r_t = r_T

N_I = []
N_R = []
N_S = []
for i in range(len(I)):
	N_I.append((D*D)*I[i])
	N_R.append((D*D)*R[i])
	N_S.append((D*D)*S[i])

time_vec = np.arange(time)
plt.plot(time_vec, N_I)
plt.plot(time_vec, N_R)
plt.plot(time_vec, N_S)
plt.legend(('Infected', 'Recovered', 'Susceptible'),
           loc='center right')
plt.show()




