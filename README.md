# hhh.comms.app

Hotter N Hell React Js app to facilitate communication for the hundreds of volunteers during race day.

1. Determine back end data base to use.
2. Determine JS framework to use for mobile dev.
3. Write an API to connect the two.

Wow I just described every project ... ever.

## Mapping

- Terry added the gps points in csv format and geojson format in the [mapping](./mapping/) folder.
- I left a python file called [process.py](./mapping/process.py) that I used to read csv and convert to geojson. We may or may not use geojson, but I converted everything anyway. Most are messed up, but the 100 mile looks good. See here [100 mile](./mapping/data/geojson/Points_100_Mile.geojson)
