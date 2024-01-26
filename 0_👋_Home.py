import streamlit as st
import base64

<<<<<<< HEAD

=======
>>>>>>> 71f85e6c8ba48ee70b4f15e98c730baf2cde4a3a
    
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
profile_image_file_path = "miky.jpg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
<<<<<<< HEAD
current_role = "Big data & Analytics Student "  
=======
current_role = "Big data & Analytics student "  
>>>>>>> 71f85e6c8ba48ee70b4f15e98c730baf2cde4a3a

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
<<<<<<< HEAD
- 🧑‍💻 I´m currrently studying a master related to Big Data & Analytics, despite of my business-oriented background I feel comfortable trying everyday 
         Analytical tools such as PowerBI, R-Studio, MySql, Tableau, Excel, and naturally Python, from where I´m deploying my portfolio ."

- 🛩️ prev: I studied a degree in Economics at the University of Salamanca where I had the opportunity to delve into Economic Science
          and I it highly related with stadistics and Mathematical Analysis.
         
 -    🇵🇱  During 2020-2021, I had the opportunity (with some retrictions due to COVID-19) to have and extraodrinary Erasmus year in Wroclaw (Poland) Where I first started 
          enjoying being in multicultural environments, speaking in English daily (and sometimes even in polish). It wasn´t my first time having an immersive experience like that 
          because before starting the university, I had a student exchange for 3 weeks in Antioch (Chicago) living with an American family.

 -    🇩🇰  By the time I finished my degree, I lived for one year abroad before deciding on my next step. So I headed to Copenhaguen (Denmark), but before that, 
         I lived some time in Malmo (Sweeden), where I had the WorkAway experience, living with a very nice business couple. I had a fantastic opportunity to work for their company 
         in a very cool position as personal assitant for a celebrity man from the States. I learned a lot about solving daily problems, working efficiently, 
         dealing with different people every day, taking important decisions and achiving my targets.

- ❤️ I like doing sports, specially team sports such as football and Rugby which I played for 4 years in different teams. With my last team ADUS, we had the chance to win the univeristy cup in Seville.
          I have a daily routine for the gym, but what I really enjoy doing when I have time is unleashing my imagination and cooking very special dishes from any gastronomy, but specially Spanish and Japanese.
          I enjoy reading and watching MasterClass courses about psychology, history and personal growth. Due my analytical side playing/ studying poker and deploying EV+ strategies bring out the best part of me

- 🤖 in 2024, I´m developing a business with my sister, as she works as perfumist, we prepare a very special show called Bingo Olfativo where you can have a sensorial experience recognicing different 
         smells, mixing with the emotion of bingo, we have already done 8 shows in barcelona, Madrid and Zamora and the public recognices our merit.
         developing the business requires me financial knwoledge, acocuntability, excel skills, communicative skills, sales and marketing skills. 
         Furthermore, I developed a program with python to randomize the cardboards used during the bingo.
         You can find below the link to the instagram account!  "

-   ¿What am I looking for? I want to focus all my energy and potential in Big data, keep growing and learning about the science of the future, Connecting the business with Data Insights.
         Following a company that I feel ethical aligned with and having the capability to bring out the best part of me. 
         As I consider myself a very Outgoing person and easy to connect with I want to be the bridge between IT and business and become a problem-solver. 

-   ¿Where would i like to work? 
         *Copenahguen 
         *Barcelona
         *Madrid 
         *working in a different city in Spain or Europe works also for me 

- 📫 contact me: mmartovi@icloud.com 
        
 https://www.instagram.com/elgranbingoolfativo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==
         

         
- 🏠  Barcelona (Spain)
=======
- 🧑‍💻 I am a studying a master related to Big Data and analytics but
          I am also developing my own business based on BINGO with smells."

- 🛩️ prev: I have studied Economics in the University of Salamanca. On the fourth year of my grade I had the opportunity to do an erasmus in Poland and 
         by the time I finished, I lived for one year in Copenhaguen.

- ❤️ I like running and staying helthy but what in really enjoy is cooking very special fishes from different gastronomies but the spanish kitchen is my favourite.
         I also enjoy playing card games such as Poker"

- 🤖 I am developing a business with my sister based on bingo but including the experience of smelling and recognincing the smell of 
         food, plants, spice... is a completely unknown experience for most of the assitants"

- 🏂 I like cooking, doing Yoga, Mindfullnes, playing card games, ski...

- 📫 mmartovi@icloud.com and I invite you to follow the instagram of my company:
          https://www.instagram.com/elgranbingoolfativo?utm_source=ig_web_button_share_sheet&igsh=OGQ5ZDc2ODk2ZA==
         
- 🏠 Barcelona (Spain)
>>>>>>> 71f85e6c8ba48ee70b4f15e98c730baf2cde4a3a
""")


# Feel free to add other points like your Linkedin, Github, Social Media, etc.

<<<<<<< HEAD

=======
>>>>>>> 71f85e6c8ba48ee70b4f15e98c730baf2cde4a3a
