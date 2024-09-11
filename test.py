import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Hi All!! Welcome")
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
fig, ax = plt.subplots()
ax.plot(xpoints, ypoints)
st.pyplot(fig)
st.code("print(x)")
st.image("img/s.jpg")
st.text("Download GTA VI for free!")
st.download_button("Download GTA VI")
st.warning("Your PC has been hacked!")