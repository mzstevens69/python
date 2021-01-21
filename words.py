from urllib.request import urlopen

def fetch_story():
    paragraph = urlopen('https://sixty-north.com/c/t.txt')
    new_paragraph = []
    for line in paragraph:
        line_letters = line.decode('utf-8').split()
        for letter in line_letters:
            new_paragraph.append(letter)
    paragraph.close()

    for word in new_paragraph:
        print(word)

if __name__ == ' __main__':
    fetch_story()