
#!/usr/bin/env python3


import string
import random
from typing import Union, List

import PySimpleGUI as sg


def gen_rand_chars(num_chars: int, chars: Union[List, tuple]) -> str:
    return "".join(str(random.choice(chars)) for _ in range(num_chars))


def scramble(text: str) -> str:
    scrambled_text = ""
    for char in text:
        rand_int = random.randint(0, len(text) - 1)
        scrambled_text += text[rand_int]
        left_half = text[:rand_int]
        right_half = text[rand_int + 1:]
        text = left_half + right_half
    return scrambled_text


def gen_strong_password(length: int=18) -> str:
    
    num_chars = length
    char_count = num_chars
    
    punctuation = gen_rand_chars(random.randint(1, 3), 
                    ("!", "$", "(", ")", "%", "&", "[", "]", ":", ";", "~", "?"))
    char_count -= len(punctuation)
    
    nums = gen_rand_chars(random.randint(1, 4), [i for i in range(10)])
    char_count -= len(nums)
    
    upper_letters = gen_rand_chars(random.randint(3, 5), string.ascii_uppercase)
    char_count -= len(upper_letters)
    
    lower_letters = gen_rand_chars(char_count, string.ascii_lowercase)
    
    chars = punctuation + nums + upper_letters + lower_letters
    return scramble(chars)
            

def run():
    
    layout = [
        [sg.Text("Please choose a length for your password and then press 'Generate'.")],
        [sg.Radio("14", "radios"), 
         sg.Radio("15", "radios"), 
         sg.Radio("16", "radios"), 
         sg.Radio("17", "radios"), 
         sg.Radio("18", "radios", default=True)],
        [sg.Button("Generate")]
    ]

    window = sg.Window("Strong Password Generator", layout)
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, 'Cancel']:
            break
        for val in values:
            if values.get(val):
                pw_len = val + 14
                break
        pw = gen_strong_password(pw_len)
        sg.popup_get_text("Here's your password!", default_text=pw)
   

if __name__ == "__main__":
    run()
    