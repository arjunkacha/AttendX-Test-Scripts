# AttendX-Test-Scripts

## Project Description
This repository contains sample automated test scripts for the AttendX student attendance application.

## Test Scripts

### 1. login_test.py
Tests login functionality with valid credentials, an invalid password, and empty credentials.

### 2. attendance_marking_test.py
Tests attendance marking for Present and Absent statuses, an empty student ID, and an invalid attendance status.

## Requirements
- Python 3
- Git
- Visual Studio Code

## How to Run

Run the login tests:

```powershell
python -m unittest login_test.py -v
```

Run the attendance tests:

```powershell
python -m unittest attendance_marking_test.py -v
```

## Version Control
Git tracks changes to the test scripts, and GitHub stores the repository for collaboration among QA team members.

## Team Collaboration

GitHub is used as the remote repository for sharing test scripts.
Team members should pull the latest changes before starting work
and commit their updates with meaningful messages.
