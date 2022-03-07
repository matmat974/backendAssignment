# backendAssignment
Assignment on backend automation


## Overview
This documentation is contains of livestream functionality of kumu dev, staging, and prod environment
### Pre-Requisites
Python - Coding Language
behave - BDD Framework
allure-behave - Generating allure report


*To install the requirement.txt*
    
    pip install -r requirements.txt


###  Workflow
1. Login and the enviroment, account number, and the secret key are set on the terminal
2. Create, Start and End Livestream scenario are placed on **livestream.feature** file.
3. The execution of livestream feature are placed on livestream_step.py file
4. Report is generated via **Allure Report**

*To run script* 

    behave -D envUrl=<environment> -D otp_api_key=<secret key> -D cp_number=<account number>   features/livestream.feature   --no-capture --no-color


*To run script and select path for Allure Results*

    behave -D envUrl=<environment> -D otp_api_key=<secret key> -D cp_number=<account number>   features/livestream.feature   --no-capture --no-color -f allure_behave.formatter:AllureFormatter -o allure-report


*Generate allure report*

    allure serve <Absoulute path of your allure report folder> 