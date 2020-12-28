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


