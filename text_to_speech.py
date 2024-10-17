import pyttsx3

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        rate = engine.getProperty("rate")
        
        # Reduce the rate by 70
        new_rate = max(rate - 100, 200)  # Ensure rate doesn't go below 50
        engine.setProperty("rate", new_rate)
        
        # Optionally set a voice (male/female)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Change index to select different voices (0 for male, 1 for female)
        
        engine.say(text)
        engine.runAndWait()
    
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

# Example usage
if __name__ == "__main__":
    text_to_speech("Hello sir ! i am your voice assistance , how can i help you today.")

################################# DONE  ###############################################
