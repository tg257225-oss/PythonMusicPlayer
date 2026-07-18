import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed! ", e)
        return


    folder = "music"

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found.")
        return


    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]


    if not mp3_files:
        print("No .mp3 files found.")


    while True:
        print("***** MP3 PLAYER *****")
        print("My song list:")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        break

if __name__ == "__main__":
    main()