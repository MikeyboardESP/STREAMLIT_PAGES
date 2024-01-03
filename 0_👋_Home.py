import streamlit as st
import base64

    
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
    st.write("**Author:** <Your Name>")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Miguel """, unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Big data & Analytics student "  

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a studying a master related to Big Data and analytics but
          I am also developing my own business based on BINGO with smells"

- 🛩️ prev: I have studied Economics in the University of Salamanca. During this years I had the opportunity to do an erasmus in Poland and 
         by the time I finished my grade I lived for one year in Copenhaguen

- ❤️ I like running and staying helthy but what in really enjoy is cooking very special fishes from different gastronomies but the spanish kitchen is my favourite.
         I also enjoy playing card games such as Poker"

- 🤖 I am developing a business with my sister based on BINGO but including the experience of smelling and recognincing the smell of 
         food, plants, species... is a completely unknown experience for most of the assitants and the format is like a show"

- 🏂 I like cooking, doing Yoga, Mindfullnes, playing card games, ski...

- 📫 mmartovi@icloud.com and u can follow the instagram of my company: https://www.instagram.com/elgranbingoolfativo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==
- 

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.

