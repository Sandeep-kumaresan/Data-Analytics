import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Working")
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
fig, ax = plt.subplots()
ax.plot(xpoints, ypoints)
st.pyplot(fig)
st.image("/img/s.jpg")