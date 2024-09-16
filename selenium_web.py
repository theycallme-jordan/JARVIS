from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class infow():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("executable_path=C:\\Users\\gusai\\Driver\\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

        # Wait for the search input element to be present using WebDriverWait
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]'))
        )

        # Perform actions on the search input element
        search.click()
        search.send_keys(query)

        # Find the submit button using XPath and click it
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

        # Add a loop to keep the script running until the browser window is closed
        while True:
            try:
                # Check if the browser window is still open
                self.driver.title
            except Exception as e:
                # If an exception is raised, assume the window is closed
                break


