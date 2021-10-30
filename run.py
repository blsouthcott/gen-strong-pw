

import string
import random

import PySimpleGUI as sg


def gen_strong_password(length=18):
    
    num_chars = length
    #num_chars = random.randint(14, 18)
    char_count = num_chars
    
    num_punctuation = random.randint(1,3)
    punctuation = "".join([random.choice(
        ("!", "$", "(", ")", "%", "&", "[", "]", ":", ";", "~", "?")
                                        ) for _ in range(num_punctuation)])
    char_count -= num_punctuation
    
    num_nums = random.randint(1,4)
    ints = [i for i in range(10)]
    nums = "".join([str(random.choice(ints)) for _ in range(num_nums)])
    char_count -= num_nums
    
    num_upper_letters = random.randint(3,5)
    upper_letters = "".join([random.choice(string.ascii_uppercase) for _ in range(num_upper_letters)])
    char_count -= num_upper_letters
    
    num_lower_letters = char_count
    lower_letters = "".join([random.choice(string.ascii_lowercase) for _ in range(num_lower_letters)])
    
    chars = punctuation + nums + upper_letters + lower_letters
    strong_password = ""
    
    for char in range(num_chars):
        rand_int = random.randint(0, len(chars) - 1)
        strong_password += chars[rand_int]
        left_half = chars[:rand_int]
        right_half = chars[rand_int + 1:]
        chars = left_half + right_half
        
    return strong_password
            

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