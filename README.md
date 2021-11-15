# Mr Listy, The List Making App:
Mr Listy is a flask-based, bootstrap themes webapp which demonstrates CRUD functionality on a MySQL server. The project utilises Python, SQL, CSS and HTML, and demonstrates my skills and foresight in devops, project management, agile methodologies and HCI.

This repository is also part of the deliverables for the QA devops project.

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This structure is represented below:  

![app structure](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/page%20planning%20inverted.png?raw=true)  

## App Design:
To demonstrate CRUD, I have chosen to build a list-making application, which allows users to:
* CREATE an account, lists and items within a list
* READ account details, lists and items of that list which belong to the user
* UPDATE a list with items (optionally; user account details)
* DELETE lists, items within a list and users account.

The database for this project currently comprises of a "users" table, a "lists" table and an "items" table. Where one user can have many lists, and one list can have many items. The ERD for this MVP is shown below:  

INSERT ERD DIAGRAM
![ERD](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/Mr%20Listy%20ERD%20Database.png)

The goal for future iterations of this project would include additional functionality to mark items as done, archieve lists, share lists amongst other users (almost like a list social network).


## CI Pipeline:  
![KANBAN BACKLOG](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/kanban%20backlog.png?raw=true)

![KANBAN TIMELINE](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/jira%20kanban%20timeline.png?raw=true)

For deployment and automated testing Jenkins was utilised to itegrate between github, being triggued to develop a build once a new commit has been made. Testing would be automated as part of thebuild process in Jenkins.

## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. This initial risk assessment is shown below:   

INSERT RISK ASSESSMENT
![RA](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/risk%20assessment%20inverted.png)  
Some of the control measures implemented in the project as a result of the risk assessment are as follows:  

The likelihood and possibility/impact level (out of five (5), where one (1) is the lowest possibility/impact and five (5) being the greatest) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.


## Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. 


# The App:  

![home](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/screenshots/mrlisty-landing.png?raw=true)  
The index page is where the user is taken too upon accessing the webserver. The navigation bar links are conditional on the session status of the user.

![login register pages with validation prompts](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/screenshots/mrlisty-register%20login%20success%20fail.png?raw=true)  
The following screens show the login and register pages. Both pages share a unique layout template and also have built-in data validation. As visible with the prompts given to the user.

![login redirect, make list, delete list, add items to list](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/screenshots/mrlisty-my%20list%20list%20items%20delete%20list.png?raw=true)  
When the user has logged in, the session status changes and displays additional options on the navigation bar not present to a unregisterd or logged out user. As shown, the user can make lists, delete lists and add (and delete) items in the lists. If the user chooses to delete the list, the corresponding items associated to it are also deleted.

![my account, delete account prompt, account deleted prompt](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/screenshots/mrlisty-my%20account%20and%20delete%20promt.png?raw=true)  
The user can also access their account details and make changes to their account username, email and password. The user can also delete their user account where they will be prompted with a modal to confirm their choice. If confirmed, the lists, associated items and user details will be deleted, and session cleared. The user is redirected to the index and prompted with a delete confirmed notification.


## Known Issues:
* User authentication needs to be rectified and enforced for viewing lists.
* Sometimes storing DateTime into database causes an error (hard-to-reproduce bug),
* No HTTPS, can be enabled given a domain with Certbot and Nginx.
* When creating description for new list, special characters produce a SQL syntax error.

## Future Work:
* Custom error pages.
* Better handling of special characters in SQL CREATE statements.
* Password verification for account deletion.
* Use of enviroment variables.
* Password reset via email.
