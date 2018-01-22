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

To use this project just import ```entertainment_center``` and create a class instance

```
import entertainment_center
center = entertainment_center.EntertainmentCenter(optional_path)
```

This project has two modes:

 - You can write your own movies' titles to a text file and provide its path to the constructor.
 - Or you can just leave it blank and we will show you some of our picks!

---
### Contributors

 - amrgamalmohammed