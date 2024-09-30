import json
from math import radians, sin, cos, sqrt, atan2


class GeoManager:
    """
    This class can be used to create a GeoJSON feature collection. It class allows you to add
    point, linestring, multilinestring, and polygon features to the collection. You can then
    retrieve the feature collection as a JSON string or as a dictionary.

    Example usage:
        geo_manager = GeoManager()
        geo_manager.add_point([102.0, 0.5], {"name": "Point A"})
        geo_manager.add_linestring(
            [[102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]], {"name": "Line A"}
        )
        print(geo_manager.to_json())
    """

    def __init__(self):
        # Initialize a feature collection with an empty list of features
        self.feature_collection = {"type": "FeatureCollection", "features": []}

    def add_point(self, coordinates, properties=None):
        """Add a point feature to the collection."""
        point_feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": coordinates},
            "properties": properties or {},
        }
        self.feature_collection["features"].append(point_feature)

    def add_linestring(self, coordinates, properties=None):
        """Add a linestring feature to the collection."""
        linestring_feature = {
            "type": "Feature",
            "geometry": {"type": "LineString", "coordinates": coordinates},
            "properties": properties or {},
        }
        self.feature_collection["features"].append(linestring_feature)

    def add_multilinestring(self, coordinates, properties=None):
        """Add a multilinestring feature to the collection."""
        multilinestring_feature = {
            "type": "Feature",
            "geometry": {"type": "MultiLineString", "coordinates": coordinates},
            "properties": properties or {},
        }
        self.feature_collection["features"].append(multilinestring_feature)

    def add_polygon(self, coordinates, properties=None):
        """Add a polygon feature to the collection."""
        polygon_feature = {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": coordinates},
            "properties": properties or {},
        }
        self.feature_collection["features"].append(polygon_feature)

    def to_json(self):
        """Return the feature collection as a JSON string."""
        return json.dumps(self.feature_collection, indent=2)

    def get_feature_collection(self):
        """Return the feature collection dictionary."""
        return self.feature_collection


class GeoProperties:
    """
    OPTIONAL: default ""
    A title to show when this item is clicked or hovered over
    "title": "A title",

    OPTIONAL: default ""
    A description to show when this item is clicked or hovered over
    "description": "A description",

    OPTIONAL: default "medium"
    Specify the size of the marker. Sizes can be different pixel sizes in different implementations.
    Value must be one of:
        "small"
        "medium"
        "large"
    "marker-size": "medium",

    OPTIONAL: default ""
    A symbol to position in the center of this icon if not provided or "".
    No symbol is overlaid and only the marker is shown.
    Allowed values include:
        - Icon ID
        - An integer 0 through 9
        - A lowercase character "a" through "z"
    "marker-symbol": "bus",

    OPTIONAL: default "7e7e7e"
    The marker's color value must follow COLOR RULES.
    "marker-color": "#fff",

    OPTIONAL: default "555555"
    The color of a line as part of a polygon, polyline, or multigeometry.
    Value must follow COLOR RULES
    "stroke": "#555555",

    OPTIONAL: default 1.0
    The opacity of the line component of a polygon, polyline, or multigeometry.
    Value must be a floating point number greater than or equal to zero and less or equal to than one
    "stroke-opacity": 1.0,

    OPTIONAL: default 2
    the width of the line component of a polygon, polyline, or multigeometry.
    Value must be a floating point number greater than or equal to 0.
    "stroke-width": 2,

    OPTIONAL: default "555555"
    The color of the interior of a polygon.
    Value must follow COLOR RULES
    "fill": "#555555",

    OPTIONAL: default 0.6
    the opacity of the interior of a polygon. Implementations may choose to set this to 0 for line features.
    Value must be a floating point number greater than or equal to zero and less or equal to than one.
    "fill-opacity": 0.5
    """

    def __init__(self, property_type="line"):
        if property_type == "line":
            self.properties = {}
            self.properties = {
                "title": "",
                "description": "",
                "stroke": "#555555",
                "stroke-opacity": 1.0,
                "stroke-width": 2,
            }
        elif property_type == "point":
            self.properties = {}
            self.properties = {
                "title": "",
                "description": "",
                "marker-size": "medium",
                "marker-symbol": "",
                "marker-color": "#fff",
            }
        elif property_type == "polygon":
            self.properties = {}
            self.properties = {
                "title": "",
                "description": "",
                "stroke": "#555555",
                "stroke-opacity": 1.0,
                "stroke-width": 2,
                "fill": "#555555",
                "fill-opacity": 0.5,
            }

    def get_properties(self):
        return self.properties

    def set_property(self, key, value):
        self.properties[key] = value


# Function to calculate Haversine distance between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    """
    Description:
        Calculate the Haversine distance between two lat/lon points.
    Args:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.
    Returns:
        float: The Haversine distance between the two points in miles.
    """
    R = 3956.0  # Earth radius in miles (use 6371.0 for km)
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# Function to find the next nearest point
def nearest_neighbor_route(points: str) -> list:
    """
    Description:
        Reorder a list of lat/lon points using the nearest neighbor algorithm.
    Args:
        points (list): A list of lat/lon points as tuples.
    Returns:
        list: A list of lat/lon points in the order of the nearest neighbor route
    """
    visited = [points[0]]  # Start with the first point
    points = points[1:]  # Remaining points

    while points:
        last_point = visited[-1]
        nearest_point = min(
            points, key=lambda p: haversine(last_point[0], last_point[1], p[0], p[1])
        )
        visited.append(nearest_point)
        points.remove(nearest_point)

    return visited


if __name__ == "__main__":
    # Example usage
    geo_manager = GeoManager()

    # Add a point feature
    geo_manager.add_point([102.0, 0.5], {"name": "Point A"})

    # Add a linestring feature
    geo_manager.add_linestring(
        [[102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]], {"name": "Line A"}
    )

    # Add a multilinestring feature
    geo_manager.add_multilinestring(
        [[[100.0, 0.0], [101.0, 1.0]], [[102.0, 2.0], [103.0, 3.0]]],
        {"name": "MultiLine A"},
    )

    # Add a polygon feature
    geo_manager.add_polygon(
        [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]]],
        {"name": "Polygon A"},
    )

    # Output the entire feature collection as a JSON string
    print(geo_manager.to_json())
