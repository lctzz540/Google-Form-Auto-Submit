from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import random
import threading
from googleform import GoogleForm


def get_random_comment():
    with open("comments.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            return random.choice(lines)
        else:
            return "File is empty or does not exist."


def submit_form():
    for i in range(20):
        edgedriver_path = "~/Desktop/msedgedriver"
        edge_options = Options()

        driver_service = Service(edgedriver_path)
        driver = webdriver.Edge(service=driver_service, options=edge_options)

        driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSeJrXSPq6NRE7bocUBTjH8adS2pxDxgCevbhNXiowGnlPkKng/formResponse"
        )

        form = GoogleForm(driver)
        form.auto_choice(first=True)
        form.next()
        form.fill_input_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/div[1]/div/div[1]/input',
            get_random_comment(),
        )
        form.auto_choice()

        try:
            form.next()
            form.auto_choice()
            form.next()
        except:
            pass

        driver.quit()


def main():
    num_threads = 5

    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=submit_form)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
