"""Core utilities for simple construction project estimates."""

from dataclasses import dataclass


@dataclass
class EstimateInput:
    """Inputs used to generate a construction estimate."""

    area_sqft: float
    material_cost_per_sqft: float
    labor_rate_per_hour: float
    labor_hours: float
    waste_factor: float = 0.1


@dataclass
class EstimateResult:
    """Output values produced by a construction estimate."""

    material_quantity_sqft: float
    material_cost: float
    labor_cost: float
    total_cost: float


def calculate_material_quantity(area_sqft: float, waste_factor: float = 0.1) -> float:
    """Return the adjusted material quantity including waste."""
    if area_sqft <= 0:
        raise ValueError("area_sqft must be greater than zero")
    if waste_factor < 0:
        raise ValueError("waste_factor cannot be negative")

    return area_sqft * (1 + waste_factor)


def calculate_estimate(data: EstimateInput) -> EstimateResult:
    """Calculate material, labor, and total project costs."""
    if data.material_cost_per_sqft < 0:
        raise ValueError("material_cost_per_sqft cannot be negative")
    if data.labor_rate_per_hour < 0:
        raise ValueError("labor_rate_per_hour cannot be negative")
    if data.labor_hours < 0:
        raise ValueError("labor_hours cannot be negative")

    material_quantity = calculate_material_quantity(data.area_sqft, data.waste_factor)
    material_cost = material_quantity * data.material_cost_per_sqft
    labor_cost = data.labor_rate_per_hour * data.labor_hours
    total_cost = material_cost + labor_cost

    return EstimateResult(
        material_quantity_sqft=material_quantity,
        material_cost=material_cost,
        labor_cost=labor_cost,
        total_cost=total_cost,
    )


def format_estimate(result: EstimateResult) -> str:
    """Create a human-readable estimate summary."""
    return (
        "Construction Estimate\n"
        "---------------------\n"
        f"Material quantity: {result.material_quantity_sqft:.2f} sqft\n"
        f"Material cost: ${result.material_cost:,.2f}\n"
        f"Labor cost: ${result.labor_cost:,.2f}\n"
        f"Total cost: ${result.total_cost:,.2f}"
    )


if __name__ == "__main__":
    sample = EstimateInput(
        area_sqft=1200,
        material_cost_per_sqft=6.5,
        labor_rate_per_hour=55,
        labor_hours=90,
        waste_factor=0.12,
    )
    print(format_estimate(calculate_estimate(sample)))
