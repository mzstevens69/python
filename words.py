from urllib.request import urlopen

def fetch_story():
    paragraph = urlopen('https://sixty-north.com/c/t.txt')
    new_paragraph = []
    for line in paragraph:
        line_letters = line.decode('utf-8').split()
        for letter in line_letters:
            new_paragraph.append(letter)
    paragraph.close()
    return paragraph

def print_paragraph(new_paragraph):
    for word in new_paragraph:
        print(word)

def main():
    words = fetch_story()
    print_paragraph(words)


if __name__ == ' __main__':
    main()