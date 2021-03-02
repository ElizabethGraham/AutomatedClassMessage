from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    browser = webdriver.Firefox()
    browser.get('https://login.alamo.edu/authenticationendpoint/login.do?Name=PreLoginRequestProcessor&commonAuthCallerPath=%252Fcas%252Flogin&forceAuth=false&passiveAuth=false&service=https%3A%2F%2Falamo.instructure.com%2Flogin%2Fcas%2F222&tenantDomain=carbon.super&sessionDataKey=1e8fa698-3884-4ea5-90a9-b5ac3f4c0542&relyingParty=Canvas&type=cas&sp=Canvas&isSaaSApp=false&authenticators=BasicAuthenticator:LOCAL')
    assert 'Alamo' in browser.title

    elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys('Sign in' + Keys.RETURN)

    browser.quit()


if __name__ == '__main__':
    main()