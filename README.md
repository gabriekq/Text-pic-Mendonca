# Text-pic-Mendonca

# Introduction 

This Project is part of the SpringMVC-Api-Mendonca – Beta 2 (https://github.com/gabriekq/SpringMVC-Api-Mendonca).
The Text-pic-Mendonca takes a resume’s picture and transforms it to text format than create an (.txt) file with the name of the picture.
# How is it work
1 – The app connects to a MySQL database to get the picture’s path and letter load it.

2 – After, load the picture. The script applies OCR in the picture in other to get the text.

3 – Once the text is ready, the Algorithm uses the name found in the database and save as (TXT) format into another folder in the system.

4- Finally the picture file is deleted, picture and the row in the database as well.
