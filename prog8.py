'''define a class called songs, it will show the lyrics of the song 
its __init__()methods should have two ba \aruguments:self and lyrics.
lyrics is a list.inside your class create a method called sing_me_a song
that prints each element of lyrics on his own line .define varible:
'''
class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
happy_bday.sing_me_a_song()