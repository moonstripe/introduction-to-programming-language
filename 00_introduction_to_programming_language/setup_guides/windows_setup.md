# Windows Setup Guide

*Time required: 20-30 mins*

This guide will walk you through the installation of all the necessary software, as well as provide a quickstart guide to running Python scripts.

## Installing `Python`

1. Download [`Python 3.11`](https://python.org/downloads/release/python-3111/) by clicking the "Windows installer (64-bit)" link under Files.

2. Open the installer from your Downloads, and click "Install"

3. Once `Python 3.11` has been downloaded, confirm that you have successfully downloaded `Python 3.11` by opening the built-in application `Windows PowerShell` and typing the following command:
    ```bash
    python --version
    ```

4. If you're having issues, try downloading `Python 3.11` from the Microsoft Store.

## Installing `Git`

`Git` is a tool used by software engineers to manage version control. Think of it as a way of viewing the history of a codebase. We will be using `Git` to download the prepared examples and coursework for the class.

1. Download [Git for Windows](https://gitforwindows.org/index.html) by clicking the blue "Download" button.

2. Open the Installer that was just downloaded, and follow the instructions:
   - Many of the steps allow you to customize your installation. You can click "Next" through all of the steps.
     - In the aftermath of the George Floyd protests in 2020, `Git` decided to allow users to change the name of their primary branch from "master" to "main". This setting can be set after the "default editor" settings page and before the "adjusting PATH" setting page.

3. Open the built-in application called `Windows PowerShell`.
   
4. Type the following command: 
    ```bash
    git --version
    ```
5. If you see a version number and the command does not fail, you have successfully installed `Git`.

## Installing `VSCode`

`VSCode` is probably the most popular beginner (and professional) code editor out there right now. We'll be writing our scripts in this program.

1. Download [VSCode for Windows](https://code.visualstudio.com/) by clicking the blue "Download for Windows" button

2. Open the installer, and follow the instructions
    - No controversy here, just smashing the "Next" button

3. Open up `VSCode`.
   
4. On the leftmost part of the `VSCode` window, there is a long column of icons. Click the icon that has three blocks attached to each other and another block floating to the top right.

5. In the search bar at the top of the Extensions window, search for `Pylance`, and install it.
   - `Pylance` helps us write better code by letting us know where the code might fail when we run it. 


## Downloading the coursework

With `Git` and `VSCode` installed, we can now import our coursework. 

1. Open `Windows PowerShell`
2. Confirm that you have both `Git` and `VSCode` installed with the shell command enabled:
    - `Git`: 
    ```bash
    git --version
    ```
    The output should show a version number.

    - `VSCode`: 
    ```bash
    code --version
    ```
    The output should show a version number and some other miscellaneous information.
3. Make sure your in your root directory with the following command:
    ```bash
    pwd
    ```
    The output should read something like: `Directory: C:\Users\[your-username] ...`
    - If it does not, try this command:
        ```bash
        cd ~
        ```

4. Copy and paste the following command:
    ```bash
    git clone https://github.com/moonstripe/introduction-to-programming-language.git
    ```
    The output should show that something is being downloaded to your machine.

5. Verify that the `git clone` worked by listing out the coursework directory:
    ```bash
    ls introduction-to-programming-language
    ```
    The output should include lessons whose name starts with a 0 and a number. 

6. Change directories to the newly downloaded folder, `introduction-to-programming-language\`.
    ```bash
    cd .\introduction-to-programming-language\
    ```

7. Then, change directories to the `00_introduction_to_programming_language\`.
    ```bash
    cd .\00_introduction_to_programming_language\
    ```

8. Verify that you're in the correct directory:
    ```bash
    ls
    ```
    The output should show one markdown file with the same name as the directory, and `test_script.py`

## Virtual Environments

This is going to be a standard practice as we move through the course. Virtual environments allow us to only import the required materials to our program, avoiding the bloat of unused packages.

1. In `Terminal`, change directories to `00_introduction_to_programming_language/`
    ```bash
    cd ~
    cd introduction-to-programming-language/00_introduction_to_programming_language/
    ```
    The result of `ls` should show the contents of the first lesson, including `test_script.py`

2. Open VSCode from the command line.
    ```bash
    code .
    ```
3. In `VSCode`, find the "Terminal" menu in the upper menu bar, and open a "New Terminal"
   - This should open `VSCode` to our directory

4. In the "Terminal" section that opened up at the bottom of your screen, type the following command:
    ```bash
    python3 -m venv env
    ```
    This will take a moment to run. If you click the file icon in the left-most column of `VSCode`, you should see a new `env/` directory.
5. To activate the environment you just initialized, type the following command:
    ```bash
    .\env\Scripts\Activate.ps1
    ```

## Run you first Python command!

1. With your virtual environment activated, type the following in the "Terminal" Section of VSCode:
    ```bash
    python test_script.py
    ```
    This should output "Adding one to two: 3"

2. Deactivate your virtual environment with the following command:

    ```bash
    deactivate
    ```

3. Congratulations, you've taken your first major steps to being a Python developer!