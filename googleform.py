from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleForm:
    def __init__(self, driver):
        self.driver = driver

    def next(self):
        xpath_first = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span'
        xpath_second = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'

        try:
            next_button = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath_first))
            )

        except:
            next_button = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, xpath_second))
            )

        next_button.click()

    def assert_content(self, content):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//p[contains(., '{content}')]")
                )
            )
            return element is not None
        except NoSuchElementException:
            return False

    def auto_choice(self, first=False):
        questions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@role='radiogroup']"))
        )
        if first is True:
            questions[0].find_elements(
                By.XPATH, ".//div[@role='radio']")[0].click()

        else:
            for question in questions:
                options = question.find_elements(
                    By.XPATH, ".//div[@role='radio']")
                if options:
                    random_index = random.randint(0, len(options) - 1)
                    options[random_index].click()
                else:
                    print("No options found for a question.")

    def fill_input_by_xpath(self, xpath, text):
        try:
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            input_field.clear()
            input_field.send_keys(text)
        except Exception as e:
            print(f"An error occurred: {e}")
