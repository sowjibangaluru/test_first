
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Suite Setup       Open Browser    http://127.0.0.1:90/login    chrome
*** Test Cases ***
Successful Login Test
    Open Browser    http://127.0.0.1:90/login    browser=chrome
    Maximize Browser Window
    sleep    5sec
    Input Text         //input[@id='username']    valid_username
    Input Password     //input[@id='password']    valid_password
    Click Element      //button[@type='submit']
    sleep    5sec

Invalid Username Test
    Input Text         //input[@id='username']    invalid_username
    Input Password     //input[@id='password']    valid_password
    Click Element      //button[@type='submit']
    Wait Until Element Is Visible     //div[@class='alert alert-danger']
    sleep    5sec

Invalid Password Test
    Input Text         //input[@id='username']    valid_username
    Input Password     //input[@id='password']    invalid_password
    Click Element      //button[@type='submit']
    Wait Until Element Is Visible     //div[@class='alert alert-danger']
    sleep    5sec

Empty Username and Password Test
    Click Element      //button[@type='submit']
    Wait Until Element Is Visible     //div[@class='alert alert-danger']


