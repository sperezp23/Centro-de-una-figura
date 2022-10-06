# Centro

# %% Librerias
import math
import matplotlib.pyplot as plt
import numpy as np

# %% Puntos de un cuadrado en el primer cuadrante
# p = np.array([[0,0],[0,1],[1,1],[1,0]])

# %% Puntos de un triangulo equilatero
# p = np.array([[-1,0],[0,math.sqrt(3)],[1,0]])

# %% Puntos de un Rombo
# p = np.array([[-10,0],[0,math.sqrt(3)],[10,0],[0,-math.sqrt(3)]])

# %% Puntos de una elipse centrada en (h,k)
h = 0; k = 0 #Coordenadas del centro
a = 1; b = 1 #Radio mayor, radio menor
t =np.linspace(0,2*math.pi,1000)
p = np.transpose(np.array([(a*np.cos(t))+h,(b*np.sin(t))+k]))

# %% Puntos aleatorios
# p = np.random.rand(100, 2)

# %% Puntos de un Astroide centrado en (h,k)
# h = 0; k = 0 #Coordenadas del centro
# a = 1; b = 1 #Radio mayo, radio menor
# t =np.linspace(0,2*math.pi,1000)
# p = np.transpose(np.array([((a*np.cos(t))**3)+h,((b*np.sin(t))**3)+k]))

# %% Puntos de una Leniscata centrada en (h,k)
# h = 0; k = 0 #Coordenadas del centro
# a = 1; b = 1 #Radio mayo, radio menor
# t =np.linspace(0,2*math.pi,1000)
# p = np.transpose(np.array([(a*np.cos(t)+h),(b*np.sin(2*t))+k]))

# %% Calculo del centroide
if p.shape[1] > 2:
    p = np.linalg.transpose(p)
  
Xc = np.mean(p[:,0],dtype = np.float64) 
Yc = np.mean(p[:,1], dtype = np.float64)  

r = np.linalg.norm([Xc,Yc])
theta = math.atan2(Yc,Xc) 

# %% Grafico de la figura y el centroide
plt.figure(1)
plt.plot(p[:,0],p[:,1])
plt.plot(Xc,Yc,marker = "o")
plt.grid()

# %% Impresión de resultados
print("\nCoordenadas cartecianas\n(Xc,Yc)=",(Xc,Yc),
      "\n\nCoordenadas polares\n(Theta,R)=", (theta, r))    