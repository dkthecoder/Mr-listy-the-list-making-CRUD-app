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
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to design and produce a web app of my choosing. The app needed to have CRUD (create, read, update and delete) functionality, needed to use the Flask micro-framework, and had to store information in a MySQL database comprised of a minimum of two tables sharing a one-to-many relationship. This structure is represented below:  

INSERT APP STRUCTURE DIAGRAM
![app structure]()  

## App Design:
To demonstrate CRUD, I have chosen to build a list-making application, which allows users to:
* CREATE an account, lists and items within a list
* READ account details, lists and items of that list which belong to the user
* UPDATE a users account details, a list with items
* DELETE users account, lists and items within a list

The database for this project currently comprises of a "users" table, a "lists" table and an "items" table. Where one user can have many lists, and one list can have many items. The ERD for this MVP is shown below:  

INSERT ERD DIAGRAM
![ERD](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/Mr%20Listy%20ERD%20Database.png)

The goal for future iterations of this project would include additional functionality to mark items as done, archieve lists, share lists amongst other users (almost like a list social network).

WORK ON CI PIPELINE
## CI Pipeline:  


## Risk Assessment:
Prior to building the app, a risk assessment was undertaken to identify risks and propose measures to control these risks. These measures could then be implemented in the app. This initial risk assessment is shown below:   

INSERT RISK ASSESSMENT
![RA](https://github.com/dkthecoder/Mr-listy-the-list-making-CRUD-app/blob/main/figures/risk%20assessment.png)  
Some of the control measures implemented in the project as a result of the risk assessment are as follows:  

The likelihood and impact level (out of 5) of each risk identified were estimated before and after the implementation of control measures, to quantify the effect of implementing the measures.

## Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. As mentioned previously, these tests are automated using Jenkins via webhooks. A successful build, in which all tests passed, is shown below:  

![build]()  
The coverage reports, showing what percentage of statements were included in the tests, were output as html files, which were archived post-build. The coverage report for the above build was:  

![cov]()  
Showing 96% coverage overall. All tests must pass for a build to be successful, a single failed test marks the build overall as failed.

INSERT SCREENSHOTS OF THE APPL FUNCTIONING
# The App:  
Upon navigating to the app the user is presented with the homepage:  

![home]()  
The nav bar provides links which allow users to add a question, view questions and take the quiz. To add a question, the user simply fills in the name of the question on the form:  

![add question]()  
The user is then redirected to a page which allows them to add up to four options for the question. The view questions page displays a list of the questions which have been added so far, which are hyperlinked to allow the user to view, update and delete the associated options:  

![view questions]()  
Users can also update and delete questions, the app is set up so that deleting a question also removes the associated options.  

## Updates:
* 12/06/2021:
    * Background colour changed to a more pleasant dodger blue
    * __repr__ methods added to Questions and Options classes
    * Quiz class added
    * Questions can now be categorised by quiz
    * Different quizzes can now be taken independently

## Known Issues:
* User authentication needs to be enforced for viewing lists. To ensure a user cannot view another users list.
* Issues with storing DateTime into database causes an error. This issue occurs randomly.
* No HTTPS, can be enabled given a domain for Certbot and Nginx.
* When creating desacription for new list, using grammer may cause SQL errors.

## Future Work:
* Custom error pages
* Better handling of session conditionals (diferent page renders/redirects)
* Password verification for account deletion
