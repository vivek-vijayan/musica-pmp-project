'''
Author: Vivek Vijayan
Date: 9 Oct 2023
Description : A desktop application using python to play the music and 
              create a playlist from the files available locally.
'''
# imports
import os
import sys
from datetime import datetime
import tkinter
from tkinter import ttk


class Genre:
    def __init__(self, genre_name, genre_id) -> None:
        self.genre_id = genre_id
        self.genre_name = genre_name


class Song:
    def __init__(self, name:str, location:str, art:str, duration:int, genre:Genre, tag:str) -> bool:
        self.song_name = name
        self.song_location = location
        self.song_art = art
        self.song_duration = duration
        self.song_genre = genre
        self.song_tag = tag


class Playlist:
    def __init__(self) -> None:
        self.playlist_name
        self.playlist_created_on
        self.audio: Song = None
        self.next:Playlist = None
        self.prev:Playlist = None
    
    def add_song_to_playlist(self, new_playlist):
        self.next = new_playlist

class Playlist_Collection:
    def __init__(self, name, playlist) -> None:
        self.head:Playlist = playlist
        self.collection_name = name

    def delete_playlist(self):
        self.head = None


