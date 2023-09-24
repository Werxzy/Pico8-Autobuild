The advanced files use a the find_replace function to help replace the right bit of text.  
There are some cases that are dependant on the files used to export from Pico-8, which then can't simply be changed using Python's replace function.
We instead search from a starting point and then a start and end range, where everything inside the range gets replaced.

For instance, the data for starting image for the web version is stored inside the html file.  
To replace it, we can search for `.p8_start_button` where the image data is stored, and use a range from `background:url("` to `")` to ensure the link to the new image remains inside the double quotes.

```python
s = find_replace(s, '.p8_start_button{',
    'background:url("',
    'start.png',
    '")'
)
```

These replacement methods are more about building a list of ways to customize the web page quickly and then use them for future projects.
