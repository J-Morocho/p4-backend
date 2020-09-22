# **<p align="center">Plantr</p>**

# Project Overview

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 2| Working RestAPI | Complete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Complete
|Day 4| MVP & Bug Fixes | Complete
|Day 5| Final Touches and Present | Complete

## Project Description

A simple dashboard for making sure your plants are getting the care they need. The preliminary version of Plantr allows you to track whether your plants have been watered.

## Google Sheet

https://docs.google.com/spreadsheets/d/1MiYUM5Rr0hr_9kbYVNgYzxu88jngsMA9udl1Ox-z7Vw/edit#gid=0

## Wireframes (Frontend)

- [Mobile](https://res.cloudinary.com/jcloud3zf/image/upload/v1600001397/project-4/plantr-mobile_q8yfnw.png)
- [Desktop](https://res.cloudinary.com/jcloud3zf/image/upload/v1600001379/project-4/p4-desktop_crum2i.png)

## Time/Priority Matrix 

- [Matrix](https://res.cloudinary.com/jcloud3zf/image/upload/v1600083025/project-4/p4backend-matrix_hfsil9.png)

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
| Create Category| H | 3hr | 3hr | 3hr|
| GET all plants in category| H | 2hr | 1.5hr | 1.5hr |
| Update plant | H | 1hr | 0.5hr | 0.5hr |
| Authentication | H | 3hr| 1.5hr | 1.5hr|
| Total | H | 11 hrs| 9 hrs | 9 hrs |

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
- corsheaders

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

I enjoyed figuring out how i would be able to keep track of the last time the plant was watered at and using the frequency to check whether the user will be allowed to perform a watering or not.

```javascript
class Plant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='plants', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # No image_url in default plant instance
    image_url = models.URLField(blank=True, null=True)
    is_watered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # frequency = 2 (twice a day)
    frequency = models.IntegerField(default=False)
    # curr time we watered
    watered_at = models.DateTimeField(null=True, blank=True)
    # Increment water count when watered_at is updated
    # if watered_count exceeds frequency then alert user
    watered_count = models.IntegerField(default=False)
```

## Issues and Resolutions

**ERROR**: Uncaught (in promise) TypeError: Failed to fetch                                
**RESOLUTION**: Needed to ensure i passed in the correct headers/url/method along with the fetch request

