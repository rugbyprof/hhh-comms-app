"""
Chat GPT Generated Code
"""

from math import radians, sin, cos, sqrt, atan2
from geoModule import GeoManager
from geoModule import GeoProperties
from geoModule import nearest_neighbor_route
import os, sys
import glob
from rich import print


def read_points_from_csv(file_path: str, latlon_headers: tuple) -> list:
    """
    Description:
        Read lat/lon points from a CSV file.
        The CSV file should have two columns: latitude and longitude.
        If may or may not have a header row.
    Args:
        file_path (str): The path to the CSV file.
        ignore_header (bool): Whether to ignore the header row.
    Returns:
        list: A list of lat/lon points as tuples.
    """
    points = []
    with open(file_path, "r") as f:
        headers = f.readline().strip().split(",")
        lat_idx = headers.index(latlon_headers[0])
        lon_idx = headers.index(latlon_headers[1])
        next(f)
        for line in f:
            line = line.strip().split(",")
            points.append((float(line[lat_idx]), float(line[lon_idx])))

    return points


def read_directory(path: str, extension: str) -> list:
    """
    Description:
        Read directory for files with a specific extension.
    Args:
        path (str): The path to the directory.
        extension (str): The file extension to search for.
    Returns:
        list: A list of file paths.
    """
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    return files


def compare_points_lists(p1s: list, p2s: list) -> list:

    for i in range(len(p1s)):
        print(f"{p1s[i]} : {p2s[i]}")


def random_hex_color() -> str:
    """
    Description:
        Generate a random hex color.
    Returns:
        str: A random hex color.
    """
    import random

    return f"#{random.randint(0, 0xFFFFFF):06x}"


if __name__ == "__main__":

    colors = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFF00",
        "#00FFFF",
        "#FF00FF",
        "#C0C0C0",
        "#808080",
        "#800000",
        "#808000",
        "#008000",
        "#800080",
        "#008080",
        "#000080",
    ]

    files = read_directory("./data/csv", "csv")

    r = 0

    for f in files:
        geo = GeoManager()
        name = f.split("/")[-1].split(".")[0]
        if "Points" in name:
            name = name[7:]
        print(name)
        if "Rest" in name:
            properties = GeoProperties("point")
            properties.set_property("marker-color", colors[r % len(colors)])
            properties.set_property("description", name)
        else:
            properties = GeoProperties("line")
            properties.set_property("stroke", colors[r % len(colors)])
            properties.set_property("description", name)
        points = read_points_from_csv(f, ("POINT_X", "POINT_Y"))
        # ordered_points = nearest_neighbor_route(points)
        multiLinestring = []
        for i in range(len(points) - 1):
            multiLinestring.append([points[i], points[i + 1]])

        geo.add_multilinestring(multiLinestring, properties.get_properties())
        # if r == 3:
        #     break
        r += 1
        geoJson = geo.to_json()
        geoName = f.replace("csv", "geojson")
        with open(geoName, "w") as f:
            f.write(geoJson)
