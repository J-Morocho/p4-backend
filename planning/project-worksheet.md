# **<p align="center">Plantr</p>**

# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Incomplete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Incomplete
|Day 2| Working RestAPI | Incomplete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Incomplete
|Day 4| MVP & Bug Fixes | Incomplete
|Day 5| Final Touches and Present | Incomplete

## Project Description

A simple dashboard for making sure your plants are getting the care they need. The preliminary version of Plantr allows you to track whether your plants have been watered.

## Google Sheet

https://docs.google.com/spreadsheets/d/1MiYUM5Rr0hr_9kbYVNgYzxu88jngsMA9udl1Ox-z7Vw/edit#gid=0

## Wireframes (Frontend)

- [Mobile](https://res.cloudinary.com/jcloud3zf/image/upload/v1600001397/project-4/plantr-mobile_q8yfnw.png)
- [Desktop](https://res.cloudinary.com/jcloud3zf/image/upload/v1600001379/project-4/p4-desktop_crum2i.png)

## Time/Priority Matrix 


#### MVP 

- Registration is required in order to utilize this API
- Once logged in the user is presented with a dashboard that has a sidebar containing the categories they've registered as well
as a list of plants within those categories
- In order to begin tracking plants the user will need to create a category and add the desired plant to it
- Registration of categories begins in the sidebar, a modal will open up that allows the user to create a new category if they wish
- Once a category is created the main page will display a button allowing a user to add a plant
- Plants have a name, description, as well as a required category that can be defined
- Once a plant is created its information is displayed on the page along with tracking details

#### PostMVP 

- Functionality that allows tracking of ambient temperature and amount of light recieved
- Search for plants where needs have not been met


## Functional Components

- Routes for creating categories and plants
- User authentication
- Update plant is_watered column
- Delete routes for plants and categories


#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Planning / structure| H | 1hr | 1.5hr | 1.5hr|
| Deployment | H | 1hr | 1hr | 1hr|
| Create Category| H | 3hr | -hr | -hr|
| GET all plants in category| H | 2hr | -hr | -hr |
| Update plant | H | 1hr | 0.5hr | 0.5hr |
| Authentication | H | 3hr| 1.5hr | 1.5hr|
| Total | H | 11 hrs| hrs | -hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Create water table | 3hr | -hr| -hr|
| Ambient temperature | 6hr| -hr| -hr|
| Light recieved | 6hr | -hr | -hr|
| Total | H | 15hrs| -hrs | -hrs |

## Additional Libraries

- djangorestframework
- djangorestframework-jwt
- django_extensions
- django_heroku

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

