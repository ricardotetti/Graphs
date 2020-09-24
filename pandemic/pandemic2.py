from pessoa import Pessoa
import numpy as np
import matplotlib.pyplot as plt
#Parametros

n = 500 #Número de pessoas
n_contaminados = 1 #porcentagem de contaminados
r_contagio = 2 #raio de contagio
p_contagio = 4 #probabilidade de contaminar
p_isolamento = 50 #porcentagem de pessoas isoladas
p_salto = 10 #probabilidade de saltar
t_contagio = 100 #tempo que a pessoa fica contaminada
D = 100 #Dimension
v = 1 #velocidade
inter = 1000 #tempo

contaminados = 0
pessoas = []

#creating all the individuals in random positions. Infecting some of them
for i in range(n):
    p = Pessoa(i,np.random.random()*D, np.random.random()*D,
                np.random.random()*D, np.random.random()*D,
                v, t_contagio, False, D, p_salto)


    if np.random.random()<n_contaminados/D:
        p.infectar(0)
        contaminados += 1
    if np.random.random()<p_isolamento/100:
        p.fixedQuarantine=True

    pessoas.append(p)


ct=[contaminados]
rt=[0]
t=[0]

#function excecuted frame by frame
def update(frame,rt,ct,t):
    contciclo = 0
    recuciclo = 0
    colores = []
    sizes = [8 for p in pessoas]
    for p in pessoas:
        #check how much time the person has been sick
        p.check_contagio(frame)
        #animate the movement of each person
        p.update_pos(0,0)
        if p.retirado:
            recuciclo+=1 #count the amount of recovered
        if p.infectado:
            contciclo=contciclo+1 #count the amount of infected
            #check for people around the sick individual and infect the ones within the
            # transmission radius given the probability
            for per in pessoas:
                if per.indice==p.indice or per.infectado or per.retirado:
                    pass
                else:
                    d=p.get_dist(per.posx,per.posy)
                    if d<r_contagio:
                        if np.random.random() < p_contagio / 100:
                            per.infectar(frame)
                            sizes[per.indice]=80
        colores.append(p.get_color()) #change dot color according to the person's status
    #update the plotting data
    ct.append(contciclo)
    #rt.append(recuciclo)
    t.append(frame)

    #return cvst,rvst
    return ct

k= []
k1 = []
for i in range(inter):
    k.append(update(i,rt,ct,t)) #O QUE ACONTECE AQUI É QUE A CADA INTEREÇÃO ELE ME DA O INDICE DOS QUE ESTAO INFECTADOS
                                #ISSO IMPLICA QUE POSSO A CADA INTERAÇÃO PEGAR O COMPRIMENTO DA LISTA A CADA UPDATE, E ISSO VAI
                                #TER O NUMERO DE CONTAMINADOS A CADA INTERAÇÃO.
    k1.append(k[i][i])
#for i in range(inter):
    #k1.append(k[i][i])

plt.plot(t[:inter],k1)
plt.xlabel("t")
plt.ylabel("$N_i(t)$")
#plt.ylim(0,n)
plt.xlim(0,inter+10)
#plt.savefig("p_salto_098")
plt.show()