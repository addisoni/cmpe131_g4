## Functional Requirements

1. Notes created on webpage are restricted to the corresponding user (other users cannot access note without permission)
2. A simple user registration web page is incorporated for new users to create their personalized account with a username and password and security question (password reset)
3. Users must validate their passwords (password confirmation) when modifying their existing or when creating new accounts
4. Users with previously-made accounts can login with "Remember Me" during password authentication if a previous password was entered correctly for that user
5. Notifications (window popups) are presented to the user when  filling out the required text fields
6. Forgotten passwords can be reset using stored security question or known password\
7. Revision history incorporated into each note-highlighting last known modified date for the note
8. Undo/redo button to remodify most recent note
9. Dropdown button which sorts notes
10. Search field which will recursively sort through all the user's current notes\
11. Multiple typefaces and font styles
12. Hyperlinks are available on every webpage (weblinks)
13. Copy, paste, and duplicate note(s)
14. Modify existing user account details

## Non-functional Requirements
- Only expected to work on Google Chrome
- Webpages should load in less than 2 seconds

## Use Cases 
### 1. Notes created on webpage are restricted to corresponding user (Benjamin Lim)
- **Pre-condition:** User is logged into their account with an existing note
- **Trigger:** User clicks on a permissions button
- **Primary Sequence:**
1. User enters other users to give permission to (Read or Read & Write) for existing note.
2. User modifies note permissions and saves changes.
3. System updates note with given conditions.

- **Primary Postconditions:**<br>
1. Note permission status displays succesfull changes to permissions
2. Note heirachy for note permissions show respective users with correct Read and Write permissions

- **Alternate Sequence:**<br>
1\. User does not enter a title for the note <br>
  a. The system notifies user there is no title <br>
  b. The system prompts user to enter a valid title (Alphanumeric longer than 0 characters) <br>

  2\. User chooses not to give any permissions to other user <br>
  a. The system prompts user "Are you sure?" <br>
  b. User confirms confirmation

  3\. Note is unsuccessfully created <br>
  a. The system does not display newly created note and notifies the user

### 2. A simple user registration web page is incorporated for new users to create their personalized with a username, password, and security question to reset their password (Benjamin Lim)
- **Pre-condition:** User is on the notes app webpage
- **Trigger:** User clicks "Create new account" 
- **Primary Sequence:**
1. System presents user with a simple account creation page (Username, Password, Password confirmation, and a Security question)
2. User enters credentials for account
5. User selects one of five security questions to answer
6. User enters answer to security question
7. User clicks on "Finish creating account"
8. System creates account

- **Primary Postconditions:**<br>
1. Account is successfully created <br>
   - The system displays their successfully created account on the screen

- **Alternate Sequence:**<br>
4\. Password does not match with previous password<br>
  a. The system notifies user that passwords do not match <br>
  b. The system prompts user to enter a matching password<br>

  6\. User does not enter an answer to the security question<br>
  a. The system displays a message saying this space can't be left blank<br>
  b. The system prompts user to enter an answer to the security question

### 3. Logout of user account (Benjamin Lim)
- **Pre-condition:** User is already logged into existing account
- **Trigger:** User presses on "Logout" button in menu
- **Primary Sequence:**
1. User is returned to login window
2. User account is no longer in session

- **Primary Postcondition:**<br>
1. User account credentials are removed from session
2. User is unable to access previous user's notes

### 4. Create new notes (Stephen Shao)
- **Pre-condition:** Users must already have an account and be logged in
- **Trigger:** User clicks on new note button
- **Primary Sequence:**
1. Window pane transitions away from original note view (note list)
2. User is presented with blank note (no text within new note)
3. User is able to start editing new note in view

- **Primary Postcondition:**<br>
1. A new note is added to the user's note pane (directory)
2. Note is saved to user's profile

### 5. Inerstable tables into notes (Stephen Shao)
- **Pre-condition:** Note previously exists
- **Trigger:** User clicks on table to insert into note
- **Primary Sequence:**
1. Table view (sizing) appears, requesting row and column dimension for requested table
2. Table size is copied into note document
3. Table is readily available to be modified by the user (inputting text into individual fields)

- **Primary Postcondition:**<br>
1. Requested table size/demension is displayed
2. Table modifications are available to the user (add/remove columns or rows)

### 6. Forgotten passwords can be reset using stored security question or known password (Stephen Shao)
-  **Pre-condition:** User forgets their password
-  **Trigger:** User presses the "forget password" button
-  **Primary Sequence:**
1. Users would be able to reset password with the press of "forget password"
2. Users would be directed to another website for forgotten passwords
3. Users need to answer security questions in which they created while creating their account
4. Users can also retype their old password in which they can create a new password afterwards

- **Primary Postcondition:**<br>
1. User finishes answering all the security questions right
   - Users are able to change their password
2. User types in old password
   - Users are able to change thier old password into a new password

- **Alternate Sequence:**<br>
User does not answer the security questions correclty
  a. User gets shown an error and have 3 tries left 
  b. After the theree failed attempts, user would be locked out for security purposes

### 7. Multiple typefaces and font styles (Najm Masri)
-  **Summary:** User creates a note and is able to customize the text with typefaces and font styles
-  **Pre-condition:** User is logged in and creates a new note
-  **Trigger:** User highlights a portion of the text they want to customize.
-  **Primary Sequence:**
1. User logs into account, opens to notes list
2. User creates new note or selects existing note they want to customize 
3. User highlights the portion of the text they want to customize then selects the font style and typeface they want
4. User clicks on one of the typeface buttons (Bold, italicize, etc.)

- **Primary Postcondition:**<br>
1. Note is edited and customized font/typeface is saved
2. The text is displayed with the specified font/typeface in the notes

- **Alternate Sequence:**<br>
User selects the wrong note to customize. 

### 8. User is able to create folders to organize notes (Najm Masri)
-  **Summary:**  Users are able to add notes to folders for additional organization
-  **Pre-condition:**  User is logged in, at least one note exists
-  **Trigger:** User clicks "new folder" button
-  **Primary Sequence:**
1. User specifies custom name for the folder
2. A new folder is created in the pane/directory view
3. Existing note is moved to the new folder

- **Primary Postcondition:**<br>
1. Navigating to folder will show new note with custom name
   
- **Alternate Sequence:**<br>
1. Folder already exists, user is able to add new or other notes to folder
2. Folder exists, user is able to rename folder to another name

### 9. Copy, paste, and duplicate note(s) (Najm Masri)
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
1. User selects more than one note to copy/duplicate which will result in an error

### 10. Modify existing user account details (Najm Masri)
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

### 11. View revision history from past savestates (Addison Ivan)
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

### 12. Undo/Redo revision history (restore pre-existing note savestates) (Addison Ivan)
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

### 13. Sortable notes (Addison Ivan)
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


### 14. Search field for notes list (Addison Ivan)
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
