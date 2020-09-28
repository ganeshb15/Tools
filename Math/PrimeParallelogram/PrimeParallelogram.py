import numpy as np
import Prime
import matplotlib.pyplot as plt
import streamlit as st

x = st.slider('Select a value',2,10000)
Choose = st.radio("With Prime or without",('Prime', 'Odd', 'All'))

Prime=np.array(Prime.PrimeNum(2,x))

if Choose == 'Prime':
	In=Prime	
elif Choose == 'Odd':
	In=np.arange(start=1, stop=x, step=2)
elif Choose == 'All':
	In=np.arange(start=1, stop=x, step=1)
	
Output=[]
for i in In:
	Temp = np.binary_repr(i)
	TempReverse=Temp[::-1]
	T1=int(Temp,2)
	T2=int(TempReverse,2)
	Output.append(T2-T1)

if Choose == 'Prime':
	plt.scatter(In,Output, c ="blue") 	
elif Choose == 'Odd':
	plt.scatter(In,Output, c ="red") 
elif Choose == 'All':
	plt.scatter(In,Output, c ="orange") 


st.pyplot(plt)

