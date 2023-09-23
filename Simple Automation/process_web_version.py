import sys

# Get filename
filename = sys.argv[1]+"_html\\index.html"
# filename = "1k_car_html\\index.html"
with open(filename) as f:
    s = f.read()


# Adjust upper margin to fit image.
margin = sys.argv[2]
# margin = 0

s = s.replace(
    'var margin_top = 0;', 
    f'var margin_top = {margin};'
)

s = s.replace(
    '<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex;">',
    f'<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex; margin-top:{margin}px">'
)

# Make original border transparent or replace with different color.
s = s.replace(
    '222', 
    sys.argv[3]
    # '22222200'
)

# Save changes
with open(filename, 'w') as f:
    f.write(s)