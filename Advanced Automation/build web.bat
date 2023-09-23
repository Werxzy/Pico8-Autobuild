set "name=1k_car"

@REM shrink and export minified version
@REM X:\shrinko8\shrinko8 %name%.p8 %name%_mini.p8 --minify-safe-only --script add_comment.py

@REM export to html
@REM "C:\Program Files (x86)\PICO-8\pico8.exe" %name%_mini.p8 -export "-f %name%.html"
"C:\Program Files (x86)\PICO-8\pico8.exe" ..\%name%.p8 -export "-f %name%.html"

@REM fix formatting and colors
python process_web_version.py %name%

@REM zip it
"C:\Program Files (x86)\WinRAR\WinRAR.exe" a -afzip ".\%name%_html.zip" %name%_html

timeout 3
