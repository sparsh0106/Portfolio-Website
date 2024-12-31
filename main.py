import streamlit as st

css_file = "S:\Programming Stuff\Code _n_ Stuff\All Projects\All Projects\My Custom Portfolio Website\styles\main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
projects_page = st.Page(
    "views/projects.py",
    title="My Projects",
    icon=":material/smart_toy:",
)

extracurricular_page = st.Page(
    "views/extracurricular.py",
    title="Extracurricular Activites",
    icon=":material/sports_basketball:",
)

pg = st.navigation(pages=[about_page, projects_page, extracurricular_page])

pg.run()

st.sidebar.write("Made by Sparsh\n[5p4r584g4rw4l0106@gmail.com](mailto:5p4r584g4rw4l0106@gmail.com)")
