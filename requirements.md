## Functional Requirements

### Benjamin
- Notes created on webpage are restricted to the corresponding user (other users cannot access note without permission)
- A simple user registration web page is incorporated for new users to create their personalized account with a username and password and security question (password reset)
- Users must validate their passwords (password confirmation) when modifying their existing or when creating new accounts
### Stephen
- Users with previously-made accounts can login with "Remember Me" during password authentication if a previous password was entered correctly for that user
- Notifications (window popups) are presented to the user when  filling out the required text fields
- Forgotten passwords can be reset using stored security question or known password\
### Addison
- Revision history incorporated into each note-highlighting last known modified date for the note
- Undo/redo button to remodify most recent note
- Dropdown button which sorts notes
- Search field which will recursively sort through all the user's current notes\
### Najm
- Multiple typefaces and font styles  
- Hyperlinks are available on every webpage (weblinks)
- Copy, paste, and duplicate note(s)
- Modify existing user account details

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
- Passwords must be stored securely in database using SMA256 encryption
- The font size must be no smaller than 12 for all headers on the website

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Benjamin>
### 1. Notes created on webpage are restricted to corresponding user
- **Pre-condition:** User is logged into their account
- **Trigger:** User creates a note
- **Primary Sequence:**
1. User clicks a button on the webpage that says "Create new note" when hovered over.
2. System prompts user to enter title for the note.
3. User enters title for the note.
4. System prompts user if they would like to give permission (Read or Read & Write) to another user.
5. User enters other users to give permission to (Read or Read & Write).
6. User submits the note creation.
7. System creates new note with given conditions (Title & Other user permissions).
8. User is taken to newly created note after system is finished creating.

- **Primary Postconditions:**<br>
1. Note is successfully created on the webpage
    - The system displays the user's newly created note on their webpage
2. Note is unsuccessfully created
    - The system does not display newly created note and notifies the user

- **Alternate Sequence:**<br>
3\. User does not enter a title for the note <br>
  a. The system notifies user there is no title <br>
  b. The system prompts user to enter a valid title (Alphanumeric longer than 0 characters) <br>

  5\. User chooses not to give any permissions to other user <br>
  a. The system prompts user "Are you sure?" <br>
  b. User confirms confirmation

### 2. A simple user registration web page is incorporated for new users to create their personalized with a username, password, and security question to reset their password
- **Pre-condition:** User is on the notes app webpage
- **Trigger:** User clicks "Create new account" 
- **Primary Sequence:**
1. System presents user with a simple account creation page (Username, Password, Password confirmation, and a Security question)
2. User enters username
3. User enters password
4. User enters password again
5. User selects one of five security questions to answer
6. User enters answer to security question
7. User clicks on "Finish creating account"
8. System creates account

- **Primary Postconditions:**<br>
1. Account is successfully created
    - The system displays their successfully created account on the screen with their information to copy down
2. Account is unsuccessfully created
    - The system informs the user it was unable to create an account and to try again

- **Alternate Sequence:**<br>
4\. Password does not match with previous password<br>
  a. The system notifies user that passwords do not match <br>
  b. The system prompts user to enter a matching password<br>

  6\. User does not enter an answer to the security question<br>
  a. The system displays a message saying this space can't be left blank<br>
  b. The system prompts user to enter an answer to the security question

### 3. Users must validate their passwords (password confirmation) when modifying their existing account
- **Pre-condition:** User is logged in
- **Trigger:** User enters "Modify Account" option
- **Primary Sequence:**
1. The system prompts user what they would like to modify (i.e. Username, password, and/or security question)
2. User modifies their account details
3. The system prompts user to enter their current password to successfully modify new account details
4. User enters current password
5. The system prompts user "Are you sure?"
6. User clicks on confirmation
7. The system proceeds to modify account details

- **Primary Postconditions:**<br>
1. Account is successfully modified
    - The system displays a "Successfully modified" message to user with their new account details to copy
2. Account is unsuccessfully modified
    - The system informs the user it was unable to modify their account and to try again

- **Alternate Sequence:**<br>
2\. User enters all information but an incorrect matching password<br>
  a. System notifies user that the passwords do not match<br>
  b. System prompts user to enter a matching password<br>
  
4\. User enters incorrect password<br>
  a. The system notifies user that the password was incorrect<br>
  b. The system prompts user to enter a correct password

### 4. Users with previously-made accounts can login with "Remember Me" during password authentication if a previous password was entered correctly for that user
- **Pre-condition:** Users must type the correct password when logging in
- **Trigger:** User checks the box of "Remember Me"
- **Primary Sequence:**
1. Website has a box which allows users to check
2. If user checks box, the website will remember the user
3. If user does not check the box, the website will not remember the user
4. The system will remember the user and will automatically login into the website for the user
5. User can ask the website to not remember them anymore if they pressed "Remember Me" before
6. System will not remember user and will ask for username and password
7. If user changes password, the website will ask for username and password again

- **Primary Postcondition:**<br>
1. User checks the "Remember Me" box
   - The system will remember the username and password in which it will be put in automatically the next time the user uses the wesbite
2. User does not check the "Remember Me" box
   - System will not remember the username and password and will ask for the username and password the next time the user uses the website

- **Alternate Sequence:**<br>
7/. User checks "Remember Me" box, but changes the password afterwards
   a. The "Remember Me" function would then be reverted
   b. System will act as if the "Remember Me" function was never on

### 5. Notifications (window popups) are presented to the user when filling out the required text fields
- **Pre-condition:** Users press create account and start putting information in
- **Trigger:** Users press create account
- **Primary Sequence:**
1. When they press "Create Account" users will be sent to another site with a form for putting in information
2. Users will insert necessary information in each specific box
3. Users will see which boxes are necessary for information with an asterisk next to the question
4. Users will be presented with certain questions like birth date, username, password, and name

- **Primary Postcondition:**<br>
1. User fill in all necessary information
   - System will create the account and input in system
  
- **Alternate Sequence:**<br>
3/. User does not fill in information in the question with astericks
  a. System would not create the account and stay on the same website
  b. User will be presented with an error sign saying what box has not been filled

