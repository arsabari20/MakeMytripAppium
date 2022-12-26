
import pytest

from Pages.Homescreen import Screen
from TestCases.BaseTest import BaseTest


#def get_data():
    #return ["Chennai", "Bangalore"]


class Test_Book(BaseTest):


    def test_bookbus(self, boarding="Chennai", destination="Bangalore"):
        home = Screen(self.driver)
        home.BookBus().Bus_booking(boarding, destination)


