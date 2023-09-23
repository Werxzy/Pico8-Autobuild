@REM export to html
"C:\Program Files (x86)\PICO-8\pico8.exe" ..\1k_car.p8 -export "-f 1k_car.html"

@REM fix content of web version
@REM (1k_car, 16, 22222200) = (project name, top margin, background color)
python process_web_version.py 1k_car 16 22222200

@REM zip web files for itch.io page
"C:\Program Files (x86)\WinRAR\WinRAR.exe" a -afzip "1k_car_html.zip" 1k_car_html\index.html 1k_car_html\1k_car.js

timeout 3
