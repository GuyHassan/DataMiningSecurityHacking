# Data Mining Security Hacking Poject

The project focuses on data mining for in-depth search, the user chooses a link to a particular site that he wants to check.
The system will take the link it received and look for all of its html, css, js files.
and search for any comments in any of the files, if there is any comment that suggests the possibility of hacking (such as: password, user, ID, etc.)
The system can search in depth on the same link it received, the default is a search on the current site, but it is possible to search for other sites that are on the same site we received (as the amount of depth we want, of course, the more time the system runs, the more depth it wants).
Finally, the system will bring us all comments that suggest the possibility of hacking including the link from which the comment came.

**That's how the project looks**

![projectPicture](https://user-images.githubusercontent.com/33221427/76643819-7e637580-655e-11ea-8907-39875e0fe911.JPG)

**This is my personal site that I built in one of the courses,
I put into Html, Css, Js files that could imply hacking.
[Review Pesonal Site](https://guyhassan.github.io/Geo-Information-Project/)**

![projectVideo](https://user-images.githubusercontent.com/33221427/76643844-89b6a100-655e-11ea-9fe4-7edf48617db7.gif)
## Usage
The project was written in Python and Beautiful Soup Library, the GUI written in HTML, CSS , Javascript, the algorithm of searching is creating in the python code, and after the javascript read the data from a JSON file and display the data on our site.

All the data saved after in a local database work with SqlLite3 Libary.

## License
[SCE Collage](https://www.sce.ac.il/)
