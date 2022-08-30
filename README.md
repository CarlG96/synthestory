# SyntheStory 

SyntheStory is a website that randomly generates story ideas for authors. A user can filter ideas by genre and choose whether they want a plot idea or character idea. A user can then save. $$$edit$$$ or delete these ideas on their own personal account.

# User Stories and Epics

## Basic Setup Epic

- As a developer, I need to perform basic set up so that my django project is working and deployed to Heroku.
- As a developer, I want to set up a base.html page for a non-logged in user so that the layout can be reused.
- As a devloper, I want to set up a base.html page for a logged-in user which is styled similarly to the non-logged in one so that the layout can be reused.

## Frontend Epic

- As a user, I want the website to be styled with color that contrasts well so the website is clear.
- As a user, I want the website to have good UI/ UX design and feedback so it is pleasing to navigate.
- As a desktop/ laptop user, I want the website to have a navigation bar for desktop devices so I can easily navigate to which section of the site I want.
- As a user, I want the website to have a footer with social media links so that I can view social media and contacts.
- As a mobile user, I want the website's navigation bar to come in the form of a burger menu so I can navigate the site more easily.
- As a user, I want the website to appear responsive over a wide range of devices and browsers.
- As a potential user/ aspiring author, I want a home page which explains what the website can offer me.
- As a user/ author, I want to be able to select from a range of genres and between plot/character ideas to choose what type of story idea I want generated.

## Authorisation Epic
- As a user, I would like there to be a sign up page so that I can easily sign up for an account.
- As an admin, I would like to implement allauth so that users will be easily able to access their account.
- As an admin of the site, I would like users to verify their email so that I can ensure the user is real.
- As a user, I would like there to be a login page so that I can easily log in once I have made an account.
- As a user, I would like to stay signed in whilst navigating the website so that unless I leave I don't have to re-input my details.

## Admin CRUD Epic
- As an admin, I want the ability to add to the databases which hold the information which assists in randomly generating story ideas (nouns, verbs etc), so the range of story ideas can grow over time.
- As an admin, I want the ability to delete information for randomly generating story ideas (nouns, verbs etc), so I can remove unwanted story ideas.
- As an admin, I want the ability to categorise information used to randomly generate story ideas by genre and whether they are plot or character ideas, so my users can have different experiences based on their preferences.

## User CRUD Epic
- As a user/ author, I want the ability to save randomly generated story ideas so I can access them at a later date.
- As a user/ author, I want the ability to change randomly generated story ideas so I can fine tune story ideas that aren't exactly what I want.
- As a user/ author, I want the ability to delete story ideas once I no longer want them so they do not clutter up my profile.
- As a user/ author, I want the site to use defensive programmming to prevent me from accidentally deleting story ideas so I don;t accidentally delete one I want to keep.

## Testing Epic
- As a developer, I want to make sure that all CRUD functionality is working correctly by testing it from both a user and admin perspective so I know the website is working as intended and bug-free.
- As a developer, I want to create some unit tests to test whether redirects and templates are acting correctly, so that functionality for the website is good.
- As a developer, I want to run my code through validators so that I know that it is of a good standard and not breaking any conventions.
- As a developer, I want to check my website in DevTools to make sure it is responsive and has good loading times so that it has good accessibility for people.
- As a developer, I want to make sure that my CSS/ JavaScript and images are loading properly on all pages so that the site appears professional.

## Documentation Epic
- As a developer, I want to complete the documentation so that others understand what my website does and also for potential future developers looking to change things.

