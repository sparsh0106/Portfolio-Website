import streamlit as st

st.title('Extracurricular Activites')

tab1, tab2, tab3, tab4 = st.tabs(["Table Tennis", "Cycling", "Music", "Astronomy"])

with tab1:
    st.write("\n")
    st.subheader("Table Tennis")
    st.write("""
            ► Team captain in school\n
            ► 1st place in Gurugram District championships.\n
            ► 1st place (U17) and 3rd place (U19) in Inter-school championship\n
            ► 2nd place in intra-hostel championship in college\n
            ► 1st place under Veteran category in Pro Table Tennis Championship organised by IIT Madras.\n    
            """)

with tab2:
    st.write("\n")
    st.subheader("Cycling")
    st.write("""
            ► Regular cyclist, averaging 150 km/week.\n
            ► Cycled over 3100 km since June 2023.\n
            ► Completed 7 long distance rides with longest ride being 130 km long.\n
            ► Completed 1250 km in June 2023 cycling challenge.\n
            ► Completed 550 km in May 2024 cycling challenge.\n
            """)
    st.write("\n")
    st.markdown("<h4 style='margin-bottom:0;'>More Cycling Stats:</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.metric(label="No. of rides", value="104")
    st.metric(label="Long Distance Rides", value="7")
    st.metric(label="Longest Rides", value="131 km")
    st.metric(label="Fastest average", value="28 km/hr")
    st.metric(label="2023", value="1977")
    st.metric(label="2024", value="1140")

with tab3:
    st.write('\n')
    st.subheader("Music")
    st.write("""
            ► Passionate drummer, school band leader for 5 years\n
            ► 1st and 2nd place in inter-school-music competition (2021,2020)\n
            ► Composed 2 original music pieces with the band\n
            ► Special mention in inter-school band competition in 2022.\n
            """)
    st.markdown("<h4 style='margin-bottom:0;'>My Content:</h4>", unsafe_allow_html=True)
    st.write("Access my YouTube channel here - [Sparsh Agarwal Drums ♪](https://www.youtube.com/@sparshagarwaldrums428)")
    st.write("Access my Instagram handle here - [@sparsh0106](https://www.instagram.com/sparsh0106/)")
    st.video("https://youtu.be/99p9jP0_AAA")
    st.video("https://drive.google.com/uc?export=download&id=1Pw-QXxz2HQvgd2dTsPymPO3dX7jTVgrq")

with tab4:
    st.write('\n')
    st.subheader("Astronomy")
    st.write("""
            ► Astrophotography: captured constellations and galaxies\n
            ► Head of high school astronomy club, member of college astronomy club\n
            """)
    st.subheader("Astrophotos")
    st.write("These are some of my astrophotos I clicked a while ago:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write('\n')
        st.write("Photo of Andromeda Galaxy (taken on Sep 28, 2022)")
        st.image("./assets/5.jpg")

        st.write('\n')
        st.write("Random patch of sky 2 (taken on Sep 4, 2023)")
        st.image("./assets/20230409_015640.jpg")

    with col2:
        st.write('\n')
        st.write("Random patch of sky 1 (taken on Sep 4, 2023)")
        st.image("./assets/20230409_013326.jpg")

        st.write('\n')
        st.write("Orion Constellation (taken on Dec 15, 2022)")
        st.image("./assets/20221215_010940.jpg")