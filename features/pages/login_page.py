from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Loginpage:
    signIn_id = "nav-link-accountList-nav-line-1"
    email_Css = "[id='ap_email']"
    Continue_mailbtn_Xpath = "//input[@class='a-button-input']"
    password_Css = "[type='password']"
    password_Submit_id = "signInSubmit"
    # searchbox_xpath = "//input[@type='text']"
    searchbox_xpath = "// input[ @ id = 'twotabsearchtextbox']"

    searchicon_id = "nav-search-submit-button"
    # productverify_css = "[class='a-color-state a-text-bold']"
    verify_xpath = "[class = 'a-color-state a-text-bold']"

    signout_Text = ["//span[text()='Sign Out']"]
    act = ["//a[@id='nav-link-accountList']"]

    def __init__(self, driver):
        self.driver = driver

    def login_my_account(self, ):
        self.driver.find_element(By.ID, self.signIn_id).click()
        self.driver.find_element(By.CSS_SELECTOR, self.email_Css).send_keys("+919047085104")
        self.driver.find_element(By.XPATH, self.Continue_mailbtn_Xpath).click()
        self.driver.find_element(By.CSS_SELECTOR, self.password_Css).send_keys("87654321")
        self.driver.find_element(By.ID, self.password_Submit_id).click()

    def search_product(self):
        self.driver.find_element(By.XPATH, self.searchbox_xpath).send_keys("Laptop")
        self.driver.find_element(By.ID, self.searchicon_id).click()

    def verify_product(self):
        status = self.driver.current_url
        print("url: ", status)

    # def moveto_action(self):
    #     ActionChains(self.driver).move_to_element(self,to_element=self.act).perform()
    #     action_test = ActionChains(self.driver)
    #     for action in self.act:
    #         action_test.move_to_element(to_element=action).click().perform()
