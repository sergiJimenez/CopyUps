     _____                                    __  __                  __         _____       
    /\  _` \                                 /\ \/\ \                /\ \       /\  __`\     
    \ \ \/\_\    ___   _____   __  __        \ \ \ \ \  _____     ___\ \ \     _\ \ \/\ \    
     \ \ \/_/_  / __`\/\ '__`\/\ \/\ \  ______\ \ \ \ \/\ '__`\  /',__\ \ \   /\_\ \ \ \ \   
      \ \ \L\ \/\ \L\ \ \ \L\ \ \ \_\ \/\______\ \ \_\ \ \ \L\ \/\__, `\ \_\  \/_/\ \ \_\ \  
       \ \____/\ \____/\ \ ,__/\/`____ \/______/\ \_____\ \ ,__/\/\____/\/\_\   /\_\ \_____\ 
        \/___/  \/___/  \ \ \/  `/___/> \        \/_____/\ \ \/  \/___/  \/_/   \/_/\/_____/ 
                         \ \_\     /\___/                 \ \_\                              
                          \/_/     \/__/                   \/_/                              

## Description

Copy-Ups! :O is a CLI developed in Python whose purpose is to clone one or multiple repositories. One of the functions that it has when you select either of the two features that this CLI gives you is the fact that if it finds a repository with the same name, it will delete that repository in order not to have copies of it.

## Requirements

In order to use it you need to install Python in any version. To check if you have it installed you just have to execute the following command:

```powershell
python --version
```

A **VERY IMPORTANT** aspect to take into account is the fact that deleting directories through a terminal requires the use of a superuser (sudo), so we must run the program as administrators on Windows or use the `sudo su` command on Linux/Unix.

## Installation

To install this repository you only need to clone it, as all the packages needed to use it will be installed the first time you run it.

## Use

To use it, we will have to go inside it with a terminal and execute the command:

```powershell
python .\main.py
# or
python3 main.py
```

If this is the first time we run it, we will see that the necessary packages are installed in order to be able to use it. Once they are finished, you can choose any of the options in the menu.

## Functionalities

- Clone a repository: this functionality allows us to clone the repository that we indicate. The first thing it will ask us for is the URL of the repository that we will have to write, or paste. And, finally, it will ask us for the path where we want to host the repository. If the repository already exists in the path we have previously indicated, it will delete it and clone the new one.
- Clone multiple repositories: this functionality is similar to the previous one but requires a previous preparation. To use this functionality we will have to use a code editor, or a text editor, and open the file "multiple_repositories.py". In the string array called `repo_urls` we will add all the URL's of the repositories we want to clone and in the string variable `base_path` we will include the path where we want them to be copied.
It is highly recommended to leave the "`r`" in front of the double quotes where we will introduce the path where we will host the repositories as this is in charge of formatting the paths in Windows as they use a backslash.

**IT IS IMPORTANT TO NOTE THAT PRIVATE REPOSITORIES WILL ASK FOR YOUR GITHUB USERNAME AND PASSWORD.**