## Background Context
### Welcome to the AirBnB clone project!

#### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

-Create a new object (ex: a new User or a new Place)
-Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Enderstand command line interpreter 🤔

### How to Start a Command Interpreter ?

#### 1. Access the Terminal/Command Prompt
- On Windows, you can open the Command Prompt by searching for "cmd" or "Command Prompt" in the Start menu.
- On macOS, open the Terminal application, typically found in the "Utilities" folder within the "Applications" directory.
- On Linux, you can access the command-line interface by opening the Terminal application or using keyboard shortcuts (e.g., Ctrl+Alt+T). 

#### 2. Login
- If required, you may need to log in with a username and password, depending on your system configuration.

#### 3. Choose a Shell
- In most cases, the default shell (e.g., Bash on Linux, Command Prompt on Windows) will start automatically. You can also switch to different shells if installed (e.g., Zsh)

### How to Use a Command Interpreter ?
Once you have the command interpreter open, you can start issuing commands. Here are some basic commands and how to use them.

#### Navigating the File System
- **cd** /path/to/directory
- **ls** (List files and directories in the current directory) 
...
#### Manipulating Files and Directories
- **mkdir** myDirectoryName (Create a new directory)
- **touch** my_file.extensionOrNot (To create a file)
- **rm** my_bad_file.txt (Delete a file)
- **rm** -r directoryName (Remove a directory with all childs)
 
#### Running Programs
ou can run programs and scripts by typing their names. For example, to run a Python script:
- python my_best_script.py

#### Piping and Redirection
ou can use | to pipe the output of one command as input to another. For example, to search for a specific term in a file:
- **cat** my_file.txt | grep "search_term"

You can redirect output to a file using `>`
- **ls** > file_list.txt

#### Viewing Files
You can use commands like cat, more, or less to view the contents of a text file:
- **cat** my_file.txt


Have happy learning 🚀 <br>
Alban Okoby 🐱‍👤
