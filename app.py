import streamlit as st
import numpy as np
import cv2
from PIL import Image

# إعداد صفحة Streamlit
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>كيف سيبدو وجهك بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)
st.write("ارفع صورة لنريك التأثير
