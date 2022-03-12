
import string
import random
import argparse
from typing import Union, List

import PySimpleGUI as sg
import pyperclip


PUNCTUATION = ("!", "$", "(", ")", "%", "&", "[", "]", ":", ";", "~", "?")


def gen_rand_chars(num_chars: int, chars: Union[List, tuple, str]) -> str:
    return "".join(str(random.choice(chars)) for _ in range(num_chars))


def scramble(text: str) -> str:
    scrambled_text = ""
    for _ in text:
        rand_int = random.randint(0, len(text) - 1)
        scrambled_text += text[rand_int]
        left_half = text[:rand_int]
        right_half = text[rand_int + 1:]
        text = left_half + right_half
    return scrambled_text


def gen_strong_password(length: int) -> str:
    
    num_chars = length
    char_count = num_chars
    
    punctuation = gen_rand_chars(random.randint(1, 3), PUNCTUATION)
    char_count -= len(punctuation)
    
    nums = gen_rand_chars(random.randint(1, 4), [i for i in range(10)])
    char_count -= len(nums)
    
    upper_letters = gen_rand_chars(random.randint(3, 5), string.ascii_uppercase)
    char_count -= len(upper_letters)
    
    lower_letters = gen_rand_chars(char_count, string.ascii_lowercase)
    
    chars = punctuation + nums + upper_letters + lower_letters
    return scramble(chars)


def get_pw_len(val: int) -> int:
    return {0: 16, 1: 20, 2: 24, 3: 30, 4: 40}.get(val)


def run_popup_window(pw):

    popup_layout = [
        [sg.InputText(pw)],
        [sg.Button("Copy")]
    ]
    popup = sg.Window("New Password", popup_layout)
    while True:
        event, values = popup.read()
        if event in [sg.WIN_CLOSED, "Cancel"]:
            break
        elif event == "Copy":
            pyperclip.copy(popup_layout[0][0].get())
            sg.popup_timed("Your password is now copied to the clipboard")


def run_main_window():

    layout = [
        [sg.Text("Please choose a length for your password and then press 'Generate'.")],
        [sg.Radio("16", "radios"),
         sg.Radio("20", "radios", default=True),
         sg.Radio("24", "radios"),
         sg.Radio("30", "radios"),
         sg.Radio("40", "radios")],
        [sg.Button("Generate")]
    ]

    window = sg.Window("Strong Password Generator", layout)
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, "Cancel"]:
            break
        for val in values:
            if values.get(val):
                pw_len = get_pw_len(val)
                break
        pw = gen_strong_password(pw_len)
        run_popup_window(pw)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-gui", dest="gui", action="store_false", default=True)
    parser.add_argument("--copy", dest="copy", action="store_true", default=False)
    parser.add_argument("pw_len", type=int, nargs="?", default=20)
    args = parser.parse_args()

    if args.gui is False:
        pw = gen_strong_password(args.pw_len)
        if args.copy is True:
            pyperclip.copy(pw)
        print(pw)

    else:
        run_main_window()


if __name__ == "__main__":
    main()
