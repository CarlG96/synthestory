# SyntheStory 

## Purpose of SyntheStory

SyntheStory is a website that randomly generates story ideas for authors. The 'story idea' is a central concept on SyntheStory and represents a short and sweet premise for a story.

After creating an account o SyntheStory, a user can filter by genre and SyntheStory will randomly generate a story idea for the user by pulling from a database containing only that particular genre's ideas. These ideas are created by the admin of the site and additional snippets of ideas and genres can be created by the admin in order to extend the usability of the site.

After a user has given a story idea a title, they can edit (editing can be done before saving), save and delete stories by accessing their own area of the website called 'My Stories'. This way a user can refer to their ideas, change randomly generated ones that don't <em>quite</em> fit and even create entirely original ones. SyntheStory is a website designed to get an author's writing off the ground and NOT a place to actually write stories so there is a character limit on the length of story idea.

## Features/ Pages

### Homepage
The Homepage contains a brief introduction and instructions on how to use SyntheStory. It is the only 'main page' (meaning pages other than error pages or pages to do with login) which does not require login access.

<!-Picture goes here->

### Genre Page
The Genre page contains a list of genres from which the user can choose to narrow down a generated story idea. They can click on the links in the cards to take them to a Genre Type page which will display a Story Idea with their chosen genre.

<!-Picture goes here->

### Genre Type Page
The Genre Type page contains a randomly generated Story Idea taken from a 'bank' of Story pieces in the database related to a specific genre. The user can save a story idea using the Save Story Idea! button or refresh the page with a new randomly generated Story Idea by clicking the Generate Another Idea! button. The user can also edit the Story Idea field text and both fields must be filled in before a submission can be made.

<!-Picture goes here->

### My Stories Page
The My Stories Page represents the user's saved stories and as such is unique to each user (see MANUAL_TESTS.md for information on how users are prevented from interfering with other users' data). The My Stories page contains links to each of the users saved Story Ideas.

<!-Picture goes here->
### Story Idea Page
The Story Idea Page is unique to each Story Idea and can only be accessed by the user who's profile corresponds to that particular Story Idea. In the Story Idea page Story Ideas can be edited or deleted by changing the fields and pressing the Edit Story button or pressing the Delete Story button respectively.

<!-Picture goes here->
### Login, Logout and Signup pages
The Login, Logout and Signup pages act as you would imagine, giving people the opportunity to make accounts and work the site. Many parts of the site will be blocked off and will redirect to the Login page unless a user is logged in.

### Error Pages
The 403, 404 and 500 error pages are there to indicate errors to a user. The 404 page will occur if the user tries to access something which does not exist. The 403 page will occur if the user tries to interact with another user's Story Ideas and the 500 page will occur if there is an internal server error. The user will be redirected to the homepage from there.

<!-Picture goes here->
## Future Features
A feature that is far beyond the scope of this project but might be an idea for the future would be to somehow link each generated Story Idea up to an API to do with a text-to-image diffusion model which would display an AI generated image displaying the Story Idea in picture form. I am not entirely sure on the achievability of this at the current moment and am ignorant of any potential copyright issues that would occur but believe it might help inspire an author with imagery.

## Data Model

Five data models were created for SyntheStory: Genre, StoryStart, StoryMiddle, StoryEnd and StoryIdea. The User model was also imported from django.contrib.auth.models.

### Genre Model

The Genre Model represents a single genre by which the user can filter which ideas are generated from. Each Genre instance contains a title, an image and a description to display to the frontend and also contains a creation date which is used to order the Genre data. The Genre Model relates to the StoryStart, StoryMiddle and StoryEnd models by acting as a foreign key for them. New Genres can be created by an admin of the site, allowing extensibility to SyntheStory's random generation in the future.

### StoryStart, StoryMiddle and StoryEnd Models

The StoryStart, StoryMiddle and StoryEnd Models are very similar and could have been derived from a base class but were decided not to due to there only three of them and the story text fields changed size on each of them. They represent corresponding parts of a randomly generated idea and contain story text, creation date and genre(which is a foreign key for Genre) fields. The genre foreign key interacts with the view to make sure that once the user has filtered their ideas by genre only that idea is pulled from when SyntheStory generates random ideas. New StoryStarts, StoryMiddles and StoryEnds can be created by the admin of the site, allowing extensibility to SyntheStory's random generation in the future.

### StoryIdea Model

The StoryIdea Model represents a saved story idea that is connected to a user. This is used to present the user with their story ideas and allow them to edit and delete them as needs be. Each StoryIdea instance contains a user(foreign key connected to User), title, story text and a creation date and updated on date. The title and story text fields are used to display information on the frontend and the creation date is used to refer to when it was created and the updated on date is used to control te order that the story ideas are presented to the user in their My Stories page.

### Entity Relationship Diagram



## Imported Modules, Installed Apps

## Agile Planning

SyntheStory was created using an agile planning method and utilised the GitHub Projects Kanban Board.

### Sprint Method

[Link to Kanban Board for SyntheStory](https://github.com/users/CarlG96/projects/2/views/1)

## Prototypes and Flowcharts

## Technology

## Testing


## Bugs
<img src="media/images/bug-image.png">
I tried to use an internal script in the HTML to pre-populate a form by changing it's 'value' attribute in the HTML with data passed in from the view. This caused Django to represent any unusual characters (such as apostrophes) with data such as '&#x27;' as a safety precaution. I then tried to use an external JavaScript file to do the same but this resulted in it not reading the Django template properly and showing no data. To rectify the problem I passed in an a dictionary of values to the form in the view as an initial value which populated the fields without bugs.

ACCOUNT_EMAIL_VERIFICATION was set to 'optional' in settings. When making fake accounts to test the signup feature using fake email addresses would cause a 500 internal server error due to the email not being sent to a valid email address but the account would still be created. As SyntheStory does not require an email address to verify account I decided to change ACCOUNT_EMAIL_VERIFICATION to 'none' to prevent internal server errors.

## Unfixed Bugs

Firefox messages: The messages that display on firefox browser do not have the text and cross line up correctly. As they work on brave I have left this as it may just be a discrepancy between how the browsers display the messages and it is still prefectly readable and understandable on Firefox.

## Deployment

## Credits
https://www.youtube.com/watch?v=qNifU_aQRio tutorial for navbar
pixabay for images
