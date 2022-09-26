# Manual Tests

Here are a list of manual tests that have been carried out to ensure that SyntheStory works correctly and is bug-free at time of deployment. They also include Behaviour-Driven Tests.

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
* The social media links should change their spacing and layout to display differently on different device sizes.
    * Test: Using DevTools responsive adjustment, the footer should change layout and distance between social media links responsively.
    * Result: The footer changes from inline to block-layout at 768px width and when inlined they move apart equally.

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

## Login Testing
### Message Testing 

## Login Protection Testing

## User Data Protection Testing

## Logout Testing
### Message Testing

## Create Idea/ Genre Page Testing
### Responsiveness

## Generate/ Genre Type Page Testing
### Responsiveness

## Create Story Idea Testing
### Message Testing

## My Stories Page Testing
### Responsiveness

## Story Idea Page Testing
### Responsiveness

## Edit Story Idea Testing
### Message Testing

## Delete Story Idea Testing
### Message Testing


