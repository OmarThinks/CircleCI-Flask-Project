
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

There are 2 ways to run the application:
1. Open this file: **`src/app.sh`**

2. using CLI type these commands
<b>

```bash
export message="Hello, World!"
python app.py
```
</b>



### 3) src/test_.py:
This file contains the test of the application  
To run this file using CLI type this command:


There are 2 ways to test the application:

1. Open this file: **`src/test.sh`**

2. using CLI type these commands

<b>

```bash
export message="Hello, World!"
python test_.py
```
</b>



To run Using **pytest** and **pytest-html**:

<b>

```bash
export message="Hello, World!"
pytest
```
</b>

Just make sure that you have installed 
**pytest** and **pytest-html**


### 4) .circleci/config.yml:
This file contains that configurations of CircleCi







## Running using pytest:


When running using pytest, the testing results will be printed in this directory:

- **`test-reports/junit.html`**
- **`test-reports/pytest_report.html`**



In CircleCI, they will be artifacts.







# Explainging CircleCi configuraion file:


This is the code inside the file:



<b>


```yml
# Section 1
version: 2.1

# Section 3
executors:
  the_python_executor:
    docker:
      - image: circleci/python:3.7.4


# Section 3
commands:
  build_and_test_commands:
    steps:
      - checkout
      - run:
          name: Install Python dependencies
          command: |
            echo 'export PATH=~$PATH:~/.local/bin' >> $BASH_ENV && source $BASH_ENV
            pip install --user -r requirements.txt
      - run:
          name: Run unit tests
          command: |
            pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html --cov --cov-report=html:test-reports/pytest_cov_report
      - store_test_results:
          path: test-reports
      - store_artifacts:
          path: test-reports    

  test_env_variables_commands:
    parameters:
      p1:
        type: string
        default: "Passing a Parameter"
    steps:
      - run:
          name: Testing Env Vars
          command: |
            echo '$message' # Prints "$message"
            echo '${message}' # Prints "${message}"
            echo "$message" # Prints "*************"
            echo "${message}" # Prints "*************"
            echo $message # Prints "*************"
            echo ${message} # Prints "*************"
            echo "<< parameters.p1 >>"


# Section 4
jobs:
  build_and_test:
    executor: the_python_executor
    steps:
      - build_and_test_commands

  trying_env_vars:
    executor: the_python_executor
    parameters:
      p1:
        type: string
        default: "Passing a Parameter"
    steps:
      - test_env_variables_commands:
          p1: << parameters.p1 >>


# Section 5
orbs:
  # Declare a dependency on the welcome-orb
  welcome: circleci/welcome-orb@0.4.1


# Section 6
workflows:
  build_test_on_push:
    jobs:
      - build_and_test
      - trying_env_vars:
          p1: "Changed the parameter"
      - welcome/run
      - welcome/run:
          requires:
            - build_and_test

  build_test_on_cron:
    triggers:
      - schedule:
          cron: "1 1 * * *"
          filters:
            branches:
              only:
                - master
    jobs:
      - build_and_test
      - trying_env_vars:
          p1: "Changed the parameter"
      - welcome/run
      - welcome/run:
          requires:
            - build_and_test
```
</b>




## Section 1: Version:

This is the version of CircleCI config file.  
The latest version is 2.  
So we will use this version.  
**Note:** There is lots of difference between version 1 and 2



## Section 2: Executors:

Executors are the environment that the application will run inside.    
Here we will run the application inside a Docker environment and the 
main image is python.




## Section 3: Commands:

Commands are fixed steps that are repeated.  
The commands are used in jobs.  
Commands have parameters.  




## Section 4: Jobs:

This is what will be executed  in the workflow.





## Section 5: Orbs:

Predefined jobs





## Section 6: Workflows:

The final product of the circleci Configuration file



































