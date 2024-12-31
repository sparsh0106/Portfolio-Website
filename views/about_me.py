import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()



col1, col2 = st.columns(2, gap = 'small', vertical_alignment='center')
with col1:
    st.image("./assets/11zon_cropped.png")
with col2:
    st.title("Sparsh Agarwal", anchor = False)
    st.write("A 2nd year engineering student at Thapar Insitute of Engineering and Technology.")

    if st.button("✉️ Contact Me"):
        show_contact_form()

st.write("\n")
st.subheader("**About Me**")
st.write("""
        Hi, I'm Sparsh, a sophomore student studying Robotics & AI Engineering at [Your College Name]. I’m passionate about solving complex problems through technology, particularly in robotics, AI, and automation.

        I have a strong foundation in Python and enjoy working on hands-on projects, from machine learning algorithms to building robotic systems. Currently, I’m exploring autonomous systems and AI-human collaboration.

        I’m always eager to learn and collaborate on innovative projects, and I’m excited to contribute to the future of robotics and AI.

    
        """)

st.write("\n")
st.subheader("**Technical Skills**")
st.write("""
        ► **Robotics**: Programming and controlling robotic systems using Python.\n
        ► **Machine Learning**: Working with various machine learning algorithms and models.\n
        ► **Data Analysis**: Proficient in using **Pandas** and **NumPy** for data manipulation and analysis.\n
        ► **Web Development**: Basic knowledge of HTML and CSS for building simple websites.\n
        ► **Embedded Systems**: Experienced in **Arduino programming** for hardware and robotics projects.\n
        ► **Data Structures**: Understanding of C++ for implementing and working with various data structures.\n
        ► **CAD Modeling and Simulations**: Creating detailed CAD models and running simulations for design validation and prototyping.\n
        ► **Game design**: Designing the maps for games using **Unity game engine**.\n
        """)

st.write("\n")
st.subheader("**Technical Experience**")
st.write("""
        ► Built machine learning models for predictions, including multiple linear regression, logistic regression, XGBoost, and KNN.\n
        ► Designed and developed a buggy project using Arduino Uno R3, integrating robotics and embedded systems.\n
        ► Leveraged OpenAI APIs to create a custom AI chatbot with a web-based user interface, demonstrating full-stack AI integration.\n
        ► Developed a custom Discord bot from scratch to enhance server functionalities and automate tasks.\n
        ► Created and simulated various mechanisms using CAD software SolidWorks, followed by 3D printing the models for prototyping and testing.\n
        ► Designed and developed a Python game using Tkinter and Pygame, showcasing creativity and programming skills.\n
        """)