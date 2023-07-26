class Car:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def get_last_service_date(self):
        return self.last_service_date

    def needs_oil_change(self):
        # Assuming an oil change is needed if more than 6 months since the last service
        # You can modify this logic based on your requirements.
        return self.calculate_months_since_last_service() > 6

    def calculate_months_since_last_service(self):
        # Implement this method to calculate the number of months since the last service date.
        # You can use any date calculation method that suits your codebase.
        pass
