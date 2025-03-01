import streamlit as st
import numpy as np
import pandas as pd
d_s=pd.DataFrame(np.random.randint(1,120,size=(4,4)))
st.header("This is my first app")
st.write(d_s)