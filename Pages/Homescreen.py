from Pages.BasePage import BasePage
from Pages.BookBusScreen import BookBusScreen


class Screen(BasePage):
        def __init__(self,driver):
            super().__init__(driver)

        def BookBus(self):
            self.Click("BookTravel_XPATH")
            self.Click("BookBus_XPATH")
            return BookBusScreen(self.driver)

        def BookHotel(self):
            pass

        def Bookflights(self):
            pass

