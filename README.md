# gen-strong-pw
Generate strong passwords either through the GUI or run as a command line script.

## How to use this
`Git clone`  or download the zip file and extract. Then `cd` into your local directory and run:

`pip install --user .`

## Options

To use with the GUI just run:

`python -m gen_strong_pw`

To use on the command line run:

`python -m gen_strong_pw --no-gui`

To automatically copy the password to the clipboard run:

`python -m gen_strong_pw --no-gui --copy`

If no password length is specified, the password generated will be 20 characters long. To generate with a specific length, do so after specifying optional arguments:

`python -m gen_strong_pw --no-gui --copy 47`
