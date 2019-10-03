from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


from features.pages.BaseActivity import BaseActivity


class IncorrectCredentialsDialog(BaseActivity):
    incorrectCredentialsDialogTitleLocator = (By.ID, "com.instagram.android:id/default_dialog_title")
    incorrectCredentialsDialogTitle = lambda self: self.driver.instance.find_element(
        *self.incorrectCredentialsDialogTitleLocator)

    def _validate_page(self):
        WebDriverWait(self.driver.instance, self.driver.ELEMENT_DISPLAY_TIMER).until(
            ec.visibility_of_element_located(self.incorrectCredentialsDialogTitleLocator))
