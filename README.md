<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="/images/4375050_logo_python_icon.svg" alt="Logo" width="80" height="80">
</div>

<h3 align="center">Music Playlist Application</h3>
  <br>
  
<!-- ABOUT THE PROJECT -->
## project brief

## Video walkthrough of the fuctioning app
   <span align="center"> [![Music application](images/musicapp.jpg)](https://youtu.be/yawTCBhiI3M) </span>

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

## Getting Started



## Creating the Database

The database was created using mySQL and the initial plan was to create three tables.  One to hold data for Artists, one to hold data for Tracks (one artist to many tracks) and one table to hold data for Albums (many tracks to many artists).  However as the MVP involved creating two tables the tables Artist and Music were implemented first as these would form the core functionality of the application.  The EDR diagram shows the relationships for these tables.

<br />
<div align="center">
    <img src="images/ERD_model.png" alt="Logo" width="80" height="80">
</div>

insert ERD table




### Technical Build Requirements

* [python 3 ](https://www.python.org/about/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/?msclkid=9eb344a1b67511ec879f0992ab58cf87#user-s-guide)
* [Jinga](https://palletsprojects.com/p/jinja/)
* [mySQL](https://dev.mysql.com/doc/)
* [Google Cloud Platform](https://cloud.google.com/docs)



### User Stories 

implemented:

As a User I want to be able to enter a track name and an artist name, so that I can create a record of my favourite music

As a User I want to be able to retrieve a list of the tracks I have saved in the database, so I can view them.

As a User I want to be able to edit the Artist details so I can change the name of the Artist.

As a User I want to be able to delete tracks that I have added as my tastes might change.

not implemented

As a User I want to create records about my favourite artists so I can check their gig schedule and access their musician webpage.

### Built With

* [python 3 ](https://www.python.org/about/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/?msclkid=9eb344a1b67511ec879f0992ab58cf87#user-s-guide)
* [Jinga](https://palletsprojects.com/p/jinja/)
* [mySQL](https://dev.mysql.com/doc/)







<!-- GETTING STARTED -->


This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
