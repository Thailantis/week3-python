import unittest

class Test_Rental_Property(unittest.TestCase):
    def test_calculate_cash_on_cash_roi(self):
        rp = RentalProperty(2000, 1000, 500, 200, 500, 200, 100, 50, 50, 50, 50, 50, 50, 50, 100, 200, 500, 100, 1000, 50000, 10000, 20000, 500)
        expected_roi = 9.36
        actual_roi = rp.calculate_cash_on_cash_roi()
        self.assertAlmostEqual(expected_roi, actual_roi, delta=0.01)

    def test_calculate_total_monthly_income(self):
        rp = RentalProperty(2000, 1000, 500, 200, 150, 100, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 200, 860, 40000, 3000, 7000, 0)
        expected_income = 2000
        actual_income = rp.calculate_total_monthly_income()
        self.assertEqual(expected_income, actual_income)


if __name__ == '__main__':
    unittest.main()
