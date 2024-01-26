import streamlit as st
import base64
from PAGES.Image_Cropper_1 import image_cropper_page
from PAGES.Netflix_Data_Analysis_2 import netflix_analysis_page 
from PAGES.Temperatures_Dashboard_3 import temperatures_dashboard_page


# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="<Miguel Martin Oviedo> Portfolio",
    page_icon="📊",
)

# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** <Miguel Martin Oviedo>")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")

# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Miguel """, unsafe_allow_html=True)  # TODO: Add your name

# ----- Profile image file -----
profile_image_file_path = "miky.jpg"  # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)

# ----- Personal title or short description -----
current_role = "Big data & Analytics student"  # Fixed the role description

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)
st.write("##")  # Adding some space

# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am currently studying a master related to Big Data and Analytics. Despite my business-oriented background, I feel comfortable using analytical tools such as PowerBI, R-Studio, MySql, Tableau, Excel, and naturally Python, from where I am deploying my portfolio.

- 🛩️ Previous: I studied a degree in Economics at the University of Salamanca where I had the opportunity to delve into Economic Science and found it highly related to statistics and Mathematical Analysis.

- :flag-pl: During 2020-2021, I had the opportunity (with some restrictions due to COVID-19) to have an extraordinary Erasmus year in Wroclaw (Poland) where I first started enjoying being in multicultural environments, speaking in English daily (and sometimes even in Polish). It wasn't my first time having an immersive experience like that because before starting the university, I had a student exchange for 3 weeks in Antioch (Chicago) living with an American family.

- :flag-dk: By the time I finished my degree, I lived for one year abroad before deciding on my next step. So I headed to Copenhagen (Denmark), but before that, I lived some time in Malmo (Sweden), where I had the WorkAway experience, living with a very nice business couple. I had a fantastic opportunity to work for their company in a very cool position as a personal assistant for a celebrity man from the States. I learned a lot about solving daily problems, working efficiently, dealing with different people every day, taking important decisions, and achieving my targets.

- ❤️ I like doing sports, especially team sports such as football and Rugby which I played for 4 years in different teams. With my last team ADUS, we had the chance to win the university cup in Seville. I have a daily routine for the gym, but what I really enjoy doing when I have time is unleashing my imagination and cooking very special dishes from any gastronomy, but especially Spanish and Japanese. I enjoy reading and watching MasterClass courses about psychology, history, and personal growth. Due to my analytical side, playing/studying poker and deploying EV+ strategies bring out the best part of me.

- 🤖 In 2024, I am developing a business with my sister, as she works as a perfumist. We prepare a very special show called Bingo Olfativo where you can have a sensorial experience recognizing different smells, mixing with the emotion of bingo. We have already done 8 shows in Barcelona, Madrid, and Zamora, and the public recognizes our merit. Developing the business requires me financial knowledge, accountability, Excel skills, communicative skills, sales and marketing skills. Furthermore, I developed a program with Python to randomize the cardboards used during the bingo. You can find below the link to the Instagram account!

- 📫 Contact me: mmartovi@icloud.com
         
 https://www.instagram.com/elgranbingoolfativo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==

         
- 🏠 Barcelona (Spain)
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.

# Feel free to add other points like your Linkedin, Github, Social Media, etc.

if __name__ == "__main__":
    # Seleccionar la página según la elección del usuario
    page_options = {
        "Home": 0,
        "Image Cropper": 1,
        "Netflix Data Analysis": 2,
        "Temperatures Dashboard": 3
    }

    selected_page = st.sidebar.selectbox("Select a page", list(page_options.keys()))

    # Ejecutar la página seleccionada
    if selected_page == "Home":
        # La página de inicio
        pass
    elif selected_page == "Image Cropper":
        # Ejecutar la función correspondiente a la página del Image Cropper
        image_cropper_page()
    elif selected_page == "Netflix Data Analysis":
        # Ejecutar la función correspondiente a la página del Netflix Data Analysis
        netflix_analysis_page()
    elif selected_page == "Temperatures Dashboard":
        # Ejecutar la función correspondiente a la página del Temperatures Dashboard
        temperatures_dashboard_page()

