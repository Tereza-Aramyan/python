'''
Music streaming data design
'''

import datetime
import string
import os.path
import uuid
import os
import threading
import multiprocessing
import time
from datetime import date


class InvalidUserError(TypeError):

    def __init__(self, message: str, reason: str):
        super().__init__(message)
        self.reason = reason

class common_method():
    def __init__(self):
        self.path = f'.\\data\\{self.__class__.__name__}'
        super().__init__()

        if not os.path.isdir("data"):
            os.makedirs ("data")

    def save(self):
        with open(self.path, 'a+') as df:
#            all_data = df.readlines()
#            for line in all_data:
#                if (line is not self.__dict__):
            df.write(str(self.__dict__))
            df.write("\n")
        df.close()

    def update(self , **kwargs):
        for k, v in kwargs.items():
            if self.__dict__.get(k):
                self.__dict__[k] = v
                self.__dict__["id"] = str(uuid.uuid3(uuid.NAMESPACE_DNS, f'{self.__dict__["id"]}{self.__dict__[k]}'))
            else :
                raise Exceptions(f'{self.__class__.__name__} does not have field_1, field_2, ...., use fields from ')
        return self.__dict__

    def delete(self):
        with open(self.path, 'r+') as df:
            all_data = df.readlines()
            df.seek(0)
            for line in all_data:
                reader = eval(line)
                if (self.__dict__["id"] not in reader.values()):
                    df.write(line)
            df.truncate()
        df.close()

    def filter(self,**kwargs):
        filtered_list = ""
        with open(self.path, 'r') as df:
            for line in df:
                flag = 1
                for k,v in kwargs.items():
                    if ((eval(line))[k] != v):
                        flag = 0
                if (flag ==1):
                    filtered_list = f"{filtered_list}{line}"
        return filtered_list


    def get(self, **kwargs):
        ret = (self.filter(**kwargs)).split("\n")
        if(len(ret) == 2):
            return "\n".join(ret)
        elif(len(ret) >2  ):
            raise Exception(f'Multiple {self.__class__.__name__} objects founded')
        else:
            raise Exception(f'No {self.__class__.__name__} objects founded')

#######################################################################################################################################
#1
class User(common_method):
    def __init__(self , first_name: str, last_name: str, email: str, password: None, profile_pic: None, birth_date: None, level : 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.profile_pic = profile_pic
        self.birth_date = birth_date
        self.level = level
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, f'{self.first_name}{self.last_name}'))
        self.validate_user()
        super().__init__()


    def validate_user(self):
        if not '@' in self.email:
            raise TypeError('Input email with correct format.')
        if (self.first_name is None or self.last_name is None ) :
            raise TypeError('First name and last name must be set.')
        if(not(any(str(el).isdigit() for el in self.password) & any(el.isupper() for el in self.password) &
               any(el.islower() for el in self.password) & any(str(el) in string.punctuation for el in self.password))):
            raise TypeError('Password does not match requirments')

    def create_playlist(self, name):
        flag = 1
        with open(".\\data\\Playlist", 'r+') as df:
            all_data = df.readlines()
            for line in all_data:
                if ( (name in line) &  (self.first_name in line) & (self.last_name in line)):
                    flag = 0
                    break
        df.close()
        if (flag == 1):
            playlist = Playlist(name, self, None)
            return playlist


    def delete_playlist(self, name):
        with open(".\\data\\Playlist", 'r+') as df:
            all_data = df.readlines()
            df.seek(0)
            for line in all_data:
                reader = eval(line)
                if (name is not reader['name']):
                    df.write(line)
            df.truncate()
        df.close()

############################################################################################################################
#4
class Playlist(common_method):
    def __init__(self, name: str, created_by: User, picture_url: str):
        self.name = name
        self.date_added = f'{date.today()}'
        self.created_by = created_by.__dict__
        self.picture_url = picture_url
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, f'{self.name}{created_by.last_name}'))
        self.count_of_songs = 0
        self.genre_list = {}
        self.duration_of_playlist = 0
        super().__init__()

    @property
    def count_of_songs(self):
        return self._count_of_songs

    @count_of_songs.setter
    def count_of_songs(self, value):
        self._count_of_songs = value
    ######################################
    @property
    def duration_of_playlist(self):
        return self._duration_of_playlist

    @duration_of_playlist.setter
    def duration_of_playlist(self, value):
        self._duration_of_playlist  = value
    ######################################
    @property
    def genre_list(self):
        return self._genre_list

    @genre_list.setter
    def genre_list(self,value):
        self._genre_list = value

    def play(self):
        print(f'Starting play {self.name}')
        self.start = time.time()
        self.play_thread = threading.Thread(target=Playlist._play, args=(self,))
        self.play_thread.start()


    def _play(self):
        time.sleep(self.duration_of_playlist)
        if(self.play_thread.is_alive()):
            self.play_thread._is_stopped = True
            print(f'Duration of {self.name} play { time.time() - self.start}')
            print(f"end playing the playlist")

    def stop(self):
        if (self.duration_of_playlist > int(time.time() - self.start)):
            self.play_thread._is_stopped = True
            print("thread is going to be stopped")
            print(f'Duration of {self.name} playlist is { time.time() - self.start}')


###########################################################################################################################################
#5
class Album(Playlist,common_method):
    def __init__(self, name, created_by, picture_url, label: str, year: int):
        Playlist.__init__(self, name, created_by, picture_url)
        self.date_added = f'{date.today()}'
        self.label = label
        self.year = year
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, f'{self.name}{label}{self.id}'))
        #self.validate()
        common_method.__init__(self)

    def validate(self):
        if not isinstance(self.created_by, Artist):
            raise Exception('Access denied.')

###########################################################################################################################################
#2
class Artist(User,common_method):
    def __init__(self, first_name, last_name, email, password, profile_pic, birth_date, level, about: str, listeners_count: int):
        User.__init__(self, first_name, last_name, email, password, profile_pic, birth_date, level)
        self.about =about
        self.listeners_count = listeners_count
        common_method.__init__(self)

    def add_song(self, title: str, artist_name: str, duration : int, year: int, genre : str, file: str, album: Album = None):
        if(album == None):
            album = self.create_album(title,0,year,None)
        new_song = Song(title, artist_name, duration, genre, year, self, 1, album)
        new_song.save()

        album.count_of_songs += 1
        album.save()

    def delete_song(self, song_id):
        with open(".\\data\\Song", 'r+') as df:
            all_data = df.readlines()
            df.seek(0)
            for line in all_data:
                reader = eval(line)
                if (song_id not in reader.values()):
                    df.write(line)
                else:
                    album.count_of_songs -= 1
                    album.save()
            df.truncate()
        df.close()

    def create_album(self, title, label, year, list_of_song_url=None):
        flag = 1
        with open(".\\data\\Album", 'r+') as df:
            all_data = df.readlines()
            for line in all_data:
                if ( (title in line) &  (self.first_name in line) & (self.last_name in line)):
                    flag = 0
                    break
        df.close()
        if (flag == 1):
            album = Album(title, self, None, label, year)
            return album


    def delete_album(self, album_id):
        with open(".\\data\\Album", 'r+') as df:
            all_data = df.readlines()
            df.seek(0)
            for line in all_data:
                reader = eval(line)
                if (album_id not in reader.values()):
                    df.write(line)
            df.truncate()
        df.close()

################################################################################################################################
#3
class Song(common_method):
    def __init__(self, title: str, artist: str, duration: int, genre: str, year: int, created_by: Artist, streams_count: int, album: Album):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.year = year
        self.created_by = created_by
        self.streams_count = streams_count
        self.album = album.__dict__
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, f'{self.title}{self.artist}'))
        #self.validate()
        super().__init__()


    def validate(self):
        if not isinstance(self.created_by, Artist):
            raise Exception('Access denied.')


    def add_to_playlist(self, playlist):
        playlistsong = PlaylistSong(playlist, self)
        playlistsong.save()

        playlist.duration_of_playlist += self.duration
        if (self.genre in (playlist.genre_list).keys()):
            playlist.genre_list[f"{self.genre}"] += 1
        else :
            playlist.genre_list[f"{self.genre}"] = 1

        playlist.save()


    def remove_from_playlist(self, playlist):
        with open(".\\data\\PlaylistSong", "r+") as df:
            all_data = df.readlines()
            df.seek(0)
            for line in all_data:
                if ( not ( line.find(self.id) & line.find(playlist.id)) ):
                    df.write(line)
                else:
                    playlist.duration_of_playlist -= self.duration

                    if (self.genre in (playlist.genre_list).keys()):
                        if (playlist.genre_list[f"{self.genre}"] == 1):
                            del playlist.genre_list[f"{self.genre}"]
                        else:
                            playlist.genre_list[f"{self.genre}"] -=  1

                    playlist.save()

            df.truncate()
        df.close()

    def play(self):
        print(f'Starting play {self.title}')
        self.start = time.time()
        self.play_thread = threading.Thread(target=Song._play, args=(self,))
        self.play_thread.start()


    def _play(self):
        time.sleep(self.duration)
        if(self.play_thread.is_alive()):
            self.play_thread._is_stopped = True
            print(f'Duration of {self.title} play { time.time() - self.start}')
            print(f"end playing the song")
        self.streams_count +=1
        self.created_by.listeners_count +=1
        self.created_by.save()
        self.save()

    def stop(self):
        if (self.duration > int(time.time() - self.start)):
            self.play_thread._is_stopped = True
            print("thread is going to be stopped")
            print(f'Duration of {self.title} play { time.time() - self.start}')


    def download(self):
        return os.path.realpath('.\\data\\Song')

################################################################################################################################
#6
class SongPlayes(common_method):
    def __init__(self,  song :Song, username: str):
        self.id =id
        self.user =username
        self.song =song
        self.start_timestamp = time.time()
        super().__init__()

###############################################################################################################################
#7
class PlaylistSong(common_method):
    def  __init__(self, playlist: Playlist, song: Song):
        self.playlist =playlist.__dict__
        self.song = song.__dict__
        self.date_added = f'{date.today()}'
        super().__init__()


###############################################################################################################################

if __name__ == '__main__':
    user = User("Tereza Aramyan", "Aramyan","aramyan-tereza@mail.ru", "Febr#$15",None,"21/03/1998", 0)
    artist = Artist("Harutyun", "Krrikyan","harutk@mail.com", "Abfg$#54", None,None, 1,"aaaa",0)
    playlist = Playlist("saved",user, None)
    album = Album("bl in your area",user,None,None,2016)
    song = Song("song1","Halsey",5, "rock",2017,artist,0,album)
    playlistsong =PlaylistSong(playlist,song)
    song2 = Song("song2","ppp",10, "pop",2017,artist,0,album)
    #song.add_to_playlist(playlist)
    #song2.add_to_playlist(playlist)
    #playlist.play()
    #time.sleep(3)
    #playlist.stop()
    #song.play()
    #song.play()
    #song.play()
    #song2.play()
    #time.sleep(6)
    #song.stop()
    #song2.stop()



    #playlist2 = Playlist("new",user, None)
    #playlist.save()
    #user.create_playlist("saved")
    #user.create_playlist("new")
    #album = Album("bl in your area",user,None,None,2016)
    #album.save()
    #artist.create_album("bl in your area",0, 2020,None)
    #song = Song("fff","Halsey",2*60, "rock",2017,artist,0,album)
    #song2 = Song("ddd","ppp",187, "pop",2017,artist,0,album)
    #artist.add_song("add_son2222","test", 3*60, 2020, "rock", None,album)
    #artist.add_song("add_son","test", 3*60, 2020, "rock", None,album)
    #artist.add_song("affffff","test", 3*60, 2020, "rock", None,album)
    #artist.add_song("llllllll","test", 3*60, 2020, "rock", None,album)
    #artist.delete_song("3cd78259-e847-3f63-a3c0-75c450227ad6")

    #playlistsong.save()
    #song2.remove_from_playlist(playlist)
    #song.add_to_playlist(playlist)
    #song2.add_to_playlist(playlist)
    #song.remove_from_playlist(playlist)
    #song.add_to_playlist(playlist)
    #song3 = Song("dffgfgfgfd","pppoooooooooo",1000, "pop",2017,artist,0,album)
    #song3.add_to_playlist(playlist)
    #song.remove_from_playlist(playlist)
    #song.save()


    #album = Album("buuua",user,None,None,2016)
    #album.save()


    #playlist = Playlist("saved",user, None)
    #playlist.save()
    #user.create_playlist("liked")
    #user.delete_playlist("saved")

    #print(user.filter(first_name = "Tereza"))
    #print(user.filter(last_name = "Aramyan"))

    #print(user.get(first_name = "Tereza"))
    #print(user.get(last_name = "Aramyan"))
    #print(user.get(last_name = "Auamyan"))

    #user.save()
    #user.delete()
    #user.update(first_name = "Satenik")
    #user.save()
    #user.delete()
    #user.update(first_name = "Harutyun", last_name = "Krrikyan")
    #user.save()


    #artist = Artist("Tereza", "Aramyan","aramyan-tereza@mail.ru", "Febr#$15","None","21/03/1998", 0, 'asas', 5)