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
| Description     | Evaluation     | Likelihood     | Impact level     | Responsibility     | Response     | Control measure |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |


