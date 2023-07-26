# engines.py

from car import Car

class CapuletEngine(Car):
    # ... (unchanged code)
    
    def engine_should_be_serviced(self):
        # Include oil change check along with mileage check
        return self.current_mileage - self.last_service_mileage > 30000 or self.needs_oil_change()


class SternmanEngine(Car):
    # ... (unchanged code)

    def engine_should_be_serviced(self):
        # Include oil change check based on warning light status
        return self.warning_light_is_on or self.needs_oil_change()


class WilloughbyEngine(Car):
    # ... (unchanged code)

    def engine_should_be_serviced(self):
        # Include oil change check along with mileage check
        return self.current_mileage - self.last_service_mileage > 60000 or self.needs_oil_change()
