from swarm import Swarm, Agent
import os
import dotenv

from triage_agent.tools import (
    transfer_to_plan,
    transfer_to_google_maps,
    transfer_to_weather,
    get_google_maps_directions,
    get_weather,
    transfer_back_to_triage
)

from triage_agent.prompts import (
    TRIAGE_INSTRUCTIONS,
    PLAN_INSTRUCTIONS,
    GOOGLE_MAPS_INSTRUCTIONS,
    WEATHER_INSTRUCTIONS,
)

dotenv.load_dotenv()

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") # original api that runs
api_key = "GOOGLE_MAPS_API_KEY"
api_key = "3d8f139292cf72433268ec1b62594143"

client = Swarm()

# client = Swarm(Agent='triage_agent',Agent=plan_agent,  google_maps_agent, weather_agent,open_file_agent, close_app_agent])

triage_agent = Agent(
    name="Triage Agent",
    instructions=TRIAGE_INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[transfer_to_plan, transfer_to_google_maps, transfer_to_weather]
)

plan_agent = Agent(
    name="Plan Agent",
    instructions=PLAN_INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[]
)

google_maps_agent = Agent(
    name="Google Maps Agent",
    instructions=GOOGLE_MAPS_INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[get_google_maps_directions]
)

weather_agent = Agent(
    name="Weather Agent",
    instructions=WEATHER_INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[get_weather]
)


# # Set up functions for each agent
triage_agent.functions = [transfer_to_plan, transfer_to_google_maps, transfer_to_weather]
plan_agent.functions = [transfer_back_to_triage]
google_maps_agent.functions = [transfer_back_to_triage]
weather_agent.functions = [get_weather, transfer_back_to_triage]






# import os
# import dotenv
# import pyttsx3
# import speech_recognition as sr
# from swarm import Swarm, Agent
# from triage_agent.tools import (
#     transfer_to_plan,
#     transfer_to_google_maps,
#     transfer_to_weather,
#     get_google_maps_directions,
#     get_weather,
#     transfer_back_to_triage
# )
# from triage_agent.prompts import (
#     TRIAGE_INSTRUCTIONS,
#     PLAN_INSTRUCTIONS,
#     GOOGLE_MAPS_INSTRUCTIONS,
#     WEATHER_INSTRUCTIONS
# )

# # Load environment variables
# dotenv.load_dotenv()

# # Set your OpenAI API key here
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY"),os.getenv("GOOGLE_MAPS_API_KEY")

# # Initialize Swarm client and agents
# client = Swarm()

# triage_agent = Agent(
#     name="Triage Agent",
#     instructions=TRIAGE_INSTRUCTIONS,
#     model="gpt-4o",
#     tools=[transfer_to_plan, transfer_to_google_maps, transfer_to_weather]
# )

# plan_agent = Agent(
#     name="Plan Agent",
#     instructions=PLAN_INSTRUCTIONS,
#     model="gpt-4o",
#     tools=[]
# )

# google_maps_agent = Agent(
#     name="Google Maps Agent",
#     instructions=GOOGLE_MAPS_INSTRUCTIONS,
#     model="gpt-4o",
#     tools=[get_google_maps_directions]
# )

# weather_agent = Agent(
#     name="Weather Agent",
#     instructions=WEATHER_INSTRUCTIONS,
#     model="gpt-4o",
#     tools=[get_weather]
# )


# # Set up text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Speed of speech
# engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# # Initialize speech recognition
# recognizer = sr.Recognizer()

# # Function to capture speech input
# def listen():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             print(f"User said: {text}")
#             return text
#         except sr.UnknownValueError:
#             speak("Sorry, I didn't catch that. Can you repeat?")
#             return None
#         except sr.RequestError:
#             speak("Sorry, there was an issue with the speech service. Try again later.")
#             return None

# # Function to speak output
# def speak(text):
#     print(f"Agent says: {text}")  # Debug output
#     engine.say(text)
#     engine.runAndWait()

# # Example function to simulate an agent interaction
# def handle_agent_interaction(input_text):
#     # Simulate processing input by the triage agent
#     if input_text:
#         response = triage_agent.run(input_text)  # Use your agent's processing method
#         speak(response)  # Convert agent's response to speech


# # Set up functions for each agent
# triage_agent.functions = [transfer_to_plan, transfer_to_google_maps, transfer_to_weather]
# plan_agent.functions = [transfer_back_to_triage]
# google_maps_agent.functions = [transfer_back_to_triage]
# weather_agent.functions = [get_weather, transfer_back_to_triage]

# # Main loop to run the system
# def main():
#     while True:
#         user_input = listen()  # Get user input via voice
#         if user_input:
#             handle_agent_interaction(user_input)  # Process the input through the agent

# if __name__ == "__main__":
#     main()