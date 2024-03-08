# TASK NINJA

## Table of contents

- [Overview](#overview)
  - [About](#about)
  - [Demo](#demo)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
- [Author](#author)

## Overview

### About

To-do list / task manager web app where you can log in as a user and create or schedule daily tasks that you need to complete. 

Users should be able to:

- Reguster an Account
- Create daily tasks
- Track of your monthly goals
- View the 'Quote of The Day' via API call
- View Calendar view of tasks
- Schedule future tasks
- Update the account username, email and photo

### Demo

https://github.com/chleighton1/TaskNinja/assets/60336791/80f3d37e-295a-4e7a-aa62-0a68b5dd2e8c

### Links

- Live Site URL: [Link](https://taskninja.herokuapp.com)

## My process

I started by drawing out the main dashboard page with pen and paper. I also drew out some of the other pages like the calendar and the main splash page. I also spent some time drawing out how I wanted my database and tables to be structured and how they would relate to each other. Once I finished all that I then used HTML and CSS to put the pages mostly together then I created my python project using Flask to create the functionality of the program. The project consists of the following main elements:

-Forms using Flask WTF to receive input from the user: Registration, Login, submitting tasks or goals, updating the account and requesting a password reset. I made use of validators to make sure I was getting the right information and / or raise validation errors.
    
-Models for the database using SQLAlchemy. The main model is the 'Users' model. This contains the relevant user information as well as a relationship to the tasks and goals tables. Idea is that each user should only be able to see their own tasks and goals. I also have a Quote table, this is just to store the 'Quote of The Day' received from the API request, so I only need to make 1 request per day.
    
-Routes for all the different functionality of the website such as adding users/tasks/goals to the database, logging in and registering an account, passing the relevent information to each page(forms, datetime objects, images, etc.).
   
-Templates for all the HTML pages. I made a main 'layout' page and then extended that for all the remaining pages
    
-Calendar so you can schedule tasks for the future and see what you have for each day. I made use of HTMLCalendar but I wanted to change some of the functionality so I inherited it into my UserCalendar class and adjusted the functions I needed to get what I wanted. This included passing in specific class names and hrefs so you could click on a date and have it take you to a new page with that dates information(specific to that user).

-Postgres database


### Built with

- [Python](https://www.python.org/) - Python
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Python Framework
- [WTForms](https://flask-wtf.readthedocs.io/en/1.2.x/) - Forms Validation

## Author

- Website - [Charles Leighton](https://www.chleighton.live/)
