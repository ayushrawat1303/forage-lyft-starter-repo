import unittest

# Assuming the Car class has a method called `get_last_service_date` that returns the last service date.


# Unit Test for CapuletEngine
class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        # Test case when service is needed
        engine = CapuletEngine("2023-01-01", 75000, 50000)
        self.assertTrue(engine.engine_should_be_serviced())

        # Test case when service is not needed
        engine = CapuletEngine("2023-01-01", 55000, 50000)
        self.assertFalse(engine.engine_should_be_serviced())


# Unit Test for SternmanEngine
class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        # Test case when service is needed (warning_light_is_on = True)
        engine = SternmanEngine("2023-01-01", True)
        self.assertTrue(engine.engine_should_be_serviced())

        # Test case when service is not needed (warning_light_is_on = False)
        engine = SternmanEngine("2023-01-01", False)
        self.assertFalse(engine.engine_should_be_serviced())


# Unit Test for WilloughbyEngine
class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        # Test case when service is needed
        engine = WilloughbyEngine("2023-01-01", 100000, 40000)
        self.assertTrue(engine.engine_should_be_serviced())

        # Test case when service is not needed
        engine = WilloughbyEngine("2023-01-01", 50000, 40000)
        self.assertFalse(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
