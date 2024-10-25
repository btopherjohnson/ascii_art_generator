# ascii_art_generator

A quick-n-dirty ascii art generator I made during a boring class in college.

| File                      | Description   |
|---------------------------|---------------|
| [cool_ascii](cool_ascii)  | Cool images I have saved |
| [imgs](imgs)              | Images used for samples  |
| ascii.py                  | Uses the brightness of each point to draw a pixel |
| ascii_gradient.py         | Finds the gradient using numpy then draws a line perpendicular to the gradient: / \| \\ - |
| ascii_gradient_fill.py    | Same as above, but fills in the space between the lines |
| ascii_gradient_canny.py   | First finds edges using a canny edge detector, then uses the same gradient algorithm to draw a line |

All of the scripts are called like this:\
`python3 ./ascii.py img.jpg`\
They will leave a text file in the directory you call it from.

Most of these work best with BIG resulting text files, but I have had luck with some smaller ones.
You can scale it by finding the ASCII_WIDTH variable and changing it.
