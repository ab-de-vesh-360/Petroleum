import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.title('Dynamic Pressure Profile')
st.sidebar.title('Inputs')

k= st.sidebar.slider('Perm(md)',min_value = 10, max_value= 200, value= 100)
mu = st.sidebar.slider('Viscosity(cp)',min_value = 10, max_value= 50, value= 15)
q = st.sidebar.slider('Flowrate(STB/day)',min_value = 100, max_value= 200, value= 200)

re = st.sidebar.number_input('Outer Radius of Reservoir(ft)', min_value=100, max_value=10000, value= 3000)
rw = st.sidebar.number_input('Wellbore Radius(ft)', min_value=1, max_value=10, value= 1)
pe = st.sidebar.number_input('Pressure of boundary of Reservoir(Psi)', min_value=100, max_value=10000, value= 4000)
B = st.sidebar.number_input('Formation Volume factor(bbl/stb)', min_value=1, max_value=2, value= 1)
h = st.sidebar.number_input('Net py thickness of Reservoir(ft)', min_value=2, max_value=500, value= 30)

r = np.linspace(rw, re, 500)
p = pe - (141.2*q*mu*B*(np.log(re/r))/k/h)
y_min = p[np.where(r==rw)]

#adding buttens
b = st.button('Show Pressure Profile')

#plotting
if b:  #tells if the button is pressed
    plt.style.use('classic')
    plt.figure(figsize=(8,6))
    fig,ax = plt.subplots()

    ax.plot(r,p)
    
    ax.grid(True)
    ax.axhline(y_min, linewidth= 3, color= 'red')
    ax.set_xlabel('radius(ft)')
    ax.set_ylabel('Prssure at radius r, (PSI)')
    ax.set_title('Pressure Profile')
    ax.set_ylim(0,5000)

    st.pyplot(fig)  #for showing the fig in app



