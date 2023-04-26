from NeuroPy2 import NeuroPy
from time import sleep 
import csv
import pandas as pd
neuroPy=NeuroPy("COM3")  
neuroPy.start()
Meditation = []
Attention=[]
BlinkStrength=[]
i = 100000
i=0
while i<600:    
    i=i+1
    print ("Meditation ", neuroPy.meditation)
    Meditation.append(neuroPy.meditation)
    print ("Attention ", neuroPy.attention)
    Attention.append(neuroPy.attention)
    print("BlinkStrength",neuroPy.blinkStrength)
    BlinkStrength.append(neuroPy.blinkStrength)
    print(i)
    sleep(0.01)

df=pd.DataFrame(Meditation, columns=['Meditation'] )
df['Attention']=Attention
df['BlinkStrength']=BlinkStrength
df.to_csv('test.csv')

print(df)
