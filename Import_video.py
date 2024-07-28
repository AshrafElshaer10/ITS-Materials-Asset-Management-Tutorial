import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

video_file_01 = open(r'ITS_Materials_Manager_App (New).mp4', 'rb')
video_bytes_01 = video_file_01.read()
st.header("ITS_Materials_Application_Tutorial:", divider= 'red')
st.video(video_bytes_01)
