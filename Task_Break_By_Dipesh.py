import time
import webbrowser 
from random import randint

name = input("Enter Your Name : ")
print(f"Hi {name}, Please tell us your favorite genre from following :")

links = {
         "Gazal":['https://www.youtube.com/watch?v=IfqcSo3zOsI',
                  'https://www.youtube.com/watch?v=5bLN85bo48s',
                  'https://www.youtube.com/watch?v=dDO9ZRSNB9s'],
         "Rock":['https://www.youtube.com/watch?v=eY62RfeviuE',
                  'https://www.youtube.com/watch?v=-tJYN-eG1zk',
                  'https://www.youtube.com/watch?v=9jK-NcRmVcw'],
         "Romantic":['https://www.youtube.com/watch?v=hjfzFVw2Zjo',
                  'https://www.youtube.com/watch?v=43wT0xhvfsA',
                  'https://www.youtube.com/watch?v=L7t73qAbkN4'],
         "Jazz":['https://www.youtube.com/watch?v=OOO4ROO_sPM',
                  'https://www.youtube.com/watch?v=QN2RnjFHmNY',
                  'https://www.youtube.com/watch?v=447yaU_4DF8'],
         "Bhajan":['https://www.youtube.com/watch?v=D9zhvsmDckk',
                  'https://www.youtube.com/watch?v=iW16WWmWZL4',
                  'https://www.youtube.com/watch?v=PlgIlN5gmQw'],
         "Indie":['https://www.youtube.com/watch?v=gGdGFtwCNBE',
                  'https://www.youtube.com/watch?v=pK7egZaT3hs',
                  'https://www.youtube.com/watch?v=hTWKbfoikeg'],
         "Classics":['https://www.youtube.com/watch?v=saApSghVCOU',
                     'https://www.youtube.com/watch?v=Ti5SNrWxftE',
                     'https://www.youtube.com/watch?v=EE9JDSlsH3E']
        }   

def display_genre():
	for key in links.keys():
		print(key,end=", ")

display_genre()

genre = input("\nEnter your favorite genre : ")
interval = int(input("Enter time interval in minutes : ")) 
    
def generate_random():
  x = randint(0,len(links[genre])-1)
  return x

def convert_to_seconds():
  minutes_to_seconds = interval * 60
  return minutes_to_seconds

seconds = convert_to_seconds()

def my_playlist():
  while True:
    url = links[genre][generate_random()]
    time.sleep(seconds)
    webbrowser.open(url)

my_playlist()