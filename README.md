# Progress Tracker App

A command line program using python 3 to help boot camp 
participants track their progress using the learning map.
A user is able to add skills, view a list of all the skills added, 
indicate the skills studied, view a list of skills I’ve studied, 
view a list of skills I haven’t studied yet and see their learning progress.

## Functionality
- `Add skill` Enables users to add skills
- `View skills` Enables to users to view added skills
- `Studied skills` Enables user to mark skill  as studied
- `View Studied skills` Enables users to see studied skills
- `Skills not studied` Enables to see skills not yet studied
- `Track progress` Enables user to track his/her proggress

## Requirements
`Python 3, click, python-pip, virtualenv

## Installation
First clone this repository.
```
$ https://github.com/PatrickCmd/progress_tracker
$ cd progress_tracker
```
Create virtual environment and activate it.
```
$ virtualenv env
$ source env/bin/activate
```
Then install the application.
` $ pip install --editable .`
## Run the application
To get help type on console
`$ tracker --help`
Run the application
`$ tracker --command=show_options`
