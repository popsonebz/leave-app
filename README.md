# Leave application system
## To deploy this application straight into minikube
Note: The docker image has been hosted in dockerhub.

Visit to the kubernetes-deployment folder (https://github.com/popsonebz/leave-app/tree/master/kubernetes-deployment) and follow the instruction.

## Admin Operation

First of all, we need to add employees to the system

leave.com/admin/add-employee/

Note:

1. By default, all employees have 18 days of leave.
2. This page was just added based on initiative as it was not specified in the task.

## Employee Operation

1. To apply for leave, the employee visits this url

leave.com/leave/apply

2. He/She is redirected to the login page for authentication

3. If Authentication is successful, the application page is displayed.

4. On selecting the start and end dates, the following are checked:

- Neither start or end date can be less than the current date.
- The end date cannot be less than the start date.
- Start date cannot later than end date.
- End date cannot be the same as start date.
- Notify the user when there is no working days within the specified period.
- Preventing duration which exceeds the maximum 18 days of leave allocated.

### Automatically Decline the following leave application:

- Employees who have not spent up to 3 months in the company from appying for leave.
- Employee who has exhausted his leave.
- Employee taking more than the remaining leave days he has.


## Carrying Over Leave Not Taken

The system carry's over a maximum of 5 days leave.

This is done in the management command defined in leave/management/commands/carry_leave_over_the_year.py

The operation can be carried out in 2 ways:

1. Manually at the end of the year
```
   python manage.py carry_leave_over_the_year
```
2. Automatically by creating a linux crontab job which executes once a day to check if its the last day of the year.

if the condition is met, the command in option 1  will be executed.

## Selenium Functional Test

Note: To use the functional test, the following needs to be done:
1. Chrome webdriver needs to be downloaden and placed into the folder path (tanget_leave_app_solution/leave/)

2. The webdriver path needs to be set accordingly as seen in leave/test.py (the current path only works on my laptop).

3. Open the link <http://localhost:8010/admin/add-employee/>

4. Create the following users:
```
first name = kate, last name = perry, employment date = 01/01/2017, username = kate, password= kate

```
```
first name = ben, last name = carson, employment date = 29/05/2017, username = ben, password= ben

```

3. Then run the command:
```
   python manage.py test
```
