# Manual Tests

Here are a list of manual tests that have been carried out to ensure that SyntheStory works correctly and is bug-free at time of deployment. They also include Behaviour-Driven Tests and some testing of the JavaScript used for messages to appear and disappear.

## Base Navigation Bar Testing
* User should be able to navigate the site easily using the navigation bar at the top of the page. On smaller screen sizes, the navigation bar should fold into a burger menu. The navigation bar should also reflect the user's logged in state; showing a login and signup link if the user is not logged in and a logout link if the user is logged in.

    * Test: Each of the navigation links in the navigation bar should be usable and go to the correct page, and the SyntheStory logo should also redirect back to the homepage.
    * Result: Each of the navigation links in the navigation bar are usable and go to the correct page, the SyntheStory logo also redirects back to the homepage.

    * Test: Upon the user logging in, the navigation bar should show the Logout link but not the Login or Signup links.
    * Result: After logging in, the user can only see the Logout link and not the Login or Signup links.

    * Test: After logging out, the user can only see the Login and Signup links and not the Logout Link.
    * Actual: The user can only see the Login and Signup links and not the Logout Link after logging out.

### Responsiveness
* The user should be able to use the navigation bar in SyntheStory across a wide range of devices and the navigation bar should squash down to a quasi-burger menu (with the word Menu instead to aid accessibility).

    * Test: Using DevTools Responsive adjustment, the Menu compresses/ expands in width and looks good and is usable across a wide range of devices.
    * Result: The Menu compresses and expands at 992px width so is expanded for monitors and compressed for most tablets/ mobile devices. The compressed menu works by being clicked/ touched and dropping down and this works without affecting any other web pages usability.

## Base Footer Testing
* User should be able to navigate to social media links from clicking on the icons, the user's logged in status should also be noticed if the user is logged in. 

    * Test: All of the social media links are usable and direct to the corresponding social media site's front page.
    * Result: The social media links all work and direct to the correct pages.

    * Test: The user's logged in status should be shown if the user is logged in to SyntheStory.
    * Result: The footer says "Logged in as {{ username }}" if the user is logged in and doesn't display this information if the user is not logged in.

### Responsiveness
* The social media links should look good for a wide range of devices.

    * Test: Using DevTools responsive adjustment, the footer should change distance between social media links responsively.
    * Result: The footer reacts responsively across a wide range of devices.

## Homepage Testing
* The homepage should display the instructions for using SyntheStory and this should be laid out easily for the user.

    * Test: The instructions on the home page should be easy to follow.
    * Result: The user can clearly understand the instructions as they are in order and have a linebreak between them. The text also contains emphasis and is contrasted well with the background.

    * Test: If the user is logged in, the user should see that reflected by the first step changing its text.
    * Result: A logged in user sees the text of Step 1 as: "You've already completed this step by logging in!" whereas a non-logged in user sees "Start by signing up for an account here: Account Signup" with the Account Signup text displaying a link to the signup page.

    * Test: The text in Step 1 that contains a link should link to the Signup page.
    * Result: The text in Step 1 directs the user to the Signup page.

### Responsiveness
* The homepage should change its layout in order to accomodate different screen sizes.

    * Test: The layout of the page should change to work on multiple different screen sizes.
    * Result: The layout changes from inlining the Step x with its corresponding text on screen widths larger than 1200px to making them block elements. This still makes sense with the text for each step appearing after the Step x title. The Steps and texts are still in the correct order.

## Signup Testing
* The user should be able to signup to SyntheStory by creating an account.

    * Test: On the Signup page, the user should be able to create an account with SyntheStory with no errors coming up.
    * Result: A user can signup an account with SyntheStory, in which case they are logged in and redirected back to the home page.

    * Test: The user should be able to create an account without supplying an email address, as this is optional.
    * Result: The user can create an account without supplying an email address.

    * Test: If the user's password is too short, they are notified and not signed up.
    * Result: The user is not signed up and the text "This password is too short. It must contain at least 8 characters." is displayed.

## Login Testing
* The user should be able to login without hassle once they have signed up.

    * Test: The user is able to login once they have registered an account by signing up.
    * Result: The user can log in with their registered account.

### Message Testing 
* The user should receive a message when they login that disappears after three seconds unless it is closed out.

    * Test: The user recieves a message when they login that addresses who they are logged in as.
    * Result: When a user signs in, the message they receive is "Successfully signed in as {{ username }}".

    * Test: The login message disappears after three seconds automatically.
    * Result: The login message disappears soon after appearing automatically. I didn't accurately measure the time but seemed roughly three seconds from counting.

    * Test: The user can dismiss the message by clicking the 'X' before the message is automatically dismissed.
    * Result: It is possible to dimiss the message before it is automatically dismissed by clicking the 'X' within three seconds of the message appearing.

## Login Protection Testing
* Users should be prevented from accessing parts of the site they shouldn't without first logging in.

    * Test: The user can access the 'Create an Idea/ Genre' page straight after logging in if they click on it and fill in the log in.
    * Result: The user will go immediately to 'Create an Idea/ Genre' page straight after logging in after trying to click on it whilst not logged in.

    * Test: The user CAN'T access the 'My Stories' Page after clicking on the link and then logging in but are redirected to the home page. This is to prevent url errors with 'None' becoming part of the url.
    * Result: The user is redirected to the home page if they try to directly access the My Stories Page and then log in when prompted.

    * Test: The user can access the 'Generate/ Genre Type Page' directly if they fill in the url for it and pass the login prompt.
    * Result: The user can access these pages after logging in if they know the url as this is not a security issue.

    * Test: The user can access a 'Story Idea' page by typing in the url and logging in as long as that particular Story Idea page is associated with thier account and not someone elses.
    * Result: The user can do this if they know the url. For example https://synthestory.herokuapp.com/my-stories/1/36/ would relate to the first user and the thirty-sixth story idea created. If the thirty sixth story idea is connected by a foreign key in the database to the first user in the database they can access this page immediately after completing the login prompt.

## User Data Protection Testing
* The user shouldn't be able to edit or delete other user's story ideas by accessing pages that contain story ideas linked to another user.

    * Test: A logged in user CAN'T access another user's stories by typing in the url and are redirected to the 403 page instead.
    * Result: Another user is prevented from accessing another user's story by being redirected to the 403 page.

    * Test: A logged in user can't access another user's 'My Stories' page.
    * Result: A logged in user is redirected to the 403 page.

    * Test: A non-logged in user that attempts to access the above two pages will be redirected to the login page
    * Result: The non-logged in user is redirected to the login page. Even if they login, if they aren't meant to have access they cannot break through the 403 'barrier' protecting the other user's information.

## Logout Testing
* The user should be able to logout without errors.

    * Test: A logged in user can click the link to the Logout page and is directed to it.
    * Result: A logged in user can do this.

    * Test: A logged in user should be able to click the 'Sign Out' button on the Logout page to log out. They should be redirected to the home page.
    * Result: A logged in user can do this.

### Message Testing
* The user should receive a message when they login that disappears after three seconds unless it is closed out.
    * Test: The user recieves a message when they logout that addresses the fact they have logged out.
    * Result: The user receives a message saying "You have signed out."

    * Test: The logout message disappears after three seconds automatically.
    * Result: The logout message disappears soon after appearing automatically. I didn't accurately measure the time but seemed roughly three seconds from counting.

    * Test: The user can dismiss the message by clicking the 'X' before the message is automatically dismissed.
    * Result: It is possible to dimiss the message before it is automatically dismissed by clicking the 'X' within three seconds of the message appearing.

## Create Idea/ Genre Page Testing
* The user should be able to access the 'Create Idea/ Genre Page' once they have logged in.
    
    * Test: From the homepage, a logged in user should be able to click on the 'Create Idea' link in the navigation bar and be taken to the Genre Page.
    * Result: A logged in user can do this.

    * Test: Images should be displayed for each genre available, giving an insight into something to do with the genre. This should be tested in the deployed site to ensure it is correctly uploaded from Cloudinary.
    * Result: Images are available to view (however they disappear at smaller device sizes to save pageroom).

### Responsiveness
* The 'Create Idea/ Genre Page' should change drastically depending on the size of device used. This is because the page uses images and as such needs to change so that it works correctly.
    
    * Test: On larger device sizes the 'cards' used for the genres display in rows of three.
    * Result: At sizes of 768px width and up the genres display in a line of three.

    * Test: On medium device sizes the 'cards' display in rows of one as block elements but still have images in them.
    * Result: At sizes between 500px and 768px width the 'cards' display in single lines and still contain images.

    * Test: On small device sizes the 'cards' display like on medium devices but without any images.
    * Result: The images display value is set to 'none' but the 'cards' still contain the text and links.

## Generate/ Genre Type Page Testing
* The 'Generate/ Genre Type' is accessible from the 'Create Idea/ Genre Page' and should be accessible once logged in.
    
    * Test: The 'Generate/ Genre Type' page is accessible from one of many links in the 'Create Idea/ Genre Page' and can be accessed once logged in.
    * Result: The user is able to click on this link and be directed to the correct page corresponding to their selected genre.

    * Test: The 'Generate/ Genre Type' page should have a prefilled in Story Idea field in its form.
    * Result: It does have a prefilled in Story Idea field in the form when accessing the page.

    * Test: The 'Generate/ Genre Type' page should contain only ideas that correlate to the genre chosen from the 'Create Idea/ Genre Page'.
    * Results: After testing all of the current links in the 'Create Idea/ Genre Page' all of them go to pages that only pull from parts of the database with ideas correlating with the genre chosen.

    * Test: By clicking the button labelled 'Generate Another Idea!', the prefilled field is changed as the page is refreshed.
    * Result: The prefilled field is changed when the page refreshes and it only pulls from parts of the database with ideas correlating with the genre chosen.

### Responsiveness
* The 'Generate/ Genre Type' page should be responsive over many device sizes.
    * Test: The 'Generate/ Genre Type' page works across a large range of devices, and text, fields and buttons resize to fit.
    * Result: This happens, and the large size of the textareas allow the text to continue to be visible even at very small screen widths.

## Create Story Idea Testing
* On the 'Generate/ Genre Type' page, the user should be able to create a story.
    * Test: By clicking on the 'Save Story Idea' button on the 'Generate/ Genre Type' page the user is redirected to the 'My Stories Page' where their Story Idea appears. This only happens if the Title and Story Idea fields are filled out.
    * Result: After filling out the relevant fields and clicking the button, the user is directed to the My Stories Page, where the Story Idea appears.

    * Test: The user should be able to edit the Story Idea field and populate it with their own text before saving the story idea.
    * Result: This is possible and redirects to the My Stories Page and the saved text is the same as what the user has inputted.

### Message Testing
* The user should receive a message when they save a Story Idea that disappears after three seconds unless it is closed out.
    * Test: The user recieves a message when they save a Story Idea that addresses the fact they have saved one.
    * Result: The user receives a message saying "Successfully added story idea: {{ Story Idea }}".

    * Test: The message disappears after three seconds automatically.
    * Result: The message disappears soon after appearing automatically. I didn't accurately measure the time but seemed roughly three seconds from counting.

    * Test: The user can dismiss the message by clicking the 'X' before the message is automatically dismissed.
    * Result: It is possible to dimiss the message before it is automatically dismissed by clicking the 'X' within three seconds of the message appearing.

## My Stories Page Testing
* The 'My Stories' Page is where a logged in user's Story Ideas should be held.
    * Test: A logged in user can access the 'My Stories' page by clicking on the link in the navigation bar titled: 'My Stories'.
    * Result: A logged in user can do this and will be sent to their own page.

    * Test: If a user has no saved stories, text appears telling and a link to the 'Create Idea/ Genre Page' is provided.
    * Result: This occurs and the link works.

    * Test: A user's saved stories appear in the 'My Stories' page.
    * Result: This occurs and you can click on the links to be taken to the respective page for each Story Idea.

    * Test: A user's saved stories appear in order of most-recently edited on the 'My Stories' page.
    * Result: After editing a Story Idea it appears first in the 'My Stories' page.

### Responsiveness
* The page layout of the 'My Stories' page should change based on the width of the device used and should be responsive.

    * Test: On larger device sizes, the layout of the page should have rows of three cards, with any excess remainders of one or two falling on a new row.
    * Result: This occurs on devices of 768px width or larger, with each card being equal in width.

    * Test: On smaller devices, the layout of the page has each 'card' on its own row.
    * Result: This occurs on devices of 768px or lower.

## Story Idea Page Testing
* The 'Story Idea' page should be accessible from the 'My Stories' page. The 'Story Idea' page contains whatever Story Idea a user has clicked on from their 'My Stories' page.
    
    * Test: A logged in user can access a 'Story Idea' page by clicking on the 'View' link in the 'My Stories' page.
    * Result: This is possible, and returns a page containing that exact Story Idea.

    * Test: The 'Story Idea' page should have a 'Delete Story Idea' button which can only be accessed by clicking a dropdown.
    * Result: The user is prevented from clicking the 'Delete Story Idea' button until the dropdown comes down.

### Responsiveness
* The 'Story Idea' page should change based on the width of the device used and should be responsive.

    * Test: The 'Story Idea' page should accomodate devices of many sizes.
    * Result: The 'Story Idea' page does not change layout but squashes and looks good across a large range of devices. On very small width devices the Story Idea field adds a scroll when the text overspills.

## Edit Story Idea Testing
* The user should have the ability to edit their Story Ideas from inside the 'Story Idea' page of that respective Story Idea.

    * Test: The textareas in the form for the Story Idea should be disabled upon entering the 'Story Idea' page.
    * Result: The textareas are disabled via script by default.

    * Test: If the user clicks the 'Edit Story Idea' button, then a new button called the 'Save Edited Idea' button should appear and the Story Idea and Title fields should become changeable.
    * Result: This occurs and the fields are changeable.

    * Test: If the user changes the Story Idea or Title fields and clicks the 'Save Edited Idea' button, they should edit their Story Idea and this should be saved.
    * Result: The user is redirected to the 'My Stories' page and the Story Idea and Title fields will be changed upon entering the same 'Story Idea' page. The most newly updated item also appears first in the 'My Stories' page.

### Message Testing
* The user should receive a message when they edit a Story Idea that disappears after three seconds unless it is closed out.

    * Test: The user recieves a message when they edit a Story Idea that addresses the fact they have edited one.
    * Result: The user receives a message saying "Successfully edited story idea: {{ Story Idea }}".

    * Test: The message disappears after three seconds automatically.
    * Result: The message disappears soon after appearing automatically. I didn't accurately measure the time but seemed roughly three seconds from counting.

    * Test: The user can dismiss the message by clicking the 'X' before the message is automatically dismissed.
    * Result: It is possible to dimiss the message before it is automatically dismissed by clicking the 'X' within three seconds of the message appearing.

## Delete Story Idea Testing
* The user should have the ability to delete their Story Ideas when they no longer want them.

    * Test: If the user clicks the 'Delete Story Idea' button in the 'Story Idea', that Story Idea will be deleted.
    * Result: When the user clicks the 'Delete Story Idea' button, the story is deleted and the user is redirected to the 'My Stories' page. The story will not appear as it has been deleted from the database.

### Message Testing
* The user should receive a message when they delete a Story Idea that disappears after three seconds unless it is closed out.

    * Test: The user recieves a message when they delete a Story Idea that addresses the fact they have deleted one.
    * Result: The user receives a message saying "Successfully deleted story idea: {{ Story Idea }}".

    * Test: The message disappears after three seconds automatically.
    * Result: The message disappears soon after appearing automatically. I didn't accurately measure the time but seemed roughly three seconds from counting.

    * Test: The user can dismiss the message by clicking the 'X' before the message is automatically dismissed.
    * Result: It is possible to dimiss the message before it is automatically dismissed by clicking the 'X' within three seconds of the message appearing.

