from abc import ABCMeta
from abc import abstractmethod


class BaseActivity(metaclass=ABCMeta):
    driver = None

    def __init__(self, driver):
        self.driver = driver
        try:
            self._validate_page()
        except Exception:
            raise InvalidPageError(
                "'{}' Screen expected, but was '{}' Screen".format(self.__class__.__name__,
                                                                   self.driver.instance.current_activity))

    @abstractmethod
    def _validate_page(self):
        return


class InvalidPageError(Exception):
    pass
