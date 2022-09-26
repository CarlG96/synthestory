# Manual Tests

Here are a list of manual tests that have been carried out to ensure that SyntheStory works correctly and is bug-free at time of deployment.

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
### Responsiveness

## Homepage Testing
### Responsiveness

## Signup Testing

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


