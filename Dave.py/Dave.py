import streamlit as st
import datetime

# Set page configuration
st.set_page_config(page_title="Davie's Biography", layout="wide")

# Custom CSS for background color and styling
background_css = """
<style>
    body {
        background-color: #ADD8E6; /* Light blue */
    }
    .main {
        background-color: #f8f9fa; /* Light gray for content area */
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        text-align: center;
        color: #2c3e50;
    }
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)

# Initialize session state if not already initialized
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False
if 'name' not in st.session_state:
    st.session_state.name = "Davie Z. Danao"
if 'about_me' not in st.session_state:
    st.session_state.about_me = ("Hi I'm Davie, I'm a Computer Engineering student at Surigao del Norte State University. I'm always eager to learn and grow in my academics. Outside of academics, I love playing online games along with my friends. ")
if 'mother_name' not in st.session_state:
    st.session_state.mother_name = "Estila Z. Danao"
if 'father_name' not in st.session_state:
    st.session_state.father_name = "Alex C. Danao"
if 'mother_bday' not in st.session_state:
    st.session_state.mother_bday = datetime.date(1977, 4, 1)
if 'father_bday' not in st.session_state:
    st.session_state.father_bday = datetime.date(1974, 3, 5)
if 'high_school' not in st.session_state:
    st.session_state.high_school = "Mariano Espina Memorial Central Elementary School"
if 'senior_high_school' not in st.session_state:
    st.session_state.senior_high_school = "Surigao del Norte National Highschool"
if 'college' not in st.session_state:
    st.session_state.college = "Surigao del Norte State University"
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = "- Playing Online Games\n- Watching Anime\n- Playing Chess"
if 'gender' not in st.session_state:
    st.session_state.gender = "Male"
if 'birthplace' not in st.session_state:
    st.session_state.birthplace = "Brgy. Taft, Surigao City, Surigao del Norte"
if 'current_address' not in st.session_state:
    st.session_state.current_address = "Brgy. Taft, Surigao City, Surigao del Norte"
if 'mybirthday' not in st.session_state:
    st.session_state.mybirthday = datetime.date(2005, 9, 29)  # Default birthdate (can be updated)

# Page header with image on the right
col1, col2, col3 = st.columns([3, 2, 1])
with col1:
    st.title("Davie's Biography")
    st.subheader("Welcome to my personal page!")
with col3:
    st.image(
        "https://scontent.xx.fbcdn.net/v/t1.15752-9/462564038_487220667072339_5843449267658515291_n.jpg?stp=dst-jpg_s480x480&_nc_cat=104&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeEsHS_Li13p8e8uRHWODFFgdtW3uTLaH1d21be5MtofV4rIBcvSnBZd7iMwK9LOLXcAklf6sHbay7QZZiZewAf9&_nc_ohc=lTVw7qH-94oQ7kNvgFyp95W&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QFaymm4hMcP69Ogybk3W46AYFIT3K45jebOBjQiY9jlpA&oe=676CA768",
        caption="Davie Z. Danao",
        width=150,
    )

# Tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(["Personal Info", "Parents", "Education", "Achievements"])

# Personal Info tab
with tab1:
    st.header("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Full Name", st.session_state.name)
        st.date_input("Date of Birth", st.session_state.mybirthday, key="mybirthday")
        st.text_input("Place of Birth", st.session_state.birthplace)
        st.radio("Gender", ["Male", "Female"], index=0 if st.session_state.gender == "Male" else 1, key="gender")
    with col2:
        st.text_input("Current Address", st.session_state.current_address)
        st.text_area("Hobbies", st.session_state.hobbies, height=100, key="hobbies")

# Family tab
with tab2:
    st.header("Parents Background")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Mother's Name", st.session_state.mother_name)
        st.date_input("Mother's Birthday", st.session_state.mother_bday, key="mother_bday")
    with col2:
        st.text_input("Father's Name", st.session_state.father_name)
        st.date_input("Father's Birthday", st.session_state.father_bday, key="father_bday")

# Education tab
with tab3:
    st.header("Educational Attainment")
    st.text_input("High School", st.session_state.high_school)
    st.text_input("Senior High School", st.session_state.senior_high_school)
    st.text_input("College", st.session_state.college)

# Achievements tab
with tab4:
    st.header("Achievements")
    st.text_area("Academic Achievements", "- In 2015, I won 1st place in the Division Chess competition.\n- In 2016, I achieved 2nd place in our classroom rankings.\n- In 2023, I graduated with high honors.", height=150)
    st.text_area("Gaming Achievements", "- Achieved Mythical Immortal Rank\n- Former Top 1 SDN Chou\n- Former Top 1 SDN Selena\n- Former Top 1 SDN Aldous\n- Top 3 SDN Hayabusa\n- 1st Runner Up in MLBB Tournament\n- Champion in College MSL MLBB Tournament", height=150)

# Footer
st.write("---")
st.markdown("""
<div style="text-align: center; font-size: 18px;">
    <strong>Thank you for visiting my page!</strong>
</div>
""", unsafe_allow_html=True)
