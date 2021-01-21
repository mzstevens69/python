import sys #used for providing url as argument
from urllib.request import urlopen


def fetch_story(url):
    paragraph = urlopen(url)
    new_paragraph = []
    for line in paragraph:
        line_letters = line.decode('utf-8').split()
        for letter in line_letters:
            new_paragraph.append(letter)
    paragraph.close()
    return new_paragraph

def print_items(items):
    for item in items:
        print(item)

def main(url):    
    words = fetch_story(url)
    print_items(words)


if __name__ == ' __main__':
    main(sys.argv[1])