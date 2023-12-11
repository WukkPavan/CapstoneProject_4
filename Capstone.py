import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to initialize the browser
@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

#Verify title of the Home Page
def test_verify_home_page_title(setup):
    driver = setup
    driver.get("http://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title

#checkbox validations 1
def test_verify_checkboxes_text(setup):
    driver = setup
    driver.find_element_by_link_text("Checkboxes").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    assert "Checkboxes" in driver.find_element_by_tag_name("h3").text

#checkbox validations 2
def validate_checkbox_state(driver, checkbox_number, expected_state):
    checkbox = driver.find_element_by_css_selector(f"input[type='checkbox']:nth-of-type({checkbox_number})")
    assert checkbox.is_selected() == expected_state

def test_verify_checkbox_states(setup):
    driver = setup
    driver.get("http://the-internet.herokuapp.com/checkboxes")
    validate_checkbox_state(driver, 1, False)
    validate_checkbox_state(driver, 2, True)

#file upload validations
def test_file_upload(setup):
    driver = setup
    driver.get("http://the-internet.herokuapp.com/")
    driver.find_element_by_link_text("File Upload").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    assert "File Uploader" in driver.find_element_by_tag_name("h3").text

    # Uploading a file
    file_path = "C:\Users\pavankumarw\Downloads\TextDataMain.xlsx"
    choose_file_input = driver.find_element_by_id("file-upload")
    choose_file_input.send_keys(file_path)

    upload_button = driver.find_element_by_id("file-submit")
    upload_button.click()
