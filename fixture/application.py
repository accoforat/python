from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesssion import SessionHalper
class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHalper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")



    def group_creation(self, group):
        wd = self.wd
        self.open_grous_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill grop form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_grous_page()

    def open_grous_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()



    def destroy (self):
        self.wd.quit()
