from playwright.sync_api import Page

class FlightPage:
    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto("https://blazedemo.com/")

    def search_flights(self, from_city, to_city):
        self.page.select_option("select[name='fromPort']", from_city)
        self.page.select_option("select[name='toPort']", to_city)
        self.page.click("input[type='submit']")

    def get_results(self):
        self.page.wait_for_selector("table tbody tr")

        rows = self.page.locator("table tbody tr")
        flights = []

        for i in range(min(rows.count(), 5)):
            row = rows.nth(i)

            airline = row.locator("td").nth(2).inner_text()
            price = row.locator("td").nth(5).inner_text()

            flights.append({
                "flight_number": i + 1,
                "airline": airline,
                "price": price
            })

        return flights