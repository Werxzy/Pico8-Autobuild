import sys

filename = sys.argv[1]+"_html\\index.html"
with open(filename) as f:
    s = f.read()

# replaces a range of text with some searching
# great for replacing ambiguous text
# the searched text (after, start, end) should either be unique or the first instance after the previous(or start).
def find_replace(s:"str", after, start, replace, end):
    # find the first instance of "after"
    first = s.find(after) + len(after)
    
    # find the range that needs to be replaced
    i0 = s.find(start, first) + len(start)
    i1 = s.find(end, i0)
    
    # replace the found section
    return s[:i0] + str(replace) + s[i1:]

# example
# a = '... .p8_start_button{ background:url("blah blah 09872345") ... }'
# a = find_repalce(a, '.p8_start_button{', 'background:url("', 'embed.png', '")')
# assert(a == '.p8_start_button{ background:url("embed.png") }')


def margin_top(s:"str", y):
    # add upper margin after running
    s = s.replace(
        'var margin_top = 0;', 
        'var margin_top = '+str(y)+';'
    )

    # add upper margin before running
    s = find_replace(s, 'id="p8_start_button"',
        'flex;', ' margin-top:'+str(y)+'px', '">'
    )
    # s = s.replace(
    #     '<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex;">',
    #     '<div id="p8_start_button" class="p8_start_button" style="width:100%; height:100%; display:flex; margin-top:'+str(y)+'px">'
    # )
    return s

s = margin_top(s, 24)



# adds extra info to the body for the background image
s = find_replace(s, '<body',
    'margin:0px;',
    'background-image: url(\'embed.png\'); background-size: 960px 960px; image-rendering: pixelated; background-repeat: no-repeat; background-position: top;',
    '">'            
)
# s = s.replace(
#     '<body style="padding:0px; margin:0px; background-color:#222; color:#ccc">',
#     # '<body style="padding:0px; margin:0px; background-image: url(\'embed.png\'); background-size: 960px 960px; image-rendering: -moz-crisp-edges;">'
#     '<body style="padding:0px; margin:0px; background-image: url(\'embed.png\'); background-size: 960px 960px; image-rendering: -moz-crisp-edges; background-repeat: no-repeat; background-position: top;">'
# )

# # make original border transparent
# s = s.replace(
#     '222', 
#     '00000000'
# )


# force size if 512 or greater
# ignore if fullscreen
s = s.replace(
    'csize = (csize+1) & ~0x7f;', 
    'csize = is_fullscreen ? (csize+1) & ~0x7f : 512;'
)

# replaces starting image
s = find_replace(s, '.p8_start_button{',
    'background:url("',
    'start.png',
    '")'
)

# makes starting image pixelated
s = find_replace(s, '.p8_start_button{',
    '',
    '\n\timage-rendering: pixelated;',
    ''
)

# replaces play button
s = find_replace(s, '<div id="p8_start_button"',
    '>',
    '<img width=80 height=80 style="margin:auto;" src="play.png"/>',
    '</div>'
)

# Adjust positioning of menu buttons
s = find_replace(s, '<div class=p8_menu_buttons',
    'margin-left:',
    '140px',
    ';'
)

with open(filename, 'w') as f:
    f.write(s)