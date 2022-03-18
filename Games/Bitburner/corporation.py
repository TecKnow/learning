import dataclasses
from dataclasses import dataclass
from typing import ClassVar, Optional
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
    material_count_per_unit_volume: ClassVar[dict[str, int]] = {material: int(1 / size) for material, size in
                                                                sizes.items()}
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
        return sum(self.sizes[material] * amount for material, amount in dataclasses.asdict(self).items())


@dataclass(frozen=True)
class Industry:
    """A data class for industry properties"""

    science_factor: float
    hardware_factor: float
    robotics_factor: float
    ai_factor: float
    real_estate_factor: float
    advertising_factor: float
    makes_products: bool = False

    def city_multiplier(
            self,
            inventory: Inventory
    ) -> float:
        # This is from the function `calculateProductionFactor()` at the following URL
        # https://github.com/danielyxie/bitburner/blob/dev/src/Corporation/Industry.ts

        quantity_multiplier = 0.002
        amount_addition = 1
        term_power = 0.73

        real_estate_power = pow(quantity_multiplier * inventory.real_estate + amount_addition, self.real_estate_factor)
        hardware_power = pow(quantity_multiplier * inventory.hardware + amount_addition, self.hardware_factor)
        robotics_power = pow(quantity_multiplier * inventory.robots + amount_addition, self.robotics_factor)
        ai_power = pow(quantity_multiplier * inventory.ai_cores + amount_addition, self.ai_factor)
        power_total = prod((real_estate_power, hardware_power, robotics_power, ai_power))
        city_mult = pow(power_total, term_power)
        city_mult = max(1, city_mult)
        return city_mult

    def improve(self, inventory: Optional[Inventory] = None) -> Inventory:
        while True:
            inventory = inventory if inventory is not None else Inventory()
            production_factor_items = set("hardware robots ai_cores real_estate".split())
            candidate_inventories = (
                dataclasses.replace(
                    inventory,
                    **{production_factor_item: getattr(inventory, production_factor_item) +
                                               Inventory.material_count_per_unit_volume[production_factor_item]})
                for
                production_factor_item in
                production_factor_items)
            candidate_inventories = ((self.city_multiplier(candidate),
                                      candidate.size,
                                      candidate) for candidate in candidate_inventories)
            sorted_candidates = sorted(candidate_inventories, key=lambda x: x[0:2], reverse=True)
            inventory = sorted_candidates[0][2]
            yield inventory

    def improve_until(self, space: int, inventory: Optional[Inventory] = None) -> Inventory:
        inventory = inventory if inventory is not None else Inventory()
        for next_inventory in self.improve(inventory):
            if next_inventory.size > space:
                return inventory
            inventory = next_inventory


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
        robotics_factor=0.2,
        ai_factor=0.15,
        advertising_factor=0.2,
        makes_products=True
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
    target_inventory = Industries.Energy.improve_until(10000)
    print(target_inventory)
    print(Industries.Energy.city_multiplier(target_inventory))
