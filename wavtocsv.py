import wave
import struct
import csv
tltl=lambda datos: datos[0]
sonido=wave.open('Yesterdays.wav','rb')

fra=sonido.readframes(sonido.getnframes())

un=struct.iter_unpack('b',fra)

sound=tuple(map(tltl,un))
sonido.close()

with open('sonido.csv','w',newline='') as csvfile:
    escribir=csv.writer(csvfile)
    escribir.writerow(['Song'])
    for i in sound:
        escribir.writerow([str(i)])
