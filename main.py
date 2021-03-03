from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class Main():
    def __init__(self):
        # Load the Chrome webdriver into the browser variable for python to access it
        self.browser = webdriver.Chrome()
        # Store the website URL in a variable to make things legible
        self.url = "https://alamo.instructure.com/calendar#view_name=month&view_start=2020-10-14"
        # Store the message in case I need to update it or something, easy to find
        self.message = "Checking in. I am still alive and I am still enrolled and I am actively working on the course. Working on the HW now. \nElizabeth Graham, Physics, still don't really know what the section number is."

    def main(self):
        self.open_browser()
        self.site_login()
        self.goto_inbox()
        # self.browser.quit()


    def open_browser(self):
        """
            This entire first block of code is randomizing the browser's user agent info
            Apparently Canvas really doesn't like Selenium / Automation tools, so I needed
            to obscure the user agent info to prevent them from detecting it.
            
            The last two lines are actually opening the browser.
        """

        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

        # Get list of user agents.
        user_agents = user_agent_rotator.get_user_agents()

        # Get Random User Agent String.
        user_agent = user_agent_rotator.get_random_user_agent()

        # Open the browser to the designated URL
        self.browser.get(self.url)
        # Make sure Alamo is in the tab title
        assert 'Alamo' in self.browser.title


    def get_credentials(self):
        """ Access the data stored in the config file and upass them to site_login()

        Returns:
            List: [username,password]
        """
        file_object = open("credentials.config", "r")  # Open credentials config (readonly)
        file_content = file_object.readline()  # Read and store the credential line in the file in this variable
        
        credentials = file_content.split(",")  # Split the line at the delimeter ','
        file_object.close()  # Close the credentials file
        return credentials  # Return the credentials list
        
        
    def site_login(self):
        """ Login using the credentials provided from get_credentials() and click submit
        """
        credentials = self.get_credentials()  # username = [0], password=[1]

        self.browser.find_element_by_id("username").send_keys(credentials[0])  # Enter the username into the username box
        self.browser.find_element_by_id ("password").send_keys(credentials[1])  # Enter the password into the password box
        self.browser.find_element_by_xpath("/html/body/div/div/div/div/form/div[3]/div/button").click()  # Click the submit button

    
    def goto_inbox(self):
        # Click on inbox
        self.browser.find_element_by_xpath("/html/body/div[2]/header[2]/div[1]/ul/li[6]/a").click()

        # Click on filter by drop down
        self.browser.find_element_by_xpath("//*[@id=\"conversation_filter_select\"]/option[4]").click()
        # Click on sent
        self.browser.find_element_by_xpath("//*[@id=\"conversation-checkbox-18722043\"]/div/label").click()
        # Click on recent message
        self.browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/ul/li[1]/a").click() 

        # Fill in the main message area with the automated message
        self.browser.find_element_by_xpath("/html/body/div[4]/div[3]/form/div[2]/textarea").send_keys(self.message)

        # self.browser.find_element_by_xpath("/html/body/div[4]/div[4]/div[2]/button[2]/span").click()  # Submit, blocked out for tests




if __name__ == '__main__':
    m = Main()
    m.main()
