### gr_project1
# Game Review Project

## Contents:
* [Introduction](#Introduction)  
* [Design Ideas](#Design-Ideas)
* [Design Documents](#Design-Documents)  
* [Test driven development](#Test-driven-development)
* [CI Pipeline](#CI-Pipeline)
* [Reflections on the project](#Reflections-on-the-project)

---
# Introduction

<p>For this project i will be expected to make a Flask Application that will contain at least 2 databases, where i will have to apply C(reate)R(ead)U(pdate)D(elete) methods.<br>
The project i have chosen to use as my base topic will be around a games review style, being able to use the front end URL to input data to the tables.
The user should be able to navigate easily through the application, having a search function and a field to read add update or delete data from the database.
I will also have all the documentation that has been part of the design process, coding and AGILE methodoligies.<br>
This will include:</p>
        <ul>
            -A trello board to keep track of progress and goals<br>
            -A risk assessment to document all the potential threats and issues my project may encounter<br>
            -An ERD and chen diagram to display the functionality and relationships between my database<br>
            -SQL relational database for incorporating the usability of my database<br>
            -Testing documentation, to prove the functionality of my code<br>
            -A functioning front end flask website<br>
            -A collection of all the files and folders in a GIT repository with no additional unnecessary files<br>
            -AWS instance of external RDS database 
            -Flask app in a stand-alone Jenkins VM with the use of .systemd and Gunicorn
            -webhooks from Jenkins for CI purposes
        </ul>
will be also keeping any changes or updates in a log, to see how the project varied due to issues or compatability with the project criteria.

---

# Design Ideas
## First iteration of the project

My initial idea for this project was based upon a forum, the use of a user id to connect to a games database and add titles and multiple reviews for that title along with the nickname chosen as a form of identity for the input.<br>

![first_erd](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/games_review_erd.png)

This project required a database that will hold three tables, one for Games, one for user ID and the other for Reviews.

In the games table, it will hold a unique id for the game added, then brief information about the game: ID, title, genre.

In the user ID, it will have : ID and User Name

In the Review table, there will be an id for the input of review, a space to create a review on the game: Review ID, game ID, (game)title, (user)Nickname, personal rating 1/10, review.

The navigation of the tables will be straight-forward and easily readable on the game which you select.

It will offer you to pick a game, add a game or remove a game. In the reviews table, you will be able to add your own review and see others reviews. You will also be able to sort the games in rating order to see what was best to worst/vice versa.



---

# Second iteration of the project

The second idea i had for the project fit not only the potential to hit MVP, but was also a large margin more achievable with the time alotted and the level of my current skills.

This version contained a similar scope, without the use of a USER table, more an open style games list, where you could add a game along with information about that game. Keep that data in a list and access it. Then via access to the game title via dropdown, it would display info on the game, and a new missions list. The missions displayed as a checkbox for confirmation of acheiving the goal, a text box to contain the mission text, and a date confirming when this was added.

![erd2](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/games_review_erd2.png)

---
This consists of 2 tables:
            The first table Games contains game_id, title, genre, rating, developers.
            The second table Mission_List contains id, game_id, mission_text, checklist and date.

This will give the option to add a new game with the details to a dropdown/list, and from there the user will be able to select the game, find the details about the game, and then a place to input the mission text.

The CRUD part of this project will be mainly in the mission text area, where the user will be able to CREATE, READ, UPDATE, DELETE information in and out of this area.

---

# Design Documents

Throughout the project, the use of 3 different methods of documentation helped with the organisation, structure and layout. I have relied heavily on the use of Trello to help keep the project on track and punctual to a reasonable to-do schedule. I also have kept track of the risks that became present within the development of the project.

## Risk Assessment

This is the documentation of each problem faced and how/when these issues where faced, including some issues that could have possibly arrived anywhere throughout the project. This is important for understanding how to keep track of potential hazards, knowing how to either resolve or avoid them in present and future projects.

![riskassess](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/Risk%20assessment.PNG)

## Project Tracking

My Trello board for the project containing what the epic and viable MVP consisted of, broken down into User stories. With the use of MoSCoW it was determined what would be implemented in the project via MVP criteria and the design idea. The Trello contained 2 major sprint goals, one would be for the documentation and building of the Flask application. The second being about the testing and eventual stand-alone functionality via Jenkins in my CI pipeline.

[Game Project Trello](https://trello.com/b/SXNfbIYg/game-review-project)

---
![trello](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/Trello2.PNG)

## Version Control

The project was primarily managed through the use of GitHub, a online public cloud service for storing and collecting data and files. This was used as a way to keep iterations of my project at different stages broken off into featurebranch for daily input, dev as a stage before deployment, and main as my final staging at the end of the project.

![Github](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/Git1.PNG)

__________________________________________________________________________________________________________________________

# Test driven development

Testing the project at intervals had changed the overall design and functionality within the project, primarily at the Flask and CRUD stages.

For the purpose of hitting MVP removing elements that where more tricky and would have put the project behind schedule. One of these issues being the use of a dropdown box with read functionality that also acted as a hyperlink.

![dropdown](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/list1.PNG)

Also the use of a checkbox in the missions html to confirm that an action had been done. This presented issues by breaking the first line of the {% for %} statement, and would show only above everything else. This was an addition feature placed in the backlog and would have only been revisited as a Could Have.

![checkb1](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/checkbox1.PNG)
![checkb2](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/checkbox2.PNG)

---

# Front End FlaskApp

Using Flask as a format for a html builder, using a sql-type database layout with the fields necessary to use the methods of CRUD within the app. Using the models as a schema for the database, the forms as a method of calling the information within the model, routes for implementing python methodologies and locations for your forms, and templates as the front end section of your html format app.

My home page covers the creating and read methods for adding a Game to the first model table.
![front end1](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/fr1.PNG)
Second page lists the games in an order where you can select the game you would like to see more information on and add missions to, along with the ability to update and delete games from this list.
![front end2](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/fr2.PNG)
Third page is where the games information is displayed as static text, above an area where mission data is added to the third table, from here you can create update and delete missions.
![front end3](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/fr3.PNG)
This is the page for updating the games using both Get and Post
![front end4](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/fr4.PNG)
This is the page for updating missions, where it traces the id of the game and the mission.
![front end5](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/fr5.PNG)

---

# Unit and integration testing
After the flask app has been completed, the next step is to check the use of each element within that app. Utilising Pytest-cov for Unit Testing, coverage of the code is tested with dummy information to see if the results will display on the receiving end. Selenium is used for integration testing via drivers as a click and type bot, simulating human interaction.

With unit testing, i acheived an 92% total coverage on my unit tests and passed 9/9 for each route.
![testing1](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/Coverage.PNG)

Here are some of the tests covered by my attempt of integration testing
![testing2](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/SeleniumTest.PNG)

---

# CI Pipeline
With the use of Jenkins, the project could utilise a continuous integration pipeline, assisting with transferring data directly to the standalone after development via use of GitHub and Webhook. The use of 2 instances within jenkins, one for the stand-alone web app, with the application of systemd files to complete the build, along with gunicorn. And the other instance for testing purposes with both unit and integration testing. 
![jenkins](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/pipeline.PNG)

---

# Reflections on the project

Throughout this project there have been peaks and troughs of times where i have struggled, and those that have come easier. But overall, this has been a great learning experience, teaching the methods in a mock real-world job. I have understood alot more about coding as a whole, and am happy to see it reflect in the work i have produced. But not everything was convenient, and left me at a standstill with work for a long period of time.

### What went well
The initial stages of this project, creating my documents and early flask files, models and forms seemed to pass by quite quickly. I would say even from some of the harder challenges, getting routes set up with full CRUD functionality and setting up the Jenkins VM with my app have all been good high points in the project. I like the look of my front end, and feel proud of my acheivement. 
 
### What went badly or could have been better
The route section of the Flask project was arguably one of the hardest sections in this project. Understanding python functionality in a code environment without being able to physically see results was difficult. I also would have liked to have jenkins running with a webhook. Avoiding merge issues and organising my GitHub better and labelling my branches in a clearer manner at less intervals.
![conflict](https://github.com/Arcticleech/gr_project1/blob/dev/rmimages/Mergeconflict.PNG)

### How i can improve
Ideally i would like to see improvements in the ability to read and visualise code, but as improvements to the project, my backlog of things i would have like to implement, a checkbox, a proffessional looking front end, and better time keeping for a more efficient and smooth transition through the project.





