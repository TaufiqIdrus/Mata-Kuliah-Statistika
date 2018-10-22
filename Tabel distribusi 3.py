import math
import time

#x = [128, 63, 97,134,133,136,125,110,118,94,76,84,132,105,80,87,100,77,120,109,90,72,103,78,94,118,117,80,140,94]
x = [115,106,97,93,92,93,95,112    ,107,90,90,99,116,111,88,90    ,121,82,83,103,81,96,77,76    ,71,99,88,84,77,98,76,78    ,55,59,66,53,112,69,57,65    ,71,72,73,78,69,66,55,63    ,89,76,76,72,77,75,60,60    ,101,91,93,89,74,57,73,78    ,92,89,85,80,83,74,79,82,    53,77,73,81,82,74,79,95,    68,65,63,59,61,66,69,63,   115,90,93,86,81,76,91,124,    88,78,82,89,91,97,85,96,    86,81,74,55,73,123,98,97,   79,74,86,96,86,67,79,87,   71,70,71,73,75,79,72,60,   62,54,51,56,57,64,65,65,   133,123,103,92,95,94,98,93,    67,76,89,92,87,78,62,75,   77,97,102,81,104,85,88,93] 

n= len(x)
sturgess = 1 + (3.3 *math.log10(n))
#k = math.ceil(sturgess)
k= 5
x_min = min(x)
x_max = max (x)
R = x_max - x_min
i = math.ceil(R/k)


print (x)
print('jumlah data: ',n)
print ('i: ',i)
print ("nilai minimum: ",x_min)
print ("nilai maksimum: ",x_max)
print ('nilai R: ',R)
print ('nilai interval kelas: ',k)
print ('nilai lebar interval: ',i)
print ()

interval=[]
m=[]
f=[]
fr=[]
fk=[]



#mencari interval
for q in range(1,k+2,1):
	interval.append(x_min + (q-1) *i)

#mencari median
for q in range(0,k,1):
	m.append(interval[q]+0.5*i)
	f.append(0) #inisialisasi frekuensi

#mencari frekuensi
for p in range (0,n,1):
    for q in range (0,k,1):
        if x[p] >= interval[q] and x[p] < interval[q+1]:
        	f[q]=f[q]+1

#mencari frekuensi relatif
for q in range(0,k,1):
    fr.append (round(f[q]/n,3))

#mengisi nilai awal frekuensi ke frekuensi kumulatif
fk.append(f[0])

#mencari nilai frekuensi kumulatif
for q in range (1,k,1):
    fk.append(fk[q-1]+f[q])

#mencari mean data tidak dikelompokkan
jumlah = 0
mean=0
meanTidakDikelompokkan=0
for i in range(0,n):
	jumlah+=x[i]

mean=jumlah/n
meanTidakDikelompokkan=round(mean,3)
#mencari mean data dikelompokkan

jumlah=0
for i in range(0,k):
	jumlah+=m[i]*f[i]

meanDikelompokkan = round(jumlah/fk[k-1],3)

#mencari median data tidak dikelompokkan
medianTidakDikelompokkan = 0
index =0
x_sorted = sorted(x)

if n%2==0:
	index = int(n/2) - 1
	medianTidakDikelompokkan = (x_sorted[index]+x_sorted[index+1])/2
else:
	index = int(int(n+1)/2)
	medianTidakDikelompokkan= x_sorted[index]

#mencari median data dikelompokkan
medianDikelompokkan =0
med=int(n/2)
i=13
for p in range(0,k,1):
	
	if p == 1:
		medianDikelompokkan = interval[p] + (i*(n/2))/f[p]
	else:
		medianDikelompokkan = interval[p] + (i*((n/2) - fk[p-1]))/f[p]
	if fk[p] >=med:
		break


variansiTidakDikelompokkan = 0
jumlah = 0
for i in range (0,n):
	jumlah += (x[i]**2)

variansiTidakDikelompokkan =  round((jumlah-n*(meanTidakDikelompokkan**2))/(n-1),3)
standarDeviasiTidakDikelompokkan = round(math.sqrt(variansiTidakDikelompokkan),2)

variansiDikelompokkan = 0
jumlah = 0

for p in range (0,k):
	jumlah += f[p]*(m[p]**2)

variansiDikelompokkan = round((jumlah-fk[k-1]*(meanDikelompokkan**2))/(fk[k-1]-1),3)
standarDeviasiDikelompokkan=round(math.sqrt(variansiDikelompokkan),2)

print('interval',interval)
print('median',m)
print('frekuensi',f)
print('frekuensi relatif',fr)
print('frekuensi kumulatif',fk)
print('mean data tidak dikelompokkan ',meanTidakDikelompokkan)
print('mean data dikelompokkan ',meanDikelompokkan)
print('median data tidak dikelompokkan ',medianTidakDikelompokkan)
print('median data dikelompokkan ',round(medianDikelompokkan,3))
print('variansi data tidak dikelompokkan ',variansiTidakDikelompokkan)
print('standar deviasi tidak dikelompokkan: ',standarDeviasiTidakDikelompokkan)
print('variansi data dikelompokkan ',variansiDikelompokkan)
print('standar deviasi dikelompokkan: ',standarDeviasiDikelompokkan)

time.sleep(5000)
