import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()



# Hero section
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Vrudish Waghmare", anchor=False)
    st.write(
        "Machine Learning Enthusiast | Data Science | Deep Learning"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# About section
st.write("\n")
st.subheader("About Me", anchor=False)
st.write(
    """
I am an MCA student passionate about Machine Learning and Deep Learning.
I enjoy building real-world AI solutions and deploying them as interactive applications.

Recently, I built a Food Image Classification system using TensorFlow and deployed it using Streamlit.
    """
, unsafe_allow_html=True)

st.divider()

# Skills section
st.write("\n")
st.subheader("Skills", anchor=False)
st.write("Python | TensorFlow | Scikit-learn | SQL | Streamlit | Flask | Git ")

st.divider()

# Projects section
st.write("\n")
st.subheader("Projects", anchor=False)
st.write(
    """
<h5>🍔 Food Vision Big - Food Image Classification</h5>

- Built a deep learning model using TensorFlow to classify food images into 101 categories.

- Achieved 80% accuracy using transfer learning (EfficientNet) and fine-tuning.

- Deployed using Streamlit with real-time image upload and prediction.

- Tech Stack: TensorFlow, Streamlit, NumPy, Pillow, Hugging Face
"""
, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🔗 GitHub", "https://github.com/vrudish-waghmare/food-vision-big")

with col2:
    st.link_button("🚀 Live App", "https://food-vision-big.streamlit.app")

with col3:
    st.link_button("🤗 Model", "https://huggingface.co/vrudish-waghmare/food-vision-big-model")

st.divider()

# Experience Section
st.write("\n")
st.subheader("Experience", anchor=False)
st.write(
    """
**Associate Analyst – Deloitte**
- Worked on service request management and ticket resolution  
- Improved documentation and knowledge base systems  
- Developed strong analytical and problem-solving skills  
"""
)

st.divider()

# Certifications Section
st.write("\n")
st.subheader("Certifications", anchor=False)
st.write("""
- TensorFlow for Deep Learning Bootcamp – Zero to Mastery *(In Progress)*  
- Complete Data Science, ML, DL & NLP Bootcamp – Krish AI Technologies *(In Progress)*  
""")






