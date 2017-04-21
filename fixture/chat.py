
class ChatHelper:

    def __init__(self, app):
        self.app = app

    def click_edit_mes(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[class="tickets__ticket-name"]').click()
        wd.find_element_by_css_selector('[class="tickets__ticket-name"]').click()