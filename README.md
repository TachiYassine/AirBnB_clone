# AirBnB Clone [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/luischaparroc/AirBnB_clone/blob/master/LICENSE) [![Build Status](https://travis-ci.org/luischaparroc/AirBnB_clone.svg?branch=master)](https://travis-ci.org/luischaparroc/AirBnB_clone)
![HBnB Logo](./image/hbnb_logo.png)


### Contents

- [Description](#Description)
- [Environment & Tools](#Environment-&-Tools)
- [Installation](#Installation)
- [Execution](#Execution)
- [Testing](#Testing)
- [Authors](#Authors)

## Description :page_facing_up:
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy the existing classes and subclasses.
This first step is very important because we will be using what we  build during this part of the project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

This multi-part phase will help us to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Environment & Tools :computer:
The console was developed in Ubuntu 14.04LTS using python3 (version 3.4.3).
<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a><!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>

## Installation :hammer_and_wrench:

1.  Clone this GitHub repository to your local machine.

`git clone https://github.com/...../AirBnB-Clone.git`

2.  Navigate to the project directory.

`cd AirBnB-Clone` 

3.  Execute the console.

`./console.py`

## Execution

The shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

## Testing

To fill later

## Authors

-   [BOUJIR Imane](https://github.com/Imane-Bjr)
-   [TACHI Yassine](https://github.com/TachiYassine)
