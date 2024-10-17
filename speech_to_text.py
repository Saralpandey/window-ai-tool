import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1.7)  # Dynamically adjust for ambient noise
        print("Say something...")
        
        # Listen to the audio from the microphone with a timeout
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None

    try:
        voice_data = r.recognize_google(audio, language='en-US')
        print("You said: " + voice_data)
        return voice_data  # Return the recognized text
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return None  # Return None if the audio could not be understood
    
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None  # Return None if there was a request error

def get_audio():
    return speech_to_text()  # Call the function directly

# Example function that uses get_audio
def ask():
    ask_val = get_audio()
    if ask_val:
        print(f"You said: {ask_val}")
    else:
        print("No valid audio input.")

# Assuming you have a function to start your application
if __name__ == "__main__":
    ask()  # Call the ask function or similar to initiate
