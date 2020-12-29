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
- Payments Page:
- If I click on the donate button I will be taken to the Payments Page.
- If I enter my payment details correctly and press the submit button I will be charged the desired amount.
- If I enter any incoorect values I will see an error message.
- After the submit button has been pressed and the payment is successful I will see the home page with a confirmation message.
- Profile page:
- If I click on the person icon in the nav bar I will be taken to the profile page.
- I will see basic details of my profile along with a donate button.
- If I click on the donate button I will be taken to the Payments Page.
- Admin Page:
- If I need to delete an issue then I can do so from the Admin page.
- If I need to change the status of an issue I can change it. 

### Process

I went through the user stories and wireframes before embarking on the actual coding of the project to ensure I had a good idea of how to approach things. 

## Features
Throughout the project I have use bootstrap as it is a modern, responsive front-end framework. It has ensured that every page of the project is 
consistent in its design and layout. 

#### Main Page
If the user hasn't logged in there will be a message asking them to do so with a link to the login page. Once the user has logged in then there will be a welcome 
message showing their username. 

#### Navigation:
There is a  header at the top of the page which includes some menu items to take you to different parts of the website. 
On small screens the navigation menu disappears and a burger icon button appears so that the menu can be toggled on or off. 
When each menu item is hovered over there is a transition to a different colour so that the user can see which menu item is being hovered over. 

#### Footer:
At the bottom of the page there are links to various social media including Twitter, LinkedIN, GitHub and Instagram. 
When the links are clicked then a new page is opened up showing the social media page. 

## Technologies Used

The following technologies have all been used during the coding of this project:

- [Bootstrap](https://getbootstrap.com/) The project is built with the use of bootstrap as it is responsive and enables fast development. 
- [JQuery](https://jquery.com/). This was used for the gaming functionality. 
- [FontAwesome](https://fontawesome.com/) I used FontAwesome for the icons shown in the footer for the social links. 
- [GitHub](https://github.com/darrenmessenger/cookbook) I used GitHub for version control. 
- [Heroku](https://python-cookbook-project-dm.herokuapp.com) I used Heroku to publish the site. 
 
## Testing

The HTML and CSS code used on this project has been tested using The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) 
and The [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input).

The project has been tested on Google Chrome (desktop and mobile versions), Mozilla Firefox and Microsoft Edge. 

Every other aspect of the site has been tested as described below.

### Responsive Testing
I utilised Bootstrap so that the whole site would be responsive on different platforms. 

On a large and medium screen the full navigation menu is displayed. 

On a small screen the menu items disappear and a burger button appears which, when clicked, displays the menu items.

### General Testing

I went through each of the User Stories to make sure that they worked as expected. 

| User Story | Result |
| ---------- | ------ |
| Home Page: |  |
| There should be a Navbar with a Login and Register link.| **PASSED** |
| If the format of the fields are incorrect then I will receive an error message.| **PASSED** |
| If the username already exists then I will receive an error message.| **PASSED** |
| Outstanding Issues Page
| All of the issues should be displayed.| **PASSED** |
| If the issue is a bug it should have an image of a bug next to the ticket.| **PASSED** |
| If the issue is a new feature it should have an image showing 'new'.| **PASSED** |
| I should be able to see the basic details of the ticket. | **PASSED** |
| I should be able to click on the upvote button and vote for the ticket. | **PASSED** |
| If I click on the upvote button it will vote for the issue and take me to the ticket details. | **PASSED** |
| I should be able to see the status of each of the tickets. | **PASSED** |
| I should be able to click on a button so that I can read more about the issue. | **PASSED** |
| If I click on the Read More button I will be taken to the Issue Detail page.| **PASSED** |
| Issue Detail:
| I should be able to see all of the details of the issue. | **PASSED** |
| If the issue is a bug it should have an image of a bug.| **PASSED** |
| If the issue is a new feature it should have an image showing 'new'.| **PASSED** |
| I should be able to click on the upvote button and vote for the ticket. | **PASSED** |
| If I click on the upvote button it will vote for the issue and refresh the page. | **PASSED** |
| I should be able to see if an image has been added to the ticket. | **PASSED** |
| I should see a compressed version of the image.| **PASSED** |
| If I click on the image it should 'zoom' in and show the image in more detail. | **PASSED** |
| I should be able to click on a button to take me back to the Outstanding Issues Page.| **PASSED** |
| I should be able to click on a button to allow me to edit the ticket. | **PASSED** |
| I should be able to see all of the comments that have been added to the ticket. | **PASSED** |
| If I am signed in I should be able to add a comment to the ticket. | **PASSED** |
| If I am not signed in I should see a message stating that I need to sign in to add a comment. | **PASSED** |
| New Issue Page:
| When the page is loaded I should see the descriptions of each section that can be entered. | **PASSED** |
| I should be able to enter the details of the issue.| **PASSED** |
| I should be able to add an image of the issue.| **PASSED** |
| If I leave a section blank then I should see an error message when I try to create the issue.| **PASSED** |
| I should be able to click on the ticket type and see a drop down list which is selectable.| **PASSED** |
| I should be able to click on a button to create the issue. | **PASSED** |
| If I click on the button to create the issue I should be taken to the outstanding issues page.| **PASSED** |
| Payments Page:
| If I click on the donate button I will be taken to the Payments Page.| **PASSED** |
| If I enter my payment details correctly and press the submit button I will be charged the desired amount.| **PASSED** |
| If I enter any incoorect values I will see an error message.| **PASSED** |
| After the submit button has been pressed and the payment is successful I will see the home page with a confirmation message.| **PASSED** |
| Profile page:
| If I click on the person icon in the nav bar I will be taken to the profile page.| **PASSED** |
| I will see basic details of my profile along with a donate button.| **PASSED** |
| If I click on the donate button I will be taken to the Payments Page.| **PASSED** |
| Admin Page:
| If I need to delete an issue then I can do so from the Admin page.| **PASSED** |
| If I need to change the status of an issue I can change it. | **PASSED** |


### Jasmine Testing 

This project did not give me the opportunity to use Jasmine testing as the functions simply ran without returning a value or called another function. 

## Deployment 

This project was deployed through Heroku. 

Following steps were taken to deploy the website:

In app.py I changed debug=True to debug=False as debug=True is used for debugging during development. 
debug=False is is for deployment to a production server.

In Cloud9 open up a command line and type ‘heroku’. That will show that heroku is already installed. 

Type ‘heroku login -i’ to login to your heroku account. Type ‘heroku apps’ to show the apps in your account. 

To create an app on Heroku you can either do it directly on Heroku or run the following command:
```
heroku apps:create python-cookbook-project-dm
```

Copy the heroku git URL from the setting page of heroku and enter the following command on Cloud9:
```
git remote add heroku https://git.heroku.com/thorin-and-company-dm.git
```

Then run the following command to see the remote git attached to your project:
```
git remote -v
```

If you haven’t added the files to Heroku yet then you will have to run the following command:
```
git add .
```
And then commit the changes:
```
git commit -m “Deployment to Heroku”
```
Type the following command to push the project to heroku:
```
git push -u heroku master
```

To create a requirements.txt file run the following command:
```
sudo pip3 freeze --local > requirements.txt
```
Then:
```
git add requirements.txt
```
```
git commit -m "Add requirements file"
```
```
git push -u heroku master
```
We then need to create a Procfile with the following commands:
```
echo web: python run.py > Procfile
```
```
git add Procfile
```
```
git commit -m "Add Procfile"
```
```
git push -u heroku master
```
In heroku app, inside the settings, clicked Config Vars, and set IP, PORT and environment variable MONGO_URI.
Clicked 'Open app' and the website was up and running.



Anyone can download the project or clone it from GitHub [here](https://github.com/darrenmessenger/cookbook) 

The live website can be found [here](http://python-cookbook-project-dm.herokuapp.com/).

### Cloning

If you wish to clone this project then you can click on the green 'Clone or download' button on [this](https://github.com/darrenmessenger/cookbook) page, and then download the .zip file. 

Unzip the file into the directory you prefer on your computer or cloud drive and then import it into your favourite IDE. 

Clone the repository
```
git clone https://github.com/darrenmessenger/cookbook.git
```

Move into the folder
```
cd directoty-name
```

You will need to install the dependencies found in the requirements.txt file:
```
pip3 freeze --local > requirements.txt
```
 
Then run:
```
sudo pip3 install flask-pymongo 
```
```
sudo pip3 install dnspython
```

To run the project locally use:
```
python3 app.py runserver
```

### Keeping MongoDB Password Private

Go to the MongoDB Atlas DB and click on ‘Connect’. Select ‘Connect Your Application’ and then click on the ‘Short SRV Connection String’ and copy the text. 

Go to cloud9 and enter in a command terminal:
```
Cd ..
nano .bashrc
```

Near the top of the opened file enter:
```
export MONGO_URI="mongodb+srv://root:r00tUser@cluster0-nogor.mongodb.net/cookbook?retryWrites=true&w=majority"
```    
Where the address in quotes is what you have just copied. Remember to change the database name and the password. Press CTRL X to exit, Y to save then Enter for the filename.

Close the Terminal and reopen it so that the changes take effect.

Type the following in a terminal to show the connection string:
```
echo $MONGO_URI
```
Edit app.py with the following so that you can connect to MongoDB:
```
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)
```

## Credits

I would like to thank all of the Code Institute students that helped throughout this project on Slack. 






