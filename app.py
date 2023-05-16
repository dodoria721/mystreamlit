import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(500,2)/[50,50] + [37.76-122.4],columns=['lat','lon'])
st.map(df)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)
