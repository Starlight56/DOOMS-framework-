"""
DOOMS Core Framework - Decimal-Origin Observation Modeling System
Author: Eryn-Starr (Starlight56)
License: Unlicense
"""

import math

class DOOMSModel:
    def __init__(self, origin=(0.0, 0.0, 0.0)):
        """
        Initialize with a 3D decimal origin.
        """
        self.origin = origin
        self.points = []

    def set_origin(self, x, y, z):
        """
        Set a new origin point.
        """
        self.origin = (float(x), float(y), float(z))

    def add_point(self, x, y, z, label=None):
        """
        Add a point relative to the current origin.
        """
        point = {
            "label": label or f"Point_{len(self.points)+1}",
            "coordinates": (float(x), float(y), float(z))
        }
        self.points.append(point)

    def get_all_points(self):
        """
        Return all stored points with labels and coordinates.
        """
        return self.points

    def calculate_distance_from_origin(self, point):
        """
        Calculate Euclidean distance from the origin.
        """
        ox, oy, oz = self.origin
        px, py, pz = point["coordinates"]
        return math.sqrt((px - ox) ** 2 + (py - oy) ** 2 + (pz - oz) ** 2)

    def export_model(self):
        """
        Export current model data as a dictionary.
        """
        return {
            "origin": self.origin,
            "points": self.points
        }

# --- Sample Usage (can be removed for deployment) ---
if __name__ == "__main__":
    model = DOOMSModel()
    model.add_point(3.2, 5.1, 2.0, label="Sensor A")
    model.add_point(-1.0, 0.0, 4.5)
    
    for pt in model.get_all_points():
        print(f"{pt['label']} | Distance: {model.calculate_distance_from_origin(pt):.4f}")

    print("Exported model:", model.export_model())
