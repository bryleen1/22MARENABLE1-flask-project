# 22MARENABLE1-flask-project
## DevOps Core Fundamental Project
### **Author** – Bryleen Karimakwenda

## **Objective**
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.  
Deliverables to meet this objective includes:
* Managing project progress through the use of a Kanban Board
* Using a Cloud Hosted managed Database and Compute Engine.
*	Creating a Python based application with CRUD functionality
*	Unit Testing with Python (Pytest)
*	Producing a functional front-end using Flask (HTML)
*	Using Git version control
*	Automating processes using Jenkins

## **Project proposal**
I propose to make a flask web application that is simply a digital to-do list. This application will be hosted on a GCP virtual instance and will also use GCP’s database instance. The app will allow the user to input tasks, view tasks, update task inputs and delete tasks. This will fulfil the CRUD functionality requirement of the project.  
The CRUD functionality of this app is as follows:
* Create – Inputting tasks
* Read – Viewing tasks added
* Update – Editing the content of tasks in the database 
* Delete – Removing individual tasks from the database 

## **Project design**
After coming up with the project idea, I brainstormed my ideas for the app and then used the MoSCoW  prioritisation technique to decide what a minimum viable product would look like.  
**Must have**  
1. A column with tasks and a column that shows the date the column was added
2. An external database hosted on the cloud
3. Ability to update a task from the website and the database
4. Ability to delete a task from the website and the database
5. An external database hosted on the cloud  

**Should have**  
1. A progress column whereby the user could say whether they’ve completed or started the task  

**Could have**  
1. Option for users to send tasks to their emails so that they don’t have to be on the app to see their tasks  

**Won't have**  
1. A table that saves all the deleted data and updated data (before it is appended)
2. A registration and login page so that users can have accounts on the app and see their task history 
3. Weekly metrics of how many tasks the user completed and failed to complete  

Following prioritisation, I created user stories and acceptance criterias for the must have.  
User story:  
- As a user I want to write a list of tasks I have to complete so that I can keep track of what I have done and what I am yet to do.  
- As a user I want to see my tasks so that I can see what I have to do.   
- As a user I want to delete tasks so that I can remove tasks I have completed or no longer want to do.  
- As a user I want to edit tasks so that I can remove or add more information to my set tasks.  

Acceptance criteria:  
- Given the user is on the home page. When I enter a task and press the submit button then I should see an updated list of my tasks.
- Given the user is on the home page. I should see all my task entries and the date I entered them. 
- Given the user is on the home page. When I click delete then I should see an updated list of my tasks with the deleted task removed.  
- Given the user is on the home page. When I click update then I should be moved to another page and be able to append the task.  

### Kanban board
I generated the Kanban board, shown below, using Jira Software. This helped me farmiliarise myself with the software and visualise the tasks I had to complete for the project. The "Create a Flask Web App" had 3 child issues and the "Automate app processes using Jenkins" task had 2 child issues. Child issues are simply sub-tasks needed to be completed to complete the task.  
![image](https://user-images.githubusercontent.com/88090980/163737568-32c2b9ff-c9b9-4aa3-8fcc-74b2becc5818.png)

### Entity Relationships

### Risk Assessment  
Below is the risk assessment I developed for possible threats to the project. Some were noted before the project began whilst others where added on as I worked on project.  
![image](https://user-images.githubusercontent.com/88090980/163738265-6c53cd43-40e9-466f-9708-829359a2938d.png)  
_The Developer responsible is me (Bryleen)._  

## **Flask App Front-end**  

_Create_  

The user visits the app’s home page via the '/' URL suffix (seen in the image below). This page responds with the form and button for the user to add their task. Above the form you can see the column headers “Tasks, Added, Actions” but there is no data underneath the headers as no tasks have been set. The image below is what the original home page looked like before I moved the title to the middle and changed it to “My to-do list”. Following from this image, you will no longer see the title as “To-do list” with the writing aligned to the left.  

![image](https://user-images.githubusercontent.com/88090980/163738457-8771e4d1-707a-4c58-937f-fbade3ba2d7c.png)

_Read_  

Below is an image of what the home page looks like with several task entries. The Actions column has links to delete or update tasks. This action is replicated in the database. The Added column reveals the date the task was added. In the database, we can see the date and time a task was created or updated.  

![image](https://user-images.githubusercontent.com/88090980/163738671-7019720d-55ca-4176-bcc0-6f6cda4349e9.png)

_Update_  

When the user clicks update on the first task, the user is redirected to the page shown in the image below. Here the user can edit their previous input before being redicted to their home page (after clicking update task).  

![image](https://user-images.githubusercontent.com/88090980/163738859-e24cd87c-f132-463f-bf6c-1045576a821b.png)

In this example, the user adds "and clean sink" to the first task. This is shown in the image below.  
![image](https://user-images.githubusercontent.com/88090980/163738951-054670aa-6ec8-4b17-b1c1-de478d489486.png)

_Delete_  

When the user clicks delete on the first task, the task is removed from the list. This is depicted in the image below whereby the updated first task can no longer be seen.  

![image](https://user-images.githubusercontent.com/88090980/163739070-fb5e4726-8656-4a76-ad81-3203a955925a.png)

## Tests and automation  
As seen in the image below, 100% of my tests are found in the file tests_app.py in the tests folder and there is 83% coverage. The tests test the home page URL endpoint, that the database is working, that page redirections are followed and that tasks added by users are appearing on the page. Testing that the home page is functional is important as that is where the user will see their tasks as well as be able to make task entries. Testing database functionality is important as it reveals whether the app’s front-end is correctly interacting with the back-end or else a lot of data will not be collected, updated or deleted from the database. There are a lot of page redirections associated with POST actions so it was important to test that the pages are redirecting accordingly. To ensure 100% coverage, the update route should have been tested. I could have tested that folllowing an update, the page redirects and shows the updated task on the page and in the databse. Given more time, I would have added those tests.  

![image](https://user-images.githubusercontent.com/88090980/163739410-8b791387-e977-4edf-900c-90375fc1bc73.png)

At the time of testing, the app passes all of the tests ran and to automate this testing process, I installed Jenkins to run the tests for my app. Jenkins clones my GitHub repository, creates a virtual environment, installs my app’s required packages and runs my tests.  

![image](https://user-images.githubusercontent.com/88090980/163739702-ed41d416-f083-45af-90aa-716527ce50e3.png)
![image](https://user-images.githubusercontent.com/88090980/163739719-5609c17e-2d15-4cbe-a48a-a613c2b17efd.png)

The job was successful (which can be seen after the tests are run and from the green tick in front of “Console Output”). This means all steps in the job were completed without fail.  

## Future developments  

Although I managed to produce a viable application, I was only able to complete my must haves for the app and the app currently uses only 1 table (Todo). To upgrade to 2 tables and essentially, move along with other app developements listed in my MoSCoW, I would need to upgrade my table and also create a new user table. The updated version of my tables are as below:
![image](https://user-images.githubusercontent.com/88090980/163741322-697c7828-ac11-49a0-adf7-99731634d089.png)

The Todo2 table adds another column to my current table (seen in the image below). This would allow the app to to be able to identify which tasks belong to which user so as to send the right tasks to the correct user. An updated database is necessary for the next phase of this app, if the app is to send users' set tasks to their emails. The email will also contain the link to the app so that instead of just reading the tasks, the user can interact with them once more. After this phase, I would then look at creating accounts for users.  
![image](https://user-images.githubusercontent.com/88090980/163742158-002b59b6-03e0-4826-8bc5-7d14867218fd.png)



