"""
I made this module that processes GPS points from a CSV file and 
converts them to a GeoJSON polyline. The module contains three functions:

- read_points_from_csv, which reads GPS points from a CSV file and returns them as a list of dictionaries.
- points_to_geojson_polyline, which converts a list of GPS points to a GeoJSON polyline.

As far as I can remember the functions did not create geojson in a way that would display
correctly and needs work.

TODO:
    - Fix the points_to_geojson_polyline function so that it creates a valid GeoJSON polyline.
    - Add type hints to the functions.
"""

import csv
import json
import sys
import glob


def read_points_from_csv(file_path: str) -> list:
    """
    Reads GPS points from a CSV file and returns them as a list of dictionaries.

    This function opens a CSV file at the specified file path, reads the rows using
    a CSV DictReader, and extracts the OBJECTID, POINT_X, and POINT_Y values for each
    row. The extracted values are converted to their appropriate data types (int for
    OBJECTID and float for POINT_X and POINT_Y) and stored in a list of dictionaries.

    Parameters:
    file_path (str): The path to the CSV file containing the GPS points.

    Returns:
    list of dict: A list of dictionaries, where each dictionary represents a GPS point
                  with the following keys:
                  - "OBJECTID" (int): The object ID of the point.
                  - "POINT_X" (float): The longitude of the point.
                  - "POINT_Y" (float): The latitude of the point.

    Example:
    >>> file_path = 'points.csv'
    >>> points = read_points_from_csv(file_path)
    >>> print(points)
    [{'OBJECTID': 1, 'POINT_X': -98.497583, 'POINT_Y': 33.918167},
     {'OBJECTID': 2, 'POINT_X': -98.666817, 'POINT_Y': 33.950933},
     {'OBJECTID': 3, 'POINT_X': -98.8181, 'POINT_Y': 33.9118}]
    """

    points = []
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            points.append(
                {
                    "OBJECTID": int(row["OBJECTID"]),
                    "POINT_X": float(row["POINT_X"]),
                    "POINT_Y": float(row["POINT_Y"]),
                }
            )
    return points


def points_to_geojson_polyline(points: list) -> dict:
    """
    Converts a list of GPS points to a GeoJSON polyline. Remebmer that a GeoJSON likes
    gps points to be in the format of (longitude, latitude) (x, y).
    """
    coordinates = [(point["POINT_X"], point["POINT_Y"]) for point in points]
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {"type": "LineString", "coordinates": coordinates},
            }
        ],
    }
    return geojson


if __name__ == "__main__":

    files = glob.glob("./data/csv/*.csv")
    for file in files:
        points = read_points_from_csv(file)
        geojson_polyline = points_to_geojson_polyline(points)

        outname = file.replace("csv", "geojson")

        # Save the GeoJSON to a file
        with open(f"{outname}", "w") as geojson_file:
            json.dump(geojson_polyline, geojson_file, indent=2)

    # below here is for 1 file at a time
    sys.exit(1)
    if len(sys.argv) != 2:
        raise ValueError("Please provide a single input CSV file.")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        raise ValueError("Input file must be a CSV file.")

    points = read_points_from_csv(file_path)
    geojson_polyline = points_to_geojson_polyline(points)
    print(file_path)
    outname = file_path.strip().split(".")[-2]

    outname = outname.replace("csv", "geojson")

    # Save the GeoJSON to a file
    with open(f"./{outname}.geojson", "w") as geojson_file:
        json.dump(geojson_polyline, geojson_file, indent=2)

    # Print the GeoJSON
    # print(json.dumps(geojson_polyline, indent=2))
