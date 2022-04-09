<div id="top"></div>

<h1 align="center">Music Playlist Application</h1>
  <br>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="/images/4375050_logo_python_icon.svg" alt="Logo" width="100" height="100"><img src="/images/317755_badge_html_html5_achievement_award_icon.png" alt="Logo" width="100" height="100"><img src="images/4691324_flask_icon.png" alt="Logo" width="100" height="100">
</div>


1. [ Project Brief. ](#brief)
2. [ Planning. ](#planning)
3. [User Stories](#user)
4. [Creating the Database](#createdb)
5. [Walkthrough](#video)
6. [CRUD](#crud)
7. [Technical Build Requirement](#build)
8. [Testing](#test)
9. [Automation](#automation)
10. [Issues](#issues)
11. [Future Consideration](#future)

  
<!-- ABOUT THE PROJECT -->
## project brief
<a name="brief"/>
The project is a CRUD application built with the technologies outlined below.  The workspace was created by using tables created in MySQL connected to database server and a Virtual Machine created in Google Cloud.  The specifics of the app are to give users the ability to create a list of their favourite musicians/artists, add tracks to the artists and then generate a list of musicians and their music.  The update and delete functionality allows users to delete tracks from the list and to change the name of the artist.

Essentially the application is designed to demonstrate the implementation of learning gained and meets the following requirements

| Requirement | Detail |
| --- | --- |
| Trello board  | Kanban board withfull expansion on user stories, use cases, tasks and issues within the project.|
| Relational Database | persistent storage with at least 2 tables in it |
| Clear Documentation | Design phases, architecture and risk assessment |
| CRUD application | Create an app which Reads, Creates, Updates and Deletes Using Python best practices |
| Fully designed test suites | create and run automated tests to provide a high level of coverage |
| Functioning front-end | Create an integrated API and front end using Flask |

## Planning 
<a name="planning"/>
The planning stage involved the use of Trello as a project management tool where a workboard was created to hold the User Stories and to record the progress of the various build stages of the application

<br />
<div align="center">
    <img src="images/trello.PNG" alt="Logo" width="1000" height="400">
</div>

### User Stories 
<a name="user"/>
implemented:

* As a User I want to be able to enter a track name and an artist name, so that I can create a record of my favourite music

* As a User I want to be able to retrieve a list of the tracks I have saved in the database, so I can view them.

* As a User I want to be able to edit the Artist details so I can change the name of the Artist.

* As a User I want to be able to delete tracks that I have added as my tastes might change.

not implemented

* As a User I want to create records about my favourite artists so I can check their gig schedule and access their musician webpage.


## Creating the Database
<a name="createdb"/>
The database was created using mySQL and the initial plan was to create three tables.  One to hold data for Artists, one to hold data for Tracks (one artist to many tracks) and one table to hold data for Albums (many tracks to many artists).  However as the MVP involved creating two tables the tables Artist and Music were implemented first as these would form the core functionality of the application.  The EDR diagram shows the relationships for these tables.

<br />
<div align="center">
    <img src="images/ERD_model.PNG" alt="Logo" width="800" height="600">
</div>

The relationship between the tables is defined by the Artist ID which is then used as a foreign key within the Music table.

The app would work by a user entering the details of one of their favourite artists.  The add music would allow users to enter the favourite tracks and to then select the artist (artist choices being populated into a dropdown box) to add the track to the artist selected from the dropdown.  The app would then allow users to select the option to view a list of their music, to delete tracks and then to edit the artist name.   

<a name="video"/>

## Video walkthrough of the fuctioning app

   <span align="center"> [![Music application](images/musicapp.jpg)](https://youtu.be/yawTCBhiI3M) </span>

## CRUD
<a name="crud"/>
This functionality represents the CREATE, READ, UPDATE and DELETE aspects of data retrieval and manipulation.  For the project CRUD is implemented as follows:

* CREATE - Create Artists and Tracks
* READ   - View a list of the artists and tracks on one page
* UPDATE - To update the Artist name
* DELETE - To delete a track from the database

### Technical Build Requirements
<a name="build"/>
* [python 3 ](https://www.python.org/about/) 
* [Flask](https://flask.palletsprojects.com/en/2.1.x/?msclkid=9eb344a1b67511ec879f0992ab58cf87#user-s-guide)
* [Jinga](https://palletsprojects.com/p/jinja/)
* [mySQL](https://dev.mysql.com/doc/)
* [Google Cloud Platform](https://cloud.google.com/docs)

The app uses python3 which is a high level scripting programming language which integrates Flask as a lightweight micro-framework for developing web applications.  The HTML pages were created using Jinga which is a fast extensible templating engine.

In terms of infrastructure the database server was hosted by Google Cloud platform and used a Virtual Machine to connect mySQL to VScode where a cloned down Github hosted repository holds the source code.

<div align="center">
    <img src="images/architecture.png" alt="Logo" width="800" height="600">
</div>

## TESTING
<a name="test"/>
Once the application code was in place and the app was functioning correctly testing was implemented.  Usually the Test Driven Development would be the process to follow (i.e. writing tests before the code and writing the code so the tests pass), however as the project forms part of a wider learning and training exercise this was not an expectation.

What is a test - "In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect."
https://docs.pytest.org/en/7.1.x/explanation/anatomy.html

Two types of tests were implement 
* [pytest ](https://docs.pytest.org/en/7.1.x/index.html) - tests which passed if the running code gave expected results
* [Pytest Coverage] (https://pypi.org/project/pytest-cov/) - a report which indicated the percentage of which the tests covered the entirety of the code base.

##Pytest

#testbase
Pytest essentially allowed a test application to be created which ran through all of the build steps including creating the database, tables and then adding in test data.  In this case a "test artist" and "test track" were added into the created database tables and the test ensured that the data had been successfully added into the tables.

In this case a "test artist" and "test track" were added into the created database tables.  Once the data was inside the tables assertions were made that 

<a name="issues"/>
## ISSUES
