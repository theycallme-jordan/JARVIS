from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MusicPlayer:
    def __init__(self, driver_path):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"executable_path={driver_path}")
        self.driver = webdriver.Chrome(options=chrome_options)

    def play(self, query):
        self.driver.get(f"https://www.youtube.com/results?search_query={query}")

        # Wait for the search results to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'video-title'))
        )

        # Find the first video element by class name and click it
        first_video = self.driver.find_element(By.ID, 'video-title')
        first_video.click()

if __name__ == "__main__":
    driver_path = r"C:\Users\gusai\Driver\chromedriver.exe"
    # music_player = MusicPlayer(driver_path)
    # music_player.play('dynamite')

