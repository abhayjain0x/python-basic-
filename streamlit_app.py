import requests
import json
import streamlit as st
import random
import time

st.set_page_config(page_title="Hacker News", page_icon=":newspaper:", layout="wide")

# Add a header and logo
header = st.container()
with header:
    st.title(":rainbow[Hacker News Sanity]")

colors = ['blue', 'green', 'orange', 'red', 'violet', 'gray']

def getting_ids():
    url = 'https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty'
    ids = requests.get(url=url)
    ids.raise_for_status()
    return ids.json()

def get_story_metadata(id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
    news = requests.get(url=url)
    news.raise_for_status()
    news_data = news.json()
    title = news_data.get('title', 'No title')
    urlu = news_data.get('url', 'No URL')
    score = news_data.get('score', 0)
    
    # Use columns to display story info
    col1, col2 = st.columns([4,1])
    with col1:
        st.subheader(f":{random.choice(colors)}[{title}]")
        st.write(f"[Read more]({urlu})")
    with col2:
        st.metric(label="Score", value=score)
    st.divider()
    time.sleep(1)

def display_stories(num_stories):
    ids = getting_ids()
    
    # Show a progress bar while loading stories
    progress_bar = st.progress(0)
    for i, id in enumerate(ids[:num_stories]):
        get_story_metadata(id)
        progress_bar.progress((i+1)/num_stories)
        time.sleep(0.1)

# Use a slider to select number of stories
num_stories = st.slider("Select number of stories:", min_value=5, max_value=50, value=10)

# Improved start button with custom CSS
start_button_css = """
    <style>
    .stButton > button {
        width: 100%;
        font-size: 20px;
        padding: 10px;
        border-radius: 5px;
        background-color: #00224D;
        color: white;
        font-weight: bold;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #00224D;
        transform: scale(1.02);
    }
    </style>
"""
st.markdown(start_button_css, unsafe_allow_html=True)

start_button = st.empty()
if start_button.button('Get Top Stories'):
    start_button.empty()
    display_stories(num_stories)
    
    # Add a reset button
    if st.button('Reset'):
        start_button.button('Get Top Stories')
        st.rerun()
