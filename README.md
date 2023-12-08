# Notetastic
[//]: # (PROJECT LOGO)
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/notetastic_logo.png" alt="Logo" width="250" height="250">
</p>

<p align="center"> 
Addison Ivan (@addisoni) (Team Lead) <br> 
Benjamin Lim (@KatsumiLeaf) <br>
Najm Masri (@najm-masri) <br>
Stephen Shao (@stephen-shao)
</p>

[//]: # (TABLE OF CONTENTS)
<details>
  <summary>Table of Contents</summary>
  
  1. [About The Project](#about-the-project)
     - [Built With](#built-with)
  2. [Getting Started](#getting-started)
     - [Prerequisites](#prerequisites)
     - [Installation and running](#installation-and-running)
  3. [User Account Functions](#user-account-functions)
     - [Creating a new account](#creating-a-new-account)
     - [Logging in](#logging-in)
     - [Logging out](#logging-out)
     - [Forgot password](#forgot-password)
     - [Modify account details](#modify-account-details)
  4. [Notes Functions](#notes-functions)
     - [Creating notes](#creating-notes)
     - [Searching for notes](#searching-for-notes)
     - [Sorting notes](#sorting-notes)
     - [Adding different typefaces and font styles](#adding-different-typefaces-and-font-styles)
     - [Creating a table](#creating-tables)
     - [Duplicate Note(s)](#duplicate-notes)
     - [Creating Folders](#user-is-able-to-create-folders-to-organize-notes)
     - [Private/Public Visibility](#notes-created-on-webpage-are-restricted-to-the-corresponding-user-and-can-change-visibility-based-on-users-selection)
     - [View and Undo/Redo revision history](#view-revision-history-from-past-savestate-and-undoredo-revision-history-restore-previous-note-savestate)
  5. [Functional Requirements (To-Date)](#functional-requirements-to-date)
</details>

[//]: # (ABOUT THE PROJECT)
## About The Project

Notetastic is a web-based note taking app that utilizies Flask-Login, Flask-SQLAlchemy, Flask-WTF, and various other
extensions to provide the user with an easy and simple way to save their thoughts and ideas online. As a user, you will
be able to do basic things such as creating your own personal account, creating and modifying your notes with different 
typefaces and font styles, have the ability to share them to the public or keep it private, and so much more!

Video Tutorial How to use Notetastic: https://drive.google.com/file/d/1srhB_0Yp-0xZQ47ax78GgxKB7mD-YTg-/view?usp=sharing

### Built With:
* [![Flask][Flask.com]][Flask-url]
  
[back to top](#notetastic)

[//]: # (GETTING STARTED)
## Getting Started

### Prerequisites
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)

Make sure you have the following libraries installed before running Notetastic:<br>
(Run these commands in the terminal)
* Refer to and download the [Requirements](https://github.com/addisoni/cmpe131_g4/blob/main/requirements3.txt) file then install using the pip3 command:
  ```sh
  pip3 install -r requirements3.txt
  ```

* Alternatively
  ```sh
  pip3 install flask-login flask-sqlalchemy flask-wtf
  ```
  
### Installation and running

1. Clone the repo
   ```sh
   git clone https://github.com/addisoni/cmpe131_g4
   ```
2. Access the app project
   ```sh
   cd cmpe131_g4
   ```
3. Running the website within flask
   ```sh
   flask run
   ```

Alternatively, running the website via python
   ```sh
   python3 run.py
   ```

[back to top](#notetastic)

[//]: # (GENERAL INSTRUCTIONS)
## User Account Functions
### Creating a new account
1. Click on "**Create Account**" tab in the menu bar

2. Now enter your account details 
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/createaccount_2.png" alt="Logo" width="415" height="361">
</p>

[back to top](#notetastic)

### Logging in
1. After creating your new account, you'll be sent to our login page where you enter your account details then click "Sign in" to login to your account
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/login.png" alt="Logo" width="317" height="331">
</p>

[back to top](#notetastic)

### Logging out
1. Click on the "**Logout**" tab in the menu bar to logout of your current session

2. Puts you back onto to the login page when you're successfully logged out
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/logout_2.png" alt="Logo" width="293" height="327">
</p>

[back to top](#notetastic)

### Forgot password
1. Click on "**Forgot Password**" tab in the menu bar

2. Enter the username and the correct security answer associated with it
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/Forgot_Password_Site.png" alt="Logo"  
width="946" height="460">
</p>

3. Once successful, you will be redirected to the "**Reset Password**" page where you can create a new password which will replace your current one
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/Reset_Password_Site.png" alt="Logo" width="946" height="460">
</p>

[back to top](#notetastic)

### Modify account details
1. In the menu bar, click on the "**Modify Account**" tab

2. Enter the user information you want to change, i.e. username, password, security question/answer then click the "**Modify Account**" button to implement those changes to your account
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/modifyaccountdetails.png" alt="Logo" width="946" height="390">
</p>

[back to top](#notetastic)

## Notes Functions

### Creating notes
1. After logging in, you will be redirected to the notes creation page where you can create new notes
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/createnotes.png" alt="Logo" width="1051" height="452">
</p>

2. To save the note after inputting the title and body, click on "**Save note**"

3. After saving, you will be redirected to the home page where you can view, delete, modify, or change the note's visibility to other users.

4. To create another new note, click the "**notes**" tab on the menu bar and do the same thing as mentioned in step 2

[back to top](#notetastic)

### Searching for notes
1. Navigate to the menu bar and click on the "**Search**" tab

2. You can search for notes containing the title or body that you inputted as shown below
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/searchBar.png" alt="Logo" width="200" height="511">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/searchResult.png" alt="Logo" width="430" height="511">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/noteContents.png" alt="Logo" width="430" height="426">
</p>

[back to top](#notetastic)

### Sorting notes
1. If you aren't already on it, click on the "**Home**" tab on top
   
2. Here, you can sort by the title ascending/descending or by date created
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/noteSort.png" alt="Logo" width="630" height="533">
</p>

[back to top](#notetastic)

### Adding different typefaces and font styles
1. You can modify your text with different typefaces and font styles using the buttons under '**Body**'
<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/typefaces%20and%20font%20styles.png" alt="Logo" width="805" height="326">
</p>

[back to top](#notetastic)

### Creating Tables
1. Users are able to create tables inside of the creating notes area.

2. Users would need to select "insert table" button

3. Users would then be presented a table in which is 2x2

4. The table cells are editable and will be saved once the user hits submit

<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/CreateTable.png" alt="Logo" width="1406" height="698">
</p>

[back to top](#notetastic)

### Duplicate Note(s)
1. Craeate a note and save it.
2. Click on Modify
3. From there you can edit your note then duplicate it
4. You can see the duplicated in your list of notes

<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/step1forDuplicateNote.png" alt="Logo" width="578" height="550">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/step2forDuplicateNote.png" alt="Logo" width="1406" height="698">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/duplicatedNote.png" alt="Logo" width="582" height="1066">
</p>

[back to top](#notetastic)

### View revision history from past savestate
1. Create a note and save it
2. Click on note history
3. From there you will be able to view the revision history

<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/noteHistory1.png" alt="Logo" width="918" height="898">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/noteHistory2.png" alt="Logo" width="972" height="870">
</p>

[back to top](#notetastic)

### User is able to create folders to organize notes
1. Click on the "Folder" tab on top to create a folder then type in your folder name
<p align="center">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/folderPage_1.png" alt="Logo" width="353" height="151">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/folderPage_2.png" alt="Logo" width="367" height="274">
</p>
2. To access the folder, press on the green button with your folder name on it
<p align="center">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/folderPage_6.png" alt="Logo" width="404" height="207">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/folderPage_3.png" alt="Logo" width="436" height="136">
</p>
3. When you're inside "Create Note", you choose what folder to send it to
<p align="center">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/folderPage_4.png" alt="Logo" width="291" height="178">
</p>
4. You can also do this on the "Home Page"
<p align="center">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/folderPage_5.png" alt="Logo" width="424" height="247">
</p>

[back to top](#notetastic)

### Notes created on webpage are restricted to the corresponding user and can change visibility based on user's selection
1. By clicking the "Make Public" or "Make Private" button, it will change the visibility of the note to be shown to all users or only to yourself
   <p align="center">
     <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/private-public.png" alt="Logo" width="238" height="243">
   </p>

[back to top](#notetastic)

### View revision history from past savestate and Undo/Redo revision history (restore previous note savestate)
1. After creating a note, modifying it, and saving it, click on the Note History button in Home to view it
2. Next click on restore last version and it will undo your revision

<p align="center"> 
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/undo1.png" alt="Logo" width="914" height="886">
  <img src="https://github.com/addisoni/cmpe131_g4/blob/main/images/readme/undo2.png" alt="Logo" width="812" height="858">
</p>

[back to top](#notetastic)


[//]: # (IMPLEMENTATION)
## Functional Requirements (To-Date)

1. Notes created on webpage are restricted to corresponding user and can change visiblity based on user's selection **(Benjamin Lim)**

2. A simple user registration web page is incorporated for new users to create their personalized account with a username and password and security question (password reset) **(Benjamin Lim)**

3. Logout of user account **(Benjamin Lim)**

4. Create new notes **(Addison Ivan)**

5. Insertable tables into notes **(Stephen Shao)**

6. Forgotten passwords can be reset using stored security question or known password **(Stephen Shao)**

7. Multiple typefaces and font styles **(Najm  Masri)**

8. User is able to create folders to organize notes **(Benjamin Lim)**

9. Duplicate note(s) **(Najm  Masri)**

10. Modify existing user account details **(Najm  Masri)**

11. View revision history from past savestate **(Addison Ivan)**

12. Undo/Redo revision history (restore previous note savestate) **(Addison Ivan)**

13. Multiple Note sorting options **(Addison Ivan)**

14. Search field for notes list **(Addison Ivan)**

[back to top](#notetastic)

[//]: # (LINKS AND IMAGES)
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Flask.com]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
