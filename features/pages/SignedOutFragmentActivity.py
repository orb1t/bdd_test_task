from features.pages.BaseActivity import BaseActivity


class SignedOutFragmentActivity(BaseActivity):
    logInBtn = lambda self: self.driver.instance.find_element_by_id('com.instagram.android:id/log_in_button')

    def open_log_in_activity(self):
        self.logInBtn().click()

    def _validate_page(self):
        assert self.logInBtn().is_displayed() is True
