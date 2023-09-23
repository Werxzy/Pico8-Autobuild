@REM replace name of game and file location of pico8
set name=1k_car
set pico8="C:\Program Files (x86)\PICO-8\pico8.exe"

@REM export to html
%pico8% ..\%name%.p8 -export "-f %name%.html"

@REM fix formatting
python process_web_version.py

@REM zip it
"C:\Program Files (x86)\WinRAR\WinRAR.exe" a -afzip "%name% html.zip" %name%_html\index.html %name%_html\%name%.js

@REM export cart
%pico8% ..\%name%.p8 -export "%name%.p8.png"

@REM export binary versions and the cart
%pico8% ..\%name%.p8 -export "%name%.bin"

timeout 3
