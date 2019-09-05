import time as t
import pyautogui as p


CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '!': '–--.', '?': '..--..', '\'': '.----.',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '}


def dot(dot):
    p.keyDown('enter', dot)
    p.keyUp('enter')


def dash(dash):
    p.keyDown('enter', dash)
    p.keyUp('enter')


def space0(TBPOC):  # Time Between Parts of Character = x
    t.sleep(TBPOC)


def space1(TBC):  # Time Between Character = 3x
    t.sleep(TBC)


def space2(TBW):  # Time Between Words = 7x
    t.sleep(TBW)


wpm = int(input("Speed (WPM): "))
T = (12/wpm)/10
while True:
    msg = input('Text to write: ')
    t.sleep(3)
    for char in msg:
        a = CODE[char.upper()]
        for i in a:
            if i == '.':
                dot(T)
                space0(T)
            elif i == ' ':
                space2(7*T)
            else:
                dash(3*T)
                space0(T)
        space1(3*T)
