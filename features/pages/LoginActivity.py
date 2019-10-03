from features.pages.BaseActivity import BaseActivity


class LoginActivity(BaseActivity):
    usernameEdit = lambda self: self.driver.instance.find_element_by_id('com.instagram.android:id'
                                                                        '/login_username')
    passwordEdit = lambda self: self.driver.instance.find_element_by_id('com.instagram.android:id'
                                                                        '/password')
    nextBtn = lambda self: self.driver.instance.find_element_by_id('com.instagram.android:id'
                                                                   '/next_button')

    def set_user_name(self, name):
        self.usernameEdit().send_keys(name)

    def set_password(self, password):
        self.passwordEdit().send_keys(password)

    def submit_login(self):
        self.nextBtn().click()

    def log_in_as(self, name, password):
        self.set_user_name(name)
        self.set_password(password)
        self.submit_login()

    def _validate_page(self):
        assert self.usernameEdit().is_displayed() is True
