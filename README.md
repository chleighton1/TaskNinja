# TASK NINJA
#### Video Demo:  <https://youtu.be/92thatphIn4>
#### Website Link: <https://taskninja.herokuapp.com/>
#### Description:
This is my final project - TASK NINJA. The idea was to create a to-do list / task manager web app. Once I had the idea down, I started by drawing out the main dashboard page with pen and paper. I then used HTML and CSS to put it mostly together then I created my python project using Flask to create the funtionality of the program. The project consists of the following main elements:
    
-Forms using Flask WTF to receive input from the user: Registration, Login, submitting tasks or goals, updating the account and requesting a password reset.
    
-Models for the database using SQLAlchemy. The main model is the 'Users' model. This contains the relevent user information as well as a relationship to the tasks and goals tables. Idea is that each user should only be able to see their own tasks and goals. I also have a Quote table, this is just to store the 'Quote of The Day' received from the API request so I only need to make 1 request per day.
    
-Routes for all the different functionality of the website such as adding users/tasks/goals to the database, logging in and registering an account, passing the relevent information to each page(forms, datetime objects, images, etc.).
   
-Templates for all the HTML pages. I made a main 'layout' page and then extended that for all the remaining pages
    
-Calendar so you can schedule tasks for the future and see what you have for each day.  This took quite a while, I made use of HTMLCalendar but I wanted to change some of the functionality so I inherited it into my UserCalendar class and adjusted the functions I needed to get what I wanted. This included passing in specific class names and hrefs so you could click on a date and have it take you to a new page with that dates information(specific to that user).
    
I used a sqlite database but then switched to Postgres when I put it onto Heroku.  I also used some tutorials online to create a create_app function and structure my project into Blueprints. I think that is about it, hope you like it!

