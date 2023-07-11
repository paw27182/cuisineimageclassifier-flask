# cuisine-image-classifier

# 1. What you can do

* To predict which class an image belong to by using the pre-trained model.<br>
  The classification class consist of "salad", "sushi" and "tofu".

* (CAUTION) This repository is for beginners' learning.  The precision of the model is not so good.

<br>

# 2. How to use

* Environment setting
  * Edit settings.py
    * PYTHON_EXE_FILE 

<br>

* Program start
  * cd cuisineimageclassifier-flask
  * python.exe app.py

<br>

* Open browser
  * http://localhost:8000/
  * Submit an image: ./uisineimageclassifier-flask/tests/salad.jpg


<br>

# 3. System
* OS: Windows 10, Ubuntu 20.04.6 LTS
* Web Framework: Flask
* Python 3.10.11
* Python Libraries: Flask matplotlib numpy Pillow requests tensorflow
* Bootstrap 5.2.3
* jQuery 3.7.0

<br>

# 4. Directories and Files Overview

| Directory/File |D/F| description |
| :------------- | :-| :---------- |
| execute | Dir | predict program directory |
| execute/model | Dir | Machine learning model |
| execute/static | Dir | html, javascript files |
| execute/template | Dir | html files |
| execute/command.py | File | Machine learning predict program |
| execute/execute.py | File | dispatcher |
| static | Dir | css, javascript files |
| templates | Dir | layout.html |
| tests | Dir | test image files |
| topview | Dir ||
| app.py  | File | start program |
| READMD.md | File ||
| requirements.txt | File | prerequisite libraries |
| setting.py | File ||
