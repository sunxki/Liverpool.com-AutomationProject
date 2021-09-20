# Liverpool.com-AutomationProject

This is the Automation suite for Liverpool.com.mx

## How to execute it (On Windows) 
  1. Clone the directory into your computer 
  2. Open CMD on windows
  3. cd to the directory where the repository was cloned (Make sure to navigate to the root folder) 
  4. input "py.test" command on the console
  5. The Webdriver will start executing the script 
  6. Once it has finished, navigate to /reports on your cloned directory and locate the new report for this run that was generated with all the details. 

Recording for the execution can be found on [here](https://www.screencast.com/t/jH26dYBD) 

## Other CMD customized commands 
### Selecting browser to execute scripts 
1. py.test -browser_name (default = **chrome**,   "firefox" available to run the script in geckodriver)

### Changing enviroment to execute scripts 
3. py.test -environment_name (default = **prod**,   "stg" available to get a different URL for another enviroment (Not provided))

## This automation suite was created  using the following tools:

- Selenium Webdriver 3.141.0 
- Python 3.9 
- [Pytest](https://docs.pytest.org/en/6.2.x/) as framework
- [ChromeDriver 92.0.4515.43](https://chromedriver.chromium.org/home) 
- Some custom libraries: 
-- [Requests](https://docs.python-requests.org/en/master/): For API call
--  [pytest-html](https://pytest-html.readthedocs.io/en/latest/index.html#) For reporting 

The suite is organized under Page Object Model (POM) , it contains the following directories, please below find a brief description of each one. 

### **pageObject**
It contains a class per each page involved on the required test cases,on these classes, constructors, locators and methods are declared and encapsulated. 
### **report**
This directory will be used to store the HTML reports once the pytest execution has finished 
### **testData**
It contains classes where the data use on each page is stored
### **test**

- **testCases:** It contain classes for the test cases required, it will inherent all the methods from pageObject classes where the object are created to performed the steps, assertion are included on this classes, as well   as data loader to bring data from testData classes.


        1. Search Bar
          As a consumer, I want to be capable to easily search for different types of articles so I can:
          Find one or more articles of my interest
          Be notified if there are no articles
          Search the articles by brand, physical characteristic, model
          
          ----
          
          
        2. Buying a Smart TV
        As a consumer, I want to be capable select a Smart TV from the catalog based on brand, size, and under a range of price so I can buy the best fit to my needs.
        
### **utilities**
It contains Base Class where all the recycled method are declared such as, API Call method,implicit waits, text generator and it was enherinted by all the test cases.
Additionally drivers for **Chrome** and **Firefox** are loaded here, required to run the scripts 
     
   
