import math 

G = 6.67 * 10**(-11)
Me = 5.972*10**24
Re = 6371*1000

h = int(input("Orbit Height (m): \n"))

T = math.sqrt(4*math.pi**2*(h+Re)**3/(G*Me))

Vg = 2* math.pi * (Re/T)
print ("ground track: ",Vg, "m/s\n")

r = (math.asin(Re /(Re+h))* (180/math.pi ))
print("earths angular radius: ", r , "deg \n")

e_min = int(input('minimun elevation(deg): \n'))

hh = math.degrees(math.asin(math.sin(math.radians(r))*math.cos(math.radians(e_min))))
print("h: ", h, "deg\n")

ls = 2 * ( 90- e_min - hh)
print("swath width: ", ls , "\n")

rs= Re * (math.sin(math.radians(ls))/math.sin(math.radians(hh)))
print("slant range: ", rs, "m\n")

Zc = int(input("Zc:\n"))

x = 2 * (hh/Zc) * h * (math.pi/180)
print("spatial resolution: ", x,"m\n")

ymax =  ((2* rs *hh)/Zc) * (math.pi/180)
print("sample distance: ",ymax,"m\n")

Ts = ymax/Vg
print("sample time: ",Ts,"s\n")

bpp = int(input("bits per pixel: \n"))
ns = int(input("number of sensors: \n"))
nsb= int(input("number of sensor bands: \n"))
Ypixels = int(input("Ypixels: \n"))
Xpixels = int(input("Xpixels: \n"))

Dsample = Zc * bpp * ns
print("Data per Sample: ",Dsample, "bits\n")

Dr = Dsample/Ts
print("Data Rate: ",Dr, "bits/s\n")

Dsize = Xpixels * Ypixels * bpp * nsb
print("Data size of single image: ",Dsize, "\n")