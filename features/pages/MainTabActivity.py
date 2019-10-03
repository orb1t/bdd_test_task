from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from features.pages.BaseActivity import BaseActivity


class MainTabActivity(BaseActivity):
    inboxBtnLocator = (By.ID, "com.instagram.android:id/action_bar_inbox_button")
    inboxBtn = lambda self: self.driver.instance.find_element(*self.inboxBtnLocator)

    def _validate_page(self):
        WebDriverWait(self.driver.instance, self.driver.ELEMENT_DISPLAY_TIMER).until(
            ec.visibility_of_element_located(self.inboxBtnLocator))
