import streamlit as st
import base64
from ultralytics import YOLO
model = YOLO('runs/detect/train2/weights/best.pt')  # load a custom model
st.title('Why we need to clean :blue[Oceans] :')
st.markdown("We need to clean the ocean because, well, it's where all the cool sea creatures live, and we can't let them swim in a garbage dump! Plus, nobody wants to surf on a plastic wave or have their beach vacation ruined by a plastic picnic. Let's tidy up the ocean and give marine life the clean, blue playground they deserve! 🌊🧹")
st.image('cleaning-the-ocean.jpg')
# !yolo task=detect mode=predict model=/runs/detect/train2/weights/best.pt conf=0.25 source=1
results = model('1.jpg')  # predict on an image
results.show()