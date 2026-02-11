import unittest

from src.builder import (
    EstimateInput,
    calculate_estimate,
    calculate_material_quantity,
    format_estimate,
)


class BuilderTests(unittest.TestCase):
    def test_material_quantity_with_waste(self):
        self.assertAlmostEqual(calculate_material_quantity(1000, 0.1), 1100)

    def test_material_quantity_raises_for_invalid_area(self):
        with self.assertRaises(ValueError):
            calculate_material_quantity(0)

    def test_estimate_calculation(self):
        data = EstimateInput(
            area_sqft=1000,
            material_cost_per_sqft=5,
            labor_rate_per_hour=40,
            labor_hours=80,
            waste_factor=0.1,
        )
        result = calculate_estimate(data)

        self.assertAlmostEqual(result.material_quantity_sqft, 1100)
        self.assertAlmostEqual(result.material_cost, 5500)
        self.assertAlmostEqual(result.labor_cost, 3200)
        self.assertAlmostEqual(result.total_cost, 8700)

    def test_formatted_output_contains_values(self):
        data = EstimateInput(
            area_sqft=200,
            material_cost_per_sqft=2,
            labor_rate_per_hour=30,
            labor_hours=10,
        )
        output = format_estimate(calculate_estimate(data))
        self.assertIn("Construction Estimate", output)
        self.assertIn("Total cost", output)


if __name__ == "__main__":
    unittest.main()
