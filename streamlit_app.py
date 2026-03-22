import streamlit as st

# page setup
about_page = st.Page(
    page = "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True 
)

project_1_page = st.Page(
    page = "views/food_vision_big.py",
    title = "Food Vision Big",
    icon = ":material/bar_chart:",
)


# Navigation Setup
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page]
    }
)

# shared on all pages
st.logo("assets/vrudish_ai_logo.png", )
st.sidebar.text("Made with ❤️ by Vrudish")


# Run the app
pg.run()
