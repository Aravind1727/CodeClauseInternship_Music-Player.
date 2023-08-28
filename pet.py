import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        pygame.init()
        pygame.mixer.init()
        
        self.playlist = []
        
        self.label = tk.Label(root, text="Music Player", font=("Helvetica", 20))
        self.label.pack(pady=10)
        
        self.playlistbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.playlistbox.pack(padx=20, pady=20)
        
        button_width = 10  # Adjust the width for the buttons
        
        self.add_button = tk.Button(root, text="Add Song", width=button_width, command=self.add_song)
        self.add_button.pack(padx=20)
        
        self.play_button = tk.Button(root, text="Play", width=button_width, command=self.play_song)
        self.play_button.pack(padx=20)
        
        self.stop_button = tk.Button(root, text="Stop", width=button_width, command=self.stop_song)
        self.stop_button.pack(padx=20)
        
    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if song_path:
            self.playlist.append(song_path)
            song_name = song_path.split("/")[-1]
            self.playlistbox.insert(tk.END, song_name)
    
    def play_song(self):
        selected_song = self.playlistbox.curselection()
        if selected_song:
            song_index = selected_song[0]
            song_path = self.playlist[song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
    
    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
