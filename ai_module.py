# ai_module.py

# ai_module.py

import random

def generate_planet_description(has_rings, size, color, moons, atmosphere ):
    """Generate a fun AI-like description of the planet."""
    descriptions = [
        f"A {color} planet of {size} size with {'majestic rings' if has_rings else 'no rings'}, "
        f"{moons} moon{'s' if moons != 1 else ''}, and a {atmosphere} atmosphere.",
        f"This {color} world is {size}-sized and {'encircled by shimmering rings' if has_rings else 'ringless'}, "
        f"with {moons} moon{'s' if moons != 1 else ''} orbiting it.",
        f"A {color} sphere floating in space, {size} in scale, surrounded by {moons} moon{'s' if moons != 1 else ''}. "
        f"Its {atmosphere} atmosphere wraps over the planet's lands."
    ]
    return random.choice(descriptions)
