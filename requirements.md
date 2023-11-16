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

## Non-functional Requirements
- Passwords must be stored securely in database using SMA256 encryption
- The font size must be no smaller than 12 for all headers on the website

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

### 3. Users must retype their original password in order to change to a new password. 
- **Pre-condition:** User is logged in
- **Trigger:** User enters "Change password" option
- **Primary Sequence:**
1. The system prompts user what they would like to change password
2. The system prompts user to enter their current password to successfully modify new account details
3. User enters current password
4. User enters new password in "new password" column
5. User enters new password again to make sure it is the right password in "re-type new password" column 
6. The system prompts user "Are you sure?"
7. User clicks on confirmation
8. The system proceeds to changes password

- **Primary Postconditions:**<br>
1. Password is successfully changed
    - The system displays a "Successfully changes" message to user with their new account details to copy
2. User types in the wrong original password
    - The system informs the user the original password was incorrect

- **Alternate Sequence:**<br>
7\. User enters all information but an incorrect matching password<br>
  a. System notifies user that the passwords do not match<br>
  b. System prompts user to enter a matching password<br>

## Use Cases <Stephen>
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
User checks "Remember Me" box, but changes the password afterwards
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
User does not fill in information in the question with astericks
  a. System would not create the account and stay on the same website
  b. User will be presented with an error sign saying what box has not been filled

### 6. Forgotten passwords can be reset using stored security question or known password 
-  **Pre-condition:** User forgets their password
-  **Trigger:** User presses the "forget password" button
-  **Primary Sequence:**
1. Users would be able to reset password with the press of "forget password"
2. Users would be directed to another website for forgotten passwords
3. Users need to answer security questions in which they created while creating their account
4. Users can also retype their old password in which they can create a new password afterwards

- **Primary Postcondition:**<br>
1. User finishes answering all the security questions right
   -Users are able to change their password
2. User types in old password
   -Users are able to change thier old password into a new password

- **Alternate Sequence:**<br>
User does not answer the security questions correclty
  a. User gets shown an error and have 3 tries left 
  b. After the theree failed attempts, user would be locked out for security purposes

## Use Cases <Najm>
### 7. Multiple typefaces and font styles
-  **Summary:** User creates a note and is able to customize the text with typefaces and font styles
-  **Pre-condition:** User is logged in and creates a new note
-  **Trigger:** User highlights a portion of the text they want to customize.
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User creates new note or selects existing note they want to customize 
3. User highlights the portion of the text they want to customize then selects the font style and typeface they want
4. The text is displayed with how they want and they save the note. 

- **Primary Postcondition:**<br>
1. Note is edited and customized font/typeface is saved.
   
- **Alternate Sequence:**<br>
User selects the wrong note to customize. 
  
- **NonFunctional Requirements:**<br>
1. It changes the font within 1 second


### 8. Hyperlinks are available on every webpage (weblinks)
-  **Summary:**  User can add hyperlinks to text in a note and navigate to it
-  **Pre-condition:**  User is logged in, creates a new note
-  **Trigger:** User selects the note that had the text and highlights the text they want to add the hyperlink to. 
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User selects new or existing note they want to hyperlink
3. User interacts with the application to insert a hyperlink and enters the URL and link text for it. 
4. The hyperlink is created and displays it within the text so that the user can navigate to it when the hyperlink is clicked.

- **Primary Postcondition:**<br>
1. Note now contains hyperlink within the chosen text
   
- **Alternate Sequence:**<br>
User inserts an incorrect link for a hyperlink that doesn’t exist and an error occurs.
  
- **NonFunctional Requirements:**<br>
1. hyperlink functions fast without delay


### 9. Copy, paste, and duplicate note(s)
-  **Summary:**  User can copy, paste, and duplicate their notes
-  **Pre-condition:** User is logged in and can view their notes
-  **Trigger:** User selects the note they want to copy/paste/duplicate. 
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User selects note they want to copy/paste/duplicate
3. User clicks “copy” to the note they want to copy
4. User creates new note and clicks “paste” to paste the copied note onto the new note
5. User selects a note and clicks “duplicate” which will create a duplicate copy of that same note
6. User saves, and can later access and edit the new notes. 

- **Primary Postcondition:**<br>
1. The note that was copied/pasted/duplicated is now in a new note that contains it.
   
- **Alternate Sequence:**<br>
User selects more than one note to copy/duplicate which will result in an error
  
- **NonFunctional Requirements:**<br>
1. It copy/pastes/duplicates in 2 seconds. 

### 10. Modify existing user account details
-  **Summary:** User can modify existing user account info/details
-  **Pre-condition:** User is logged into their account of this application
-  **Trigger:** User navigates to account settings and selects the info they want to modify
-  **Primary Sequence:**
1. User logs into account
2. User navigates to account settings and selects the info they want to modify
3. User types in the new information 
4. User clicks save changes
5. Application processes the changes and updates the user’s account info

- **Primary Postcondition:**<br>
1. he user’s account info is updated and saved
   
- **Alternate Sequence:**<br>
User inserts incorrect info, like for names they type in numbers, so an error occurs. 
  
- **NonFunctional Requirements:**<br>
1. Application displays in Spanish

## Use Cases <Addison>
### 11. Revision history from previous savestates
-  **Pre-condition:** User has created account and started or appended current note 
-  **Trigger:** User hovers/views pane with past revision 
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User creates new note (per previous usecase)
3. User types at least one character/number into note
4. User saves note and navigates to revision header in note bar

- **Primary Postcondition:**<br>
Previous/post modified date(s) are shown in revision header

- **Alternate Sequence:**<br>
1. User opens previously created note and navigates to revision header
2. No modifications to note was made, no revisions previously made, revision history is blank/nonexistent

### 12. Undo/Redo Changes from previous savestate
-  **Pre-condition:** User has modified existing note(s) and has made recent changes (same session)
-  **Trigger:** User clicks on undo/redo button in toolbar
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User creates or opens existing note
3. User modifies existing note (recent changes) and saves note
4. User clicks undo button and returns back to previous save state 

- **Primary Postcondition:**<br>
Note is remodified to most recent revision (since last save)

- **Alternate Sequence:**<br>
Clicking on Undo button, changed to “Redo”, reverts back to original state (before any “Undo” changes were made)

### 13. Sortable notes
-  **Pre-condition:** User has at least one saved note in list
-  **Trigger:** User clicks on sort dropdown menu in toolbar and selects sorting option
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User navigates to toolbar and clicks on sort dropdown button
3. User clicks on one of the available options in dropdown menu:
	-Date Added
	-Date Modified
	-Title Ascending
	-Title Descending
4. Dropdown menu title shows selected sorting method (based from list above) 

- **Primary Postcondition:**<br>
Notes are sorted based on the selected dropdown conditions (above)

- **Alternate Sequence:**<br>
1. User selects dropdown item above then re-selects another category from the dropdown menu
2. User clicks on dropdown item but no notes are available (no changes are made)


### 14. Search field for notes list
-  **Pre-condition:** User has at least one saved note in list
-  **Trigger:** User clicks on sort dropdown menu in toolbar
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User navigates to toolbar and clicks on search field 
3. User begins typing contents/string and pressing enter to start search
4. Content condensed based on typed content from user

- **Primary Postcondition:**<br>
Notes are condensed based on the query written by the user in the search field

- **Alternate Sequence:**<br>
1. Typed content does not match any string from the existing notes, “no results found” is displayed
2. No notes have been created, displays “No notes have been created and saved, please create and save a note first”



