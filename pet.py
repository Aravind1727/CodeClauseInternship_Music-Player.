import tkinter as tk
from tkinter import filedialog
import threading
from tkinter import ttk
import time

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        self.entry_width = 40  # Width for the buttons
        
        self.playlist = []
        self.current_song_index = -1
        self.playing = False
        
        self.label = tk.Label(root, text="Music Player", font=("Helvetica", 20))
        self.label.pack(pady=10)
        
        self.playlist_label = tk.Label(root, text="Playlist:")
        self.playlist_label.pack(pady=5)
        
        self.playlist_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.playlist_listbox.pack(padx=20, pady=5)
        
        self.add_button = tk.Button(root, text="Add Song", width=self.entry_width, command=self.add_song)
        self.add_button.pack(pady=5)
        
        self.play_button = tk.Button(root, text="Play", width=self.entry_width, command=self.play_pause_song)
        self.play_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop", width=self.entry_width, command=self.stop_song)
        self.stop_button.pack(pady=5)
        
        self.add_hover_effects()
    
    def add_hover_effects(self):
        buttons = [self.add_button, self.play_button, self.stop_button]
        
        for button in buttons:
            button.bind("<Enter>", lambda event, b=button: self.on_enter(event, b))
            button.bind("<Leave>", lambda event, b=button: self.on_leave(event, b))
        
    def on_enter(self, event, button):
        button.config(bg="lightgreen")
        
    def on_leave(self, event, button):
        button.config(bg="SystemButtonFace")
    
    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")])
        if song_path:
            song_name = song_path.split("/")[-1]
            self.playlist.append(song_path)
            self.playlist_listbox.insert(tk.END, song_name)
    
    def play_pause_song(self):
        if not self.playing:
            self.play_song()
        else:
            self.pause_song()
    
    def play_song(self):
        selected_song = self.playlist_listbox.curselection()
        if selected_song:
            song_index = selected_song[0]
            if self.current_song_index != song_index:
                self.stop_song()
                self.current_song_index = song_index
                
                song_path = self.playlist[song_index]
                self.playing = True
                self.play_button.config(text="Pause")
                
                self.playback_thread = threading.Thread(target=self.play_audio, args=(song_path,))
                self.playback_thread.start()
    
    def pause_song(self):
        self.playing = False
        self.play_button.config(text="Play")
    
    def stop_song(self):
        self.playing = False
        self.play_button.config(text="Play")
    
    def play_audio(self, song_path):
        self.audio = tk.StringVar()
        self.audio.set(song_path)
        self.root.update_idletasks()
        
        self.audio_obj = tk.ttk.Audio.play(self.audio.get())
        time.sleep(self.audio_obj.info().length)
        
        self.playing = False
        self.play_button.config(text="Play")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
