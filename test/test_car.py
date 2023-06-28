import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    def test_CapuletEngine_should_be_serviced(self):
        last_service_mileage = 30000
        current_mileage = 60001
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_CapuletEngine_should_not_be_serviced(self):
        last_service_mileage = 30000
        current_mileage = 60000
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_WilloughbyEngine_should_be_serviced(self):
        last_service_mileage = 30000
        current_mileage = 90001
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_WilloughbyEngine_should_not_be_serviced(self):
        last_service_mileage = 30000
        current_mileage = 90000
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_SternmanEngine_should_be_serviced(self):
        warning_light_is_on = True
        
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_SternmanEngine_should_not_be_serviced(self):
        warning_light_is_on = False
        
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

    def test_SpindlerBattery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_SpindlerBattery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_NubbinBattery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_NubbinBattery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())