from Pages.BasePage import BasePage


class BookBusScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def Bus_booking(self,boarding,destination):
        self.Click("BoardingPT_XPATH")
        self.Click("City_XPATH")
        self.Type("City_XPATH",boarding)
        self.Click("Koyambedu_XPATH")
        self.Click("DropingPT_XPATH")
        self.Click("City_XPATH")
        self.Type("City_XPATH",destination)
        self.Click("ElectronicCity_XPATH")




