class Playlist:
    def __init__(self):
        self.name = input('Playlist Name : ')
        self.songs = []
        
    def addsong(self):
        n = int(input('Jumlah Lagu : '))
        for i in range(n):
            name = input('Song Name : ')
            self.songs.append(name)
            
    def display(self):
        print(f'{self.name} Playlist')
        for i in range(len(self.songs)):
            print(self.songs[i])
            
def main():
    pl = Playlist()
    pl.addsong()
    pl.display()
    
if __name__ == '__main__':
    main()
    