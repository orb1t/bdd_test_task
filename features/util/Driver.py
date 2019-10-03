from appium import webdriver


class Driver:

    ELEMENT_DISPLAY_TIMER = 10

    def __init__(self):
        desired_caps = {
            'platformName'     : 'Android',
            # 'deviceName'       : 'emulator-5554',
            'deviceName'       : 'd301c6fa0603',
            'appPackage'       : 'com.instagram.android',
            'appActivity'      : 'com.instagram.android.activity.MainTabActivity',
            'appWaitActivity'  : 'com.instagram.nux.activity.SignedOutFragmentActivity'
        }

        self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
