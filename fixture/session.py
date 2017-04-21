
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email, password):
        wd = self.app.wd
        wd.find_element_by_css_selector("[ng-model='login.userInfo.email']").send_keys(email)
        wd.find_element_by_css_selector("[ng-model='login.userInfo.password']").send_keys(password)
        wd.find_element_by_css_selector("[type='submit']").click()