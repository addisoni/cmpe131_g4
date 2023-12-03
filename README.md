<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/notetastic_logo.png" alt="Logo" width="250" height="250">
  </a>
</div>

<p align="center"> 
Addison Ivan (@addisoni) (Team Lead) <br> 
Benjamin Lim (@KatsumiLeaf) <br>
Najm Masri (@najm-masri) <br>
Stephen Shao (@stephen-shao)
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation-and-running">Installation and running</a></li>
      </ul>
    </li>
    <li><a href="#user-account-functions">User Account Functions</a></li>
      <ul>
        <li><a href="#creating-a-new-account">Creating a new account</a></li>
        <li><a href="#logging-in">Logging in</a></li>
        <li><a href="#logging-out">Logging out</a></li>
        <li><a href="#forgot-password">Forgot password</a></li>
        <li><a href="#modify-account-details">Modify account details</a></li>
      </ul>
    <li><a href="#notes-functions">Notes Functions</li>
      <li><a href="#creating-notes">Creating notes</a></li>
      <li><a href="#adding-different-typefaces-and-font-styles">Adding different typesfaces and font styles</a></li>
      <li><a href="#searching-for-notes">Searching for notes</a></li>
      <li><a href="#sorting-notes">Sorting notes</a></li>
    <li><a href="#functional-requirements-to-date">Functional Requirements (To-Date)</li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Notetastic is a web-based note taking app that utilizies Flask-Login, Flask-SQLAlchemy, Flask-WTF, and various other
extensions to provide the user with an easy and simple way to save their thoughts and ideas online. As a user, you will
be able to do basic things such as creating your own personal account, creating and modifying your notes with different 
typefaces and font styles, have the ability to share them to the public or keep it private, and so much more!

### Built With:
* [![Flask][Flask.com]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- General Instructions -->
## User Account Functions
### Creating a new account
1. Click on "**Create Account**" tab in the menu bar

2. Now enter your account details 
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/createaccount_2.png" alt="Logo" width="415" height="361">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Logging in
1. After creating your new account, you'll be sent to our login page where you enter your account details then click "Sign in" to login to your account
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/login.png" alt="Logo" width="317" height="331">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Logging out
1. Click on the "**Logout**" tab in the menu bar to logout of your current session

2. Puts you back onto to the login page when you're successfully logged out
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/logout_2.png" alt="Logo" width="293" height="327">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Forgot password
1. Click on "**Forgot Password**" tab in the menu bar

2. Enter the username and the correct security answer associated with it
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/Forgot_Password_Site.png" alt="Logo" width="946" height="460">
  </a>
</div>

3. Once successful, you will be redirected to the "**Reset Password**" page where you can create a new password which will replace your current one
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/Reset_Password_Site.png" alt="Logo" width="946" height="460">
  </a>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Modify account details
1. In the menu bar, click on the "**Modify Account**" tab

2. Enter the user information you want to change, i.e. username, password, security question/answer then click the "**Modify Account**" button to implement those changes to your account
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/modifyaccountdetails.png" alt="Logo" width="946" height="390">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Notes Functions

### Creating notes
1. After logging in, you will be redirected to the notes creation page where you can create new notes
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/notePage.png" alt="Logo" width="1051" height="452">
  </a>
</div>

2. To save the note after inputting the title and body, click on "**Save Note**"

3. After saving, you will be redirected to the home page where you can view, delete, modify, or change the note's visibility to other users.

4. To create another new note, click the "**Notes**" tab on the menu bar and do the same thing as mentioned in step 2
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Adding different typefaces and font styles
1. You can modify your text with different typefaces and font styles using the buttons under '**Body**'
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/typefaces and font styles.png" alt="Logo" width="1005" height="526">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Searching for notes
1. Navigate to the menu bar and click on the "**Search**" tab

2. You can search for notes containing the title or body that you inputted as shown below
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/searchBar.png" alt="Logo" width="200" height="511">
    <img src="images/readme/searchResult.png" alt="Logo" width="430" height="511">
    <img src="images/readme/noteContents.png" alt="Logo" width="430" height="426">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Sorting notes
1. If you aren't already on it, click on the "**Home**" tab on top
   
2. Here, you can sort by the title ascending/descending or by date created
<div align="center">
  <a href="https://github.com/addisoni/cmpe131_g4">
    <img src="images/readme/noteSort.png" alt="Logo" width="630" height="533">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Implementation -->
## Functional Requirements (To-Date)

1. Notes created on webpage are restricted to corresponding user and can change visiblity based on user's selection **(Benjamin Lim)** 

2. A simple user registration web page is incorporated for new users to create their personalized account with a username and password and security question (password reset) **(Benjamin Lim)** 

3. Logout of user account **(Benjamin Lim)**
   
4. Create new notes **(Addison Ivan)**

5. Forgotten passwords can be reset using stored security question or known password **(Stephen Shao)**

6. Multipletypefaces and font styles **(Najm Masri)**

7. Modify existing user account details **(Najm Masri)**
    
8. Multiple note sorting options **(Addison Ivan)**

9. Search field for notes list **(Addison Ivan)**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Flask.com]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
