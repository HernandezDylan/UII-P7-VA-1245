import numpy as np
import matplotlib.pyplot as plt
# Hernadez Dylan NC= 1245
No_lista=[1,2,3,17,48]
Califa_ML=[20,30,80,100,90]
Califa_VA=[70,90,60,90,100]
plt.plot(No_lista,Califa_ML,label="Califa ML")
plt.plot(No_lista,Califa_ML,label="Califa VA")
plt.title(" Calificaciones Materias")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion")
plt.legend()
plt.show()