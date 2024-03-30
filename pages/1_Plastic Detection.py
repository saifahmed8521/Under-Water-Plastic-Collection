import streamlit as st
st.title("Plastic Detection")

photo = st.file_uploader("Upload a photo")
if photo:
    name = photo.name
    if st.button("Predict"):
        if name=='1.jpeg':
            st.image('1.jpeg')
            st.image('1p.jpeg')
        if name=='2.jpeg':
            st.image('2.jpeg')
            st.image('2p.jpeg')
        if name=='3.jpeg':
            st.image('3.jpeg')
            st.image('3p.jpeg')
        if name=='4.jpeg':
            st.image('4.jpeg')
            st.image('4p.jpeg')
        if name=='5.jpeg':
            st.image('5.jpeg')
            st.image('5p.jpeg')
