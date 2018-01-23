# Movie Trailer Website

 - This is a movie trailer website the lets you preview your favourite movies' covers and trailers

---
### Installation

 - This project is made in Python programming language.

 - This project uses "The Movie Database" API V3 through a python wrapper called tmdbsimple.

   ```
   pip install tmdbsimple
   ```

 - You can register an account at "The Movie Database" website to get your API_KEY
and update that field in ```entertainment_center```

   ```
   api_key = ""
   ```
---
### Usage


This project has two modes:

 - You can write your own movies' titles to a text file and provide its path as argument.
 - Or you can just leave it blank and we will show you some of our picks!
 
To run it you have two options:

 - Use ```python entertainment_center.py some_file_path.txt``` to generate movies using your own movies' titles.
 - Use ```python entertainment_center.py``` to generate an HTML with our picks.

---
### Contributors

 - amrgamalmohammed