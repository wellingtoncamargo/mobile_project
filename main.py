import os
import glob
import unittest
from time import sleep
from Elements import _element
from Objects import _object


class AndroidWebViewTests(unittest.TestCase):

    def test_001(self):
        _object.capturaPng('Login/Home')
        _object.click_element_locator(_element.myGarden)
        _object.validation_element_locator(_element.emptyGarden, 'Your garden is empty')
        _object.click_element_locator(_element.plantList)
        _object.await_element_locator(_element.filterZone)
        _object.capturaPng('Login/PlantList')

    def test_002(self):

        _object.click_element_locator(_element.filterZone)
        _object.capturaPng('Nova/Filtro')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    _object.tearDown()

# pytest main.py --html-report=./report/report.html