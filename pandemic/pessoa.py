import math
import numpy as np

class Pessoa:
    def __init__(self,i, posx, posy, objx, objy, v, t_contaminado, fixedQuarantine, Dimension,p_jump):
        # movement speed
        self.v=v
        # target position
        self.objx=objx
        self.objy=objy
        #ID and name
        self.indice=i
        self.nome="Pessoa "+str(i)
        #State: Susceptible, Infected or Retired
        self.infectado = False
        self.suscetivel = True
        self.retirado = False
        #Current position
        self.posx = posx
        self.posy=posy
        #is it fixed (in quarantine)?
        self.fixedQuarantine = fixedQuarantine
        self.D = Dimension
        self.jump = p_jump/100

        # displacement per iteration
        if self.fixedQuarantine:
            self.deltax = 0
            self.deltay = 0
        else:
            self.deltax = (self.objx - self.posx) / self.v
            self.deltay = (self.objy - self.posy) / self.v
        #time in which the person was infected
        self.i_contagio=-1
        #time that the infection lasts, recover time
        self.t_contaminado = t_contaminado


    def __str__(self):
        return self.nome+" na posica ("+str(self.posx)+", "+str(self.posy) + ")"

    def infectar(self,i):
        #infect
        self.infectado=True
        self.suscetivel=False
        self.retirado = False
        self.i_contagio=i

    def retirar(self):
        #heal/removed
        self.retirado=True
        self.suscetivel=False
        self.infectado=False

    def set_objetivo(self,objx,objy):
        #this function is used to create a new target position
        self.objx=objx
        self.objy=objy
        if self.fixedQuarantine:
            self.deltax = 0
            self.deltay=0
        else:
            self.deltax = (self.objx - self.posx) / self.v
            self.deltay = (self.objy - self.posy) / self.v
            #self.deltax = (self.objx - self.posx) + self.v
            #self.deltay = (self.objy - self.posy) + self.v


    def check_contagio(self,i):
        #this function is used to heal the person if the established infection time has passed
        if self.i_contagio>-1:
            if i-self.i_contagio>self.t_contaminado:
                self.retirar()


    def update_pos(self, n_posx, n_posy):
        #this funcion animates the movement
        if(n_posx==0 and n_posy==0):
            self.posx=self.posx+self.deltax
            self.posy=self.posy+self.deltay
        else:
            self.posx=n_posx
            self.posy=n_posy

        if abs(self.posx-self.objx)<3 and abs(self.posy-self.objy)<3:
            r = np.random.random()
            if r > self.jump: 
                jumpx = (np.random.random())*self.D
                jumpy = (np.random.random())*self.D
                self.set_objetivo(jumpx, jumpy)
            else:
                position_y = self.v*(np.random.uniform(-np.pi,np.pi))
                position_x = self.v*(np.random.uniform(-np.pi,np.pi))
                self.set_objetivo(position_x,position_y)
        if self.posx>self.D:
            self.posx=self.D
        if self.posy>self.D:
            self.posy=self.D
        if self.posx<0:
            self.posx=0
        if self.posy<0:
            self.posy=0

    def get_color(self):
        if self.infectado:
            return 'red'
        if self.suscetivel:
            return 'blue'
        if self.retirado:
            return 'gray'

    def get_pos(self):
        return (self.posx,self.posy)

    def get_dist(self,x,y):
        #this funcion calculates the distance between this person an another.
        return np.sqrt((self.posx-x)**2+(self.posy-y)**2)
