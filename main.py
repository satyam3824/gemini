import streamlit as st      #importing streamlit library

st.header("Gemini English Grammar Check")  #title of website
st.write("Hello")  #display a normal text


if st.button("Click me"): #display a button with a message
      st.write("Button clicked.")
# st.download_button("Download file", data)


import pandas as pd
# to create a download button
st.download_button(
    label="Download Hello World File",
    data="Hello World",
    file_name="data.txt",
    icon=":material/download:",
)

# create a link button
url = 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet'
st.link_button("Go to gallery", url)
st.page_link('https://docs.streamlit.io/develop/quick-reference/cheat-sheet', label="Home")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


# checkbox
if st.checkbox("I agree"):
      st.write("Checkbox is clicked.")

# returns an integer
my_feed = st.feedback("thumbs") 
st.write(my_feed)
st.feedback("stars")
st.feedback("faces")


p1 = st.pills("Tags", ["Sports", "Politics"])
st.write(p1)

# radio button
r1 = st.radio("Pick one", ["cats", "dogs"], key='1')
st.write(r1)

r1 = st.radio("Pick one", ["cats", "dogs"], key='2')
st.write(r1)

# image
st.image("https://upscfever.com/upsc-fever/assets/images/home/home-icons-100/rbi.png")
# map
df = pd.DataFrame(
    {
        "col1": [20.5937],
        "col2": [78.9629],
    }
)
st.map(df, latitude="col1", longitude="col2")

# markdown
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.
Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)



st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")

# # Use widgets' returned values in variables:
# for i in range(int(st.number_input("Num:"))):
#     foo()
# if st.sidebar.selectbox("I:",["f"]) == "f":
#     b()
# my_slider_val = st.slider("Quinn Mallory", 1, 88)
# st.write(slider_val)

# Disable widgets to remove interactivity:
st.slider("Pick a number", 0, 100, disabled=True, key="slider1")
st.slider("Pick a number", 0, 100, disabled=True, key="slider2")



