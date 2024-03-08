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

I began by sketching the main dashboard, along with other pages like the calendar and splash page, using pen and paper. I also outlined the structure of my database and its tables, considering their relationships. With that blueprint in mind:

1. **HTML/CSS:** I translated the sketches into web pages using HTML and CSS, focusing on layout and design.
2. **Python with Flask:** I initiated a Python project using Flask to implement the program's functionality. Here's an overview of the main elements:
   - **Forms:** Utilized Flask WTF to create forms for user registration, login, task/goal submission, account updates, and password reset. Integrated validators to ensure data integrity and handle validation errors effectively.
   - **Database Models:** Employed SQLAlchemy to define database models, with the central model being 'Users'. This model stored user information and maintained relationships with 'tasks' and 'goals' tables. The 'Quote' table was also added to store the 'Quote of The Day' obtained from an API request, ensuring only one request per day.
   - **Routes:** Implemented routes to handle various functionalities of the website, such as user/task/goal management, login/register actions, and passing necessary data to each page (e.g., forms, datetime objects, images).
   - **Templates:** Created HTML templates for all pages, utilizing a main 'layout' page and extending it for other pages for consistency.
   - **Calendar:** Integrated a calendar feature to schedule tasks and view daily plans. Initially utilized HTMLCalendar but customized its functionality by subclassing into 'UserCalendar', adapting necessary functions to enable user-specific actions such as clicking on dates to view individualized information.
3. **Postgres Database:** Utilized Postgres as the backend database to store user information, tasks, goals, and daily quotes.

This approach ensured a structured and functional web application with Flask, incorporating necessary features like forms, database management, routing, templating, and calendar integration to create a user-friendly experience.


### Built with

- [Python](https://www.python.org/) - Python
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Python Framework
- [WTForms](https://flask-wtf.readthedocs.io/en/1.2.x/) - Forms Validation

## Author

- Website - [Charles Leighton](https://www.chleighton.live/)
