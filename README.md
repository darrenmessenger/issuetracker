# Issue Tracker 

[![Build Status](https://travis-ci.org/darrenmessenger/issuetracker.svg?branch=main)](https://travis-ci.org/darrenmessenger/issuetracker)

<img src="media/img/Main Page.png">

## Reason For Project

This project has been built for the Code Institute Full Stack Frameworks with Django Milestone Final Project .
The brief was to build a full-stack site based around business logic used to control a centrally-owned dataset. It should have an authentication mechanism and provide paid access to the site's data.

Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit 
from the collection of the dataset as a whole.

The main technologies that are to be used for this project are HTML, CSS, JavaScript, Python+Django,Relational database (recommending MySQL or Postgres), Stripe payments, Additional libraries and APIs

I have decided to create a project based on the Issue Tracker idea. It will Report and track work on bugs and other issues with a product they like.

The wireframes for this website can be found in the repository within Github in the directory "media/img/Wireframes", 
or you can click [here](https://github.com/darrenmessenger/issuetracker/tree/main/media/img/Wireframes).

### Database Schema
Postgres was used as the database for the project.
The final database ERD can be found in the folder [here](https://github.com/darrenmessenger/issuetracker/tree/main/media/img/ERD).
The final database consists of 2 tables, Ticket and TicketComment. Details are shown below: 

### Ticket
- title (The title of the ticket)
- author (Author of the ticket)
- content (The description of the bug or the new feature)
- ticket_type (The type of the ticket, bug or new feature)
- created_date (The date the ticket was created)
- published_date (The date the ticket was published)
- views (This integer is increased by 1 everytime the bug/new feature is viewed)
- upvotes (The user can vote for the bug/new feature if they like it or have the same problem)
- image (Any images or screenprints that may help with the description of the bug/new enhancement)
- status (The status of the bug (ToDo, UnerReview, Declined, Planned, InProgress, Completed)

#### TicketComment
- author (Author of the ticket)
- comment (The comment that the user is making)
- comment_date(The date of the comment)
- ticket (The ticket that the comment is linked to)

### User Stories

- Home Page:
- There should be a Navbar with a Login and Register link.
- I should see a welcome message and a link to login or register to the the site. 
- If I press on the Donate button I will be taken to the payments page
- If I press on the All Open Issues button I will be taken to the Outstanding Issues Page
- Navbar:
- If I am not logged in I should see a 'Log In' and a 'Register' menu option.
- If I click the Login link it should open the Login page. 
- If I click the Register link it should open the Register page. 
- If I click on the IssueTracker title in the navbar it should always take me back to the home page.
- If I click on the 'LogOut' menu option it should log me out and take me to the home page.
- Login Page:
- When the Login page is loaded it should show a blank Username and Password.
- If I enter my Username and Password correctly it should navigate to the home page with a new welcome message that includes my username.
- If I enter an incorrect username or password I should see an error message stating that the username or password is incorrect.
- Registration Page:
- When the Registration page is loaded it should show a blank eMail, Username and Password.
- I can register a new account if I fill in all of the fields. 
- If the format of the fields are incorrect then I will receive an error message.
- If the username already exists then I will receive an error message.
- Outstanding Issues Page
- All of the issues should be displayed.
- If the issue is a bug it should have an image of a bug next to the ticket.
- If the issue is a new feature it should have an image showing 'new'.
- I should be able to see the basic details of the ticket. 
- I should be able to click on the upvote button and vote for the ticket. 
- If I click on the upvote button it will vote for the issue and take me to the ticket details. 
- I should be able to see the status of each of the tickets. 
- I should be able to click on a button so that I can read more about the issue. 
- If I click on the Read More button I will be taken to the Issue Detail page.
- Issue Detail:
- I should be able to see all of the details of the issue. 
- If the issue is a bug it should have an image of a bug.
- If the issue is a new feature it should have an image showing 'new'.
- I should be able to click on the upvote button and vote for the ticket. 
- If I click on the upvote button it will vote for the issue and refresh the page. 
- I should be able to see if an image has been added to the ticket. 
- I should see a compressed version of the image.
- If I click on the image it should 'zoom' in and show the image in more detail. 
- I should be able to click on a button to take me back to the Outstanding Issues Page.
- I should be able to click on a button to allow me to edit the ticket. 
- I should be able to see all of the comments that have been added to the ticket. 
- If I am signed in I should be able to add a comment to the ticket. 
- If I am not signed in I should see a message stating that I need to sign in to add a comment. 
- New Issue Page:
- When the page is loaded I should see the descriptions of each section that can be entered. 
- I should be able to enter the details of the issue.
- I should be able to add an image of the issue.
- If I leave a section blank then I should see an error message when I try to create the issue.
- I should be able to click on the ticket type and see a drop down list which is selectable.
- I should be able to click on a button to create the issue. 
- If I click on the button to create the issue I should be taken to the outstanding issues page.






