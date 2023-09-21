import math,tabulate
import matplotlib.pyplot as plt
import numpy as np
dt=3600
gc=6.6743*math.pow(10,-11)
def trasformCord(x0,x1):
    if x0==0:
        return x1
    if x0>0:
        return x0+x1
    return x0-x1
class Model:
    def __init__(self,dist,sunMass,planetMass,v=0):
        self.m0=sunMass
        self.m1=planetMass
        self.sx=0
        self.sy=dist
        if v==0:
            self.vx=math.sqrt(gc*self.m1/self.sy)
        else:
            self.vx=v
        self.vy=0
        self.dsx=self.dsy=self.dvx=self.dvy=0




    def iterate(self):
        self.sx+=self.dsx
        self.sy+=self.dsy
        self.vx+=self.dvx
        self.vy+=self.dvy
        self.dist=math.sqrt(math.pow(-self.sx,2)+math.pow(-self.sy,2))
        self.g=gc*self.m1/math.pow(self.dist,2)
        self.gx=self.g*-self.sx/self.dist
        self.gy=self.g*-self.sy/self.dist
        self.vx2=self.vx+self.gx*dt/2
        self.vy2=self.vy+self.gy*dt/2
        self.dsx=self.vx2*dt
        self.dsy = self.vy2 * dt
        self.sx2=self.sx+self.vx*dt/2
        self.sy2 = self.sy + self.vy * dt / 2
        self.dist2=math.sqrt(math.pow(-self.sx2,2)+math.pow(-self.sy2,2))
        self.g2=gc*self.m1/math.pow(self.dist2,2)
        self.gx2=self.g2*-self.sx2/self.dist2
        self.gy2 = self.g2 * -self.sy2 / self.dist2
        self.dvx=self.gx2*dt
        self.dvy=self.gy2*dt






earthSunModel=Model(1.5*math.pow(10,8),1.989*math.pow(10,30),5.972*math.pow(10,24))
earthMoonModel=Model(38440000,5.972*math.pow(10,24),7.347*math.pow(10,22))
exs=[]
eys=[]
mxs=[]
mys=[]
cys=[]
cxs=[]
tab=[]
print("Earth v: "+str(earthSunModel.vx))
print("Moon v: "+str(earthMoonModel.vx))
for i in range(200):
    earthSunModel.iterate()
    exs.append(earthSunModel.sx)
    eys.append(earthSunModel.sy)
earthSunModel.sx=0
earthSunModel.sy=earthSunModel.dist
for i in range(200):
    earthMoonModel.iterate()
    mxs.append(earthSunModel.sx+earthMoonModel.sx)
    mys.append(earthSunModel.sy+earthMoonModel.sy)

plt.plot(np.array(mxs),np.array(mys),color="red")#path of moon around earth
plt.plot(np.array(exs),np.array(eys),color="blue")#path of earth around sun
plt.plot(np.array(cxs),np.array(cys),color="green")#path of moon around sun
plt.show()

