filename = "1k_car_html\\index.html"
with open(filename) as f:
    s = f.read()

margin = 0

# add upper margin after running
s = s.replace(
    'var margin_top = 0;', 
    f'var margin_top = {margin};'
)

# make original border transparent
s = s.replace(
    '222', 
    '22222200'
)

# add upper margin before running
s = s.replace(
    '<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex;">',
    f'<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex; margin-top:{margin}px">'
)

with open(filename, 'w') as f:
    f.write(s)