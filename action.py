import datetime
import webbrowser
import requests
import text_to_speech
import weather
from bs4 import BeautifulSoup

def search_youtube_scrape(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    try:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if '/channel/' in href or '/user/' in href:
                return f"https://www.youtube.com{href}"  # Return the first found link
    except Exception as e:
        print(f"Error fetching YouTube data: {e}")
    return "No channel found."

def get_news():
    url = 'https://inshortsapi.vercel.app/news'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            return news_data['data']
        else:
            return "Could not fetch news at this time."
    except Exception as e:
        return f"Error fetching news: {e}"

def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data['type'] == 'single':
                return joke_data['joke']
            else:
                return f"{joke_data['setup']} ... {joke_data['delivery']}"
    except Exception as e:
        return f"Error fetching joke: {e}"

def Action(send):
    if send is None:
        print("Expected a string but got NoneType")
        return None  # Prevent further processing of NoneType
    
    user_data = send.lower()  # Proceed if send is a valid string

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is NAVI.")
        return "My name is navi."
    
    elif "jokes" in user_data or "tell me some jokes" in user_data:
        
        return "jokes is ready sir", get_joke()

    elif "news" in user_data or "today news" in user_data:
        return "here is today most important headlines",get_news()
        
    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hey, sir! How can I help you?")
        return "Hey, sir! How can I help you?"
    
    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I am doing great these days, sir.")
        return "I am doing great these days, sir."

    elif "thank you" in user_data or "thank" in user_data:
        text_to_speech.text_to_speech("It's my pleasure to assist you, sir.")
        return "It's my pleasure to assist you, sir."
        
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning, sir! How can I assist you today?")
        return "Good morning, sir! How can I assist you today?"

    elif "time now" in user_data:
        current_time = datetime.datetime.now().strftime("%H:%M")
        text_to_speech.text_to_speech(f"The current time is {current_time}.")
        return f"The current time is {current_time}."

    elif "shutdown" in user_data or "quit" in user_data:
        text_to_speech.text_to_speech("Okay, sir.")
        return "Okay, sir."

    elif "play music" in user_data or "music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is now ready for you. Enjoy your music!")
        return "Spotify is now ready for you. Enjoy your music!"

    elif "play millionaire song" in user_data:
        url='https://www.youtube.com/watch?v=XO8wew38VM8'
        webbrowser.open(url)
        text_to_speech.text_to_speech("The song is ready for you, sir. Enjoy!")
        return "The song is ready for you, sir. Enjoy!"

    elif "youtube" in user_data or "open youtube" in user_data:
        url='https://youtube.com/'
        webbrowser.open(url)
        text_to_speech.text_to_speech("YouTube is now ready for you.")
        return "YouTube is now ready for you."

    elif "search youtube" in user_data or "triggered insaan" in user_data:
        channel_name = user_data.replace("search youtube", "").replace("find channel", "").strip()
        if channel_name:
            channel_link = search_youtube_scrape(channel_name)
            text_to_speech.text_to_speech(f"I found this channel: {channel_link}")
            return channel_link
        else:
            return "Please specify the channel name."

    elif "open google" in user_data or "google" in user_data:
        url = 'https://google.com/'
        webbrowser.open(url)
        text_to_speech.text_to_speech("Google is now ready for you.")
        return "Google is now ready for you."

    elif "chatgpt" in user_data or "open chatgpt" in user_data:
        url='https://openai.com/chatgpt/'
        webbrowser.open(url)
        text_to_speech.text_to_speech("ChatGPT is open for you. Click the start button to begin.")
        return "ChatGPT is open for you. Click the start button to begin."

    elif "check weather" in user_data:
        ans = weather.Weather()  # Assuming weather() returns a string response
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I'm not able to understand your request.")
        return "I'm not able to understand your request."
