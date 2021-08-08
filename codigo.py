import numpy as np

# Dados

x0 = -49.26612219
y0 = -25.41003028
z0 = 8.625381315


# Pontos Irradiados

x1 = -49.26657650
y1 = -25.41024690
h1 = 31.02323878
d01 = 36.160


x2 = -49.26643000
y2 = -25.40963340
h2 = 31.01075255
d02 = 58.140


x3 = -49.26651300
y3 = -25.40998200
h3 = 23.76086841
d03 = 42.990

x4 = -49.26649390
y4 = -25.40989230
h4 = 23.81259576
d04 = 42.390

# Azimutes das Irradiações


dx1 = x1 - x0
dx2 = x2 - x0
dx3 = x3 - x0
dx4 = x4 - x0

dy1 = y1 - y0
dy2 = y2 - y0
dy3 = y3 - y0
dy4 = y4 - y0


A1 = np.arctan(dx1/dy1) + np.radians(180)# 3o Quadrante
A2 = np.radians(360) - np.arctan(dx2/dy2) # 4o Quadrante
A3 = np.radians(360) - np.arctan(dx3/dy3) # 4o Quadrante
A4 = np.radians(360) - np.arctan(dx4/dy4) # 4o Quadrante



# Precisão do Desnível

def gms (x):
    g = int(x)
    m = int((x-g)*60)
    s = (x-g-m/60)*3600
    
    return '%s°%s\'%s"' %(abs(g), abs(m), round(abs(s),3))

prec = 6*np.sqrt(0.757) #Precisão do Desnível
print('Precisão do Desnível: ',round(prec,3),'mm')


aux1 = (np.cos(np.degrees(30)))**2
aux2 = (-757000*np.sin(np.degrees(30)))**2


prec_di = np.sqrt(prec**2/2/aux1)
prec_z = np.sqrt(prec**2/2/aux2)

print('Precisão da Componente Disância inclinada: ', round(prec_di,3),'mm') #Precisão da componente Distância inclinada
print('Precisão da componente ângulo Zenital; ', gms(np.degrees(prec_z))) #Precisão da componente ângulo Zenital

#x1 = x0 + di.sen(az)
#y1 = y0 + di.cos(az)

# Precisões das componentes horizontais

xt1 = -49.26672419 #rn
xt2 = -49.26631827
xt3 = -49.26606975
xt4 = -49.26591281
xt5 = -49.2658014
xt6 = -49.26579638
xt7 = -49.26590672
xt8 = -49.26612219 #estacao

dxt1 = xt2 - xt1
dxt2 = xt3 - xt2
dxt3 = xt4 - xt3
dxt4 = xt5 - xt4
dxt5 = xt6 - xt5
dxt6 = xt7 - xt6
dxt7 = xt8 - xt7


yt1 = -25.41674109 #rn
yt2 = -25.41577104
yt3 = -25.414787
yt4 = -25.41373362
yt5 = -25.41265343
yt6 = -25.41160137
yt7 = -25.4106014
yt8 = -25.41003028 #estacao

dyt1 = yt2 - yt1
dyt2 = yt3 - yt2
dyt3 = yt4 - yt3
dyt4 = yt5 - yt4
dyt5 = yt6 - yt5
dyt6 = yt7 - yt6
dyt7 = yt8 - yt7

d12 = 113.65
d23 = 110.12
d34 = 118.85
d45 = 120.95
d56 = 115.69
d67 = 112.47
d78 = 67.64


Ae1 = np.arctan(dxt1/dyt1)
Ae2 = np.arctan(dxt2/dyt2)
Ae3 = np.arctan(dxt3/dyt3)
Ae4 = np.arctan(dxt4/dyt4)
Ae5 = np.arctan(dxt5/dyt5)
Ae6 = np.radians(360) - np.arctan(dxt6/dyt6)
Ae7 = np.radians(360) - np.arctan(dxt7/dyt7)

prec_a = np.radians(1.5/3600)
prec_m = 1 + 1.5/1000000


prec_x2 = np.sqrt((np.cos(Ae1))**2 * prec_m**2 + (-d12 * np.sin(Ae1))**2 * prec_a**2)
prec_x3 = np.sqrt(prec_x2 + (np.cos(Ae2))**2 * prec_m**2 + (-d23 * np.sin(Ae2))**2 * prec_a**2)
prec_x4 = np.sqrt(prec_x3 + (np.cos(Ae3))**2 * prec_m**2 + (-d34 * np.sin(Ae3))**2 * prec_a**2)
prec_x5 = np.sqrt(prec_x4 + (np.cos(Ae4))**2 * prec_m**2 + (-d45 * np.sin(Ae4))**2 * prec_a**2)
prec_x6 = np.sqrt(prec_x5 + (np.cos(Ae5))**2 * prec_m**2 + (-d56 * np.sin(Ae5))**2 * prec_a**2)
prec_x7 = np.sqrt(prec_x6 + (np.cos(Ae6))**2 * prec_m**2 + (-d67 * np.sin(Ae6))**2 * prec_a**2)
prec_x8 = np.sqrt(prec_x7 + (np.cos(Ae7))**2 * prec_m**2 + (-d78 * np.sin(Ae7))**2 * prec_a**2) #final

print('Precisão da componente X na estação: ',round(prec_x8,3),'mm')

prec_y2 = np.sqrt((np.cos(Ae1))**2 * prec_m**2 + (-d12 * np.sin(Ae1))**2 * prec_a**2)
prec_y3 = np.sqrt(prec_x3 + (np.cos(Ae2))**2 * prec_m**2 + (-d23 * np.sin(Ae2))**2 * prec_a**2)
prec_y4 = np.sqrt(prec_x4 + (np.cos(Ae3))**2 * prec_m**2 + (-d34 * np.sin(Ae3))**2 * prec_a**2)
prec_y5 = np.sqrt(prec_x5 + (np.cos(Ae4))**2 * prec_m**2 + (-d45 * np.sin(Ae4))**2 * prec_a**2)
prec_y6 = np.sqrt(prec_x6 + (np.cos(Ae5))**2 * prec_m**2 + (-d56 * np.sin(Ae5))**2 * prec_a**2)
prec_y7 = np.sqrt(prec_x7 + (np.cos(Ae6))**2 * prec_m**2 + (-d67 * np.sin(Ae6))**2 * prec_a**2)
prec_y8 = np.sqrt(prec_x8 + (np.cos(Ae7))**2 * prec_m**2 + (-d78 * np.sin(Ae7))**2 * prec_a**2) #final

print('Precisão da componente Y na estação: ',round(prec_y8,3),'mm')

#Coordenada X


# estaçao isenta de erro

prec_x1 = prec_x8 + np.sqrt((np.cos(A1))**2 * prec_m**2 + (np.sin(A1))**2 * prec_a**2)
prec_x2 = prec_x8 + np.sqrt((np.cos(A2))**2 * prec_m**2 + (np.sin(A2))**2 * prec_a**2)
prec_x3 = prec_x8 + np.sqrt((np.cos(A3))**2 * prec_m**2 + (np.sin(A3))**2 * prec_a**2)
prec_x4 = prec_x8 + np.sqrt((np.cos(A4))**2 * prec_m**2 + (np.sin(A4))**2 * prec_a**2)

prec_y1 = prec_y8 + np.sqrt((-np.sin(A1))**2 * prec_m**2 + (np.cos(A1))**2 * prec_a**2)
prec_y2 = prec_y8 + np.sqrt((-np.sin(A2))**2 * prec_m**2 + (np.cos(A2))**2 * prec_a**2)
prec_y3 = prec_y8 + np.sqrt((-np.sin(A3))**2 * prec_m**2 + (np.cos(A3))**2 * prec_a**2)
prec_y4 = prec_y8 + np.sqrt((-np.sin(A4))**2 * prec_m**2 + (np.cos(A4))**2 * prec_a**2)


print('Precisão Aproximada de x1: ', round(prec_x1,3), 'mm')
print('Precisão Aproximada de x2: ', round(prec_x2,3), 'mm')
print('Precisão Aproximada de x3: ', round(prec_x3,3), 'mm')
print('Precisão Aproximada de x4: ', round(prec_x4,3), 'mm')

print('Precisão Aproximada de y1: ', round(prec_y1,3), 'mm')
print('Precisão Aproximada de y2: ', round(prec_y2,3), 'mm')
print('Precisão Aproximada de y3: ', round(prec_y3,3), 'mm')
print('Precisão Aproximada de y4: ', round(prec_y4,3), 'mm')