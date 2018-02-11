#first class example
class Song(object):
    def __init__(self, lyrics):
        self.lyrics=lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            
            
happy_bday= Song(['Happy Birthday to you', 'I dont want to get sued',
                "So I'll stop right here"])
                
bulls_on_parade= Song (['They rally around the family', 
                        'With pockets full of shells'])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song() 


#my song

class canzone():
    def __init__ (self,daje):
        self.daje=daje
        
    def karaoke(self):
        for line in self.daje:
            print line  
        
ninna=canzone(['ninna nanna', 'ninna oh', 'questo pupo a chi lo do'])
nanna=canzone(['ohioioi ohioioioi cara giorgia segna per noi'])

ninna.karaoke()
nanna.karaoke()

#output: ['ninna nanna', 'ninna oh', 'questo pupo a chi lo do']
#['ninna nanna', 'ninna oh', 'questo pupo a chi lo do']
# to have the words printed you have to specify a for loop
# for line in self.daje
                

   