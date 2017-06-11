'''
simple 2D projectile
'''
import matplotlib.pyplot as plt
import math
def plot_graph(x,y):
  plt.plot(x,y,marker='o')
  plt.xlabel("x-coordinate")
  plt.ylabel("y-coordinate")
  plt.title("simple 2d Projectile position graph")
  plt.show()
def floatrange(start,stop,jump):
  float_num=[]
  while start<stop:
    float_num.append(start)
    start=start+jump
  return float_num  

def compute(theta,u):
  g=9.8
  theta=math.radians(theta)
  t_max=((2*u*math.sin(theta))/(g))
  r=floatrange(0,t_max,0.001)
  x=[]
  y=[]
  for i in r:
    x.append((u*mathcoa(theta)*i))
    y.append((u*math.sin(theta)*i)-(0.5*g*i*i))
  plot_graph(x,y)
 if __name__=='__main__':
  u=float(input("ener the initial velocity(m/s):"))
  theta=float(input("enter the angle of projection (degree):")
