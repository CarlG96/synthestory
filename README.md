# SyntheStory 

## Purpose of SyntheStory

SyntheStory is a website that randomly generates story ideas for authors. The 'story idea' is a central concept on SyntheStory and represents a short and sweet premise for a story.

After creating an account o SyntheStory, a user can filter by genre and SyntheStory will randomly generate a story idea for the user by pulling from a database containing only that particular genre's ideas. These ideas are created by the admin of the site and additional snippets of ideas and genres can be created by the admin in order to extend the usability of the site.

After a user has given a story idea a title, they can edit (editing can be done before saving), save and delete stories by accessing their own area of the website called 'My Stories'. This way a user can refer to their ideas, change randomly generated ones that don't <em>quite</em> fit and even create entirely original ones. SyntheStory is a website designed to get an author's writing off the ground and NOT a place to actually write stories so there is a character limit on the length of story idea.

## Features

## Future Features

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

## Unfixed Bugs

## Deployment

## Credits
https://www.youtube.com/watch?v=qNifU_aQRio tutorial for navbar
pixabay for images
https://www.youtube.com/watch?v=GUEB9FogoP8&list=PLDyQo7g0_nsXEOxGlAgccV8fu-cHZnI5B&index=8 for animation of logo