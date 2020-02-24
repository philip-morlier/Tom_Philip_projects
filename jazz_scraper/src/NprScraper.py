from bs4 import BeautifulSoup

class NprScraper():

    def get_page(self, url):
        pass

    def create_sportify_playlist(self, playlist):
        pass

    def parse(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        song_data = soup.find_all("div", {"class": "single-data"})
        sack = []
        for i in song_data:
            song = {}
            for x in i.find_all("div", {"class": "label"}):
                if 'ARTIST' in x:
                    song['artist'] = (x.getText().split(':')[1])
                if str(x).__contains__('TITLE'):
                    song['title'] = (x.getText().split(':')[1])
                if str(x).__contains__('ALBUM'):
                    song['album'] = (x.getText().split(':')[1])
                # TODO: only add if song contains all three items
                sack.append(song)