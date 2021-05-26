
[![CircleCI](https://circleci.com/gh/OmarThinks/CircleCI-Flask-Project.svg?style=svg)](https://circleci.com/gh/OmarThinks/CircleCI-Flask-Project)
[![CircleCI Build Status](https://circleci.com/gh/OmarThinks/CircleCI-Flask-Project.svg?style=shield "CircleCI Build Status")](https://circleci.com/gh/OmarThinks/CircleCI-Flask-Project) 
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/OmarThinks/CircleCI-hello-world/master/LICENSE) 


# CircleCI-Flask-Project



## Files:


### 1) requirements.txt:
This file has all the requirements to run the application  
Flask, pytest, and pytest-html


### 2) src/app.py:
This file contains the flask application  
To run this file using CLI type this command:

<b>

```bash
python app.py
```
</b>



### 3) src/test_.py:
This file contains the test of the application  
To run this file using CLI type this command:

<b>

```bash
python test_.py
```
</b>



To run Using **pytest** and **pytest-html**:

<b>

```bash
pytest --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
```
</b>

Just make sure that you ahve installed 
**pytest** and **pytest-html**


### 4) .circleci/config.yml:
This file contains that confiurations of CircleCi








