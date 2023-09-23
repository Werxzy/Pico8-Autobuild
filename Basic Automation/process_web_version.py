import sys

# Get filename
filename = sys.argv[1]+"_html\\index.html"
# filename = "1k_car_html\\index.html"
with open(filename) as f:
    s = f.read()


# Make original border transparent or replace with different color.
s = s.replace(
    '#222', 
    f'#{sys.argv[2]}'
    # '#00000000'
)

if len(sys.argv) > 3:
    # Adjust upper margin to fit image.
    margin = sys.argv[3]
    # margin = 16

    s = s.replace(
        'var margin_top = 0;', 
        f'var margin_top = {margin};'
    )

    s = s.replace(
        '<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex;">',
        f'<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex; margin-top:{margin}px">'
    )


# Save changes
with open(filename, 'w') as f:
    f.write(s)
