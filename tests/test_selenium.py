from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import pytest

#initialise site loading
class Test():
        
    @pytest.fixture()
    def test_setup():
        global driver
        #driver points to driver location
        driver = Firefox()
        driver = webdriver.Firefox(executable_path="/driver/geckodriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://127.0.0.1:5000/")
        yield
        driver.close()
        driver.quit()



    def test_register():
        driver.find_element(By.NAME, "Register").click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("username").send_keys("Ronald Mcdonald")
        driver.find_element_by_id("email").send_keys("RonaldMcdonald@hotmail.com")
        driver.find_element_by_id("password").send_keys("pa33w0rd")
        driver.find_element_by_id("confirm_password").send_keys("pa33w0rd")
        driver.find_element(By.NAME, "Sign Up").click()
        driver.implicitly_wait(10)

        get_title = driver.title
        assert get_title == "Login"


    #test if login is successful
    def test_login():
        driver.find_element_by_id("email").send_keys("RonaldMcdonald@hotmail.com")
        driver.find_element_by_id("password").send_keys("pa33w0rd")
        driver.find_element(By.NAME, "remember").click()
        driver.find_element(By.NAME, "Login").click()
        driver.implicitly_wait(10)

        get_title = driver.title
        assert get_title == "My Lists"

    #Tests creating/deleting listsd with different syntax.
    def test_mylists():
        driver.find_element_by_id("new_list_name").send_keys("Shopping List")
        driver.find_element_by_id("new_list_description").send_keys("A cool list of thing I need to buy so I do not starve")
        driver.find_element(By.NAME, "submit").click()
        driver.implicitly_wait(5)

        get_title = driver.find_element(By.NAME, "Shopping List")
        assert get_title == "Shopping List"

        driver.find_element_by_id("new_list_name").send_keys("Friends List")
        driver.find_element_by_id("new_list_description").send_keys("A cool list of thing I need to buy so I do not starve")
        driver.find_element(By.NAME, "submit").click()
        driver.implicitly_wait(5)

        driver.find_element_by_id("new_list_name").send_keys("Shopping List")
        driver.find_element_by_id("new_list_description").send_keys("A cool list of thing I need to buy so I do not starve")
        driver.find_element(By.NAME, "submit").click()
        driver.implicitly_wait(5)



 
    def test_lists_items():
        driver.find_element_by_id("email").send_keys("RonaldMcdonald@hotmail.com")
        driver.find_element_by_id("password").send_keys("pa33w0rd")
        driver.find_element(By.NAME, "remember").click()
        driver.find_element(By.NAME, "Login").click()
        driver.implicitly_wait(10)

