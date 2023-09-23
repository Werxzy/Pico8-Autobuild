@REM replace name of game and file locations where necessary
set name=1k_car
set pico8="C:\Program Files (x86)\PICO-8\pico8.exe"
set margin=16
set color=22222200

@REM export to html
%pico8% ..\%name%.p8 -export "-f %name%.html"
@REM "C:\Program Files (x86)\PICO-8\pico8.exe" ..\1k_car.p8 -export "-f 1k_car.html"

@REM fix content of web version
python process_web_version.py %name% %margin% %color%
@REM python process_web_version.py 1k_car 16 22222200

@REM zip web files for itch.io page
"C:\Program Files (x86)\WinRAR\WinRAR.exe" a -afzip "%name%_html.zip" %name%_html\index.html %name%_html\%name%.js
@REM "C:\Program Files (x86)\WinRAR\WinRAR.exe" a -afzip "1k_car_html.zip" 1k_car_html\index.html 1k_car_html\1k_car.js

@REM export cart
%pico8% ..\%name%.p8 -export "%name%.p8.png"
@REM "C:\Program Files (x86)\PICO-8\pico8.exe" ..\1k_car.p8 -export "1k_car.p8.png"

@REM export binary versions and the cart
%pico8% ..\%name%.p8 -export "%name%.bin"
@REM "C:\Program Files (x86)\PICO-8\pico8.exe" ..\1k_car.p8 -export "1k_car.bin"

timeout 3
