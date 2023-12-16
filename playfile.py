import pygame

# Initialize pygame
pygame.init()

# Load the MP3 file
pygame.mixer.init()
pygame.mixer.music.load('/Users/chrisventer/Documents/Python code/OpenAI/speech.mp3')  # Replace 'yourfile.mp3' with your MP3 file path

# Play the MP3 file
pygame.mixer.music.play()

# Keep the script running until the music is playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

