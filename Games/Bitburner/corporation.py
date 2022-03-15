import dataclasses
from typing import ClassVar
from dataclasses import dataclass
from math import prod


@dataclass
class Inventory:
    sizes: ClassVar[dict[str, float]] = {
        "water": 0.05,
        "energy": 0.01,
        "food": 0.03,
        "plants": 0.05,
        "metal": 0.1,
        "hardware": 0.06,
        "chemicals": 0.05,
        "drugs": 0.02,
        "robots": 0.5,
        "ai_cores": 0.1,
        "real_estate": 0.005,
    }
    water: float = 0
    energy: float = 0
    food: float = 0
    plants: float = 0
    metal: float = 0
    hardware: float = 0
    chemicals: float = 0
    drugs: float = 0
    robots: float = 0
    ai_cores: float = 0
    real_estate: float = 0

    @property
    def size(self):
        return sum(self.sizes[material] * amount for  material, amount in dataclasses.asdict(self).items())



@dataclass(frozen=True)
class Industry:
    """A data class for industry properties"""

    science_factor: float
    hardware_factor: float
    robotics_factor: float
    ai_factor: float
    real_estate_factor: float
    advertising_factor: float
    creates_products: bool = False

    def city_multiplier(
            self,
            hardware_quantity: float,
            robots_quantity: float,
            ai_quantity: float,
            real_estate_quantity: float,
    ):
        # This is from the function `calculateProductionFactor()` at the following URL
        # https://github.com/danielyxie/bitburner/blob/dev/src/Corporation/Industry.ts

        quantity_multiplier = 0.002
        amount_addition = 1
        term_power = 0.73

        real_estate_power = pow(quantity_multiplier * real_estate_quantity + amount_addition, self.real_estate_factor)
        hardware_power = pow(quantity_multiplier * hardware_quantity + amount_addition, self.hardware_factor)
        robotics_power = pow(quantity_multiplier * robots_quantity + amount_addition, self.robotics_factor)
        ai_power = pow(quantity_multiplier * ai_quantity + amount_addition, self.ai_factor)
        power_total = prod((real_estate_power, hardware_power, robotics_power, ai_power))
        city_mult = pow(power_total, term_power)
        city_mult = max(1, city_mult)
        return city_mult


class Industries:
    Energy = Industry(
        science_factor=0.7,
        hardware_factor=0,
        robotics_factor=0.05,
        ai_factor=0.3,
        real_estate_factor=0.65,
        advertising_factor=0.08
    )
    Utilities = Industry(
        real_estate_factor=0.5,
        science_factor=0.6,
        hardware_factor=0,
        robotics_factor=0.4,
        ai_factor=0.4,
        advertising_factor=0.08
    )
    Agriculture = Industry(
        real_estate_factor=0.72,
        science_factor=0.5,
        hardware_factor=0.2,
        robotics_factor=0.3,
        ai_factor=0.3,
        advertising_factor=0.04
    )
    Fishing = Industry(
        real_estate_factor=0.15,
        science_factor=0.35,
        hardware_factor=0.35,
        robotics_factor=0.5,
        ai_factor=0.08,
        advertising_factor=0
    )
    # TODO: Fill in the rest of this data from the following URL:
    #  https://github.com/danielyxie/bitburner/blob/d955398a684d08c3103d23b46023f6549947ffa0/src/Corporation/Industry.ts
    # Mining = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    # Food = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    Tobacco = Industry(
        real_estate_factor=0.15,
        science_factor=0.75,
        hardware_factor=0.15,
        robotics_factor=0,
        ai_factor=0,
        advertising_factor=0
    )

    # Chemical = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    #
    # Pharmaceutical = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    # Computer = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    # Robotics = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    # Software = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    # Healthcare = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )
    # RealEstate = Industry(
    #     real_estate_factor=0,
    #     science_factor=0,
    #     hardware_factor=0,
    #     robotics_factor=0,
    #     ai_factor=0,
    #     advertising_factor=0
    # )


if __name__ == "__main__":
    # test_mult = Industries.Agriculture.city_multiplier(9300, 726, 6270, 230400)
    # print(6 * test_mult)
    test_inventory = Inventory(hardware=9300, robots=726, ai_cores=6270, real_estate=230400)
    print(f"{test_inventory=}, {test_inventory.size=}")
