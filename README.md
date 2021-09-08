<h2>gr_project1</h2><br>
<h2>Game Review Project</h2>


<h1>Introduction.</h1>

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
        </ul>
<p> will be also keeping any changes or updates in a log, to see how the project varied due to issues or compatability with the project criteria. </p>

__________________________________________________________________________________________________________________________


<h1>Design Ideas</h1><br>

<h3>First iteration of the project</h3>

<p>My initial idea for this project was based upon a forum, the use of a user id to connect to a games database and add titles and multiple reviews for that title along with the nickname chosen as a form of identity for the input.<br>

This project required a database that will hold three tables, one for Games, one for user ID and the other for Reviews.<br><br>

In the games table, it will hold a unique id for the game added, then brief information about the game: ID, title, genre.<br><br>

In the user ID, it will have : ID and User Name<br><br>

In the Review table, there will be an id for the input of review, a space to create a review on the game: Review ID, game ID, (game)title, (user)Nickname, personal rating 1/10, review.<br><br>

The navigation of the tables will be straight-forward and easily readable on the game which you select.<br><br>

It will offer you to pick a game, add a game or remove a game. In the reviews table, you will be able to add your own review and see others reviews. You will also be able to sort the games in rating order to see what was best to worst/vice versa.</p>



__________________________________________________________________________________________________________________________

<h3>Second iteration of the project</h3>

<p>The second idea i had for the project fit not only the potential to hit MVP, but was also a large margin more achievable with the time alotted and the level of my current skills.</p>

<p>This version contained a similar scope, without the use of a USER table, more an open style games list, where you could add a game along with information about that game. Keep that data in a list and access it. Then via access to the game title via dropdown, it would display info on the game, and a new missions list. The missions displayed as a checkbox for confirmation of acheiving the goal, a text box to contain the mission text, and a date confirming when this was added.</p>

<p>This consists of 2 tables:<br>
            The first table Games contains game_id, title, genre, rating, developers.<br>
            The second table Mission_List contains id, game_id, mission_text, checklist and date.<br>

This will give the option to add a new game with the details to a dropdown list, and from there the user will be able to select the game, find the details about the game, and then a place to input the mission text.</p>

<p>The CRUD part of this project will be mainly in the mission text area, where the user will be able to CREATE, READ, UPDATE, DELETE information in and out of this area.</p>

__________________________________________________________________________________________________________________________

<h1>Design Documents<h1><br>

__________________________________________________________________________________________________________________________

<h1>Project Tracking<h1>

__________________________________________________________________________________________________________________________

<h1>Test driven development</h1>

__________________________________________________________________________________________________________________________

<h1>CI Pipeline</h1>

__________________________________________________________________________________________________________________________

<h1>Reflections on the project</h1><br>
<h3>What went well</h3><br>
<h3>What went badly or could have been better</h3><br>
<h3>How i can improve</h3><br>





