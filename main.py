import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame



def play_music(folder,song_name):

    file_path = os.path.join(folder, song_name)


    if not os.path.exists(file_path):
        print("File not found.")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top, [V]olume, Restar[T]")

    while True:
        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Music paused.")

        if command == "R":
            pygame.mixer.music.unpause()
            print("Music resumed.")


        if command == "T":
            pygame.mixer.music.rewind()
            print("Music restarted.")


        if command == "S":
            pygame.mixer.music.stop()
            print("Music stopped.")
            break

        if command == "V":
            while True:
                vol_input = input("\nEnter the volume level (0-100): ")

                try:
                    vol_percent = int(vol_input)
                except ValueError:
                    print("Invalid choice. Please enter a number between 0 and 100.")
                    continue

                if vol_percent > 100 or vol_percent < 0:
                    print("Invalid choice. Please enter a number between 0 and 100.")
                    continue

                vol_percent = max(0, min(100, vol_percent))
                pygame.mixer.music.set_volume(vol_percent/100)
                print(f"Volume set to {vol_percent}%")
                break






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

        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("Quitting...")
            break


        if not choice_input.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice = int(choice_input) -1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()