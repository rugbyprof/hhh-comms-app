# Mapping

I learned a bit researching these. Most I knew, but some others I did not (ubers and kepler for sure). One or more of these visulization libraries will help us display the routes in the app. Leaflet is a promising library for the visualization, but its been a while. The problem is "you get what you pay for", so open source and free mapping layers tend to look free (IMHO). For anyone interested, research the popularity and usecases for these. It'll help us make a good decision. OR, one of you gets so awesome at 1 of these, we just let you take over mapping :)

## Spatial Data Visualization

### 1. Google Maps (JavaScript API)

Google Maps is a powerful tool for visualizing geographic data, including coordinates and GeoJSON.

- **How to visualize lat/lon coordinates**:
  You can plot coordinates on a Google Map using the **Google Maps JavaScript API**.

  **Example:**

  ```html
  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
  <script>
    function initMap() {
      var location = { lat: 37.7749, lng: -122.4194 }; // Example Lat/Lon
      var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: location,
      });
      var marker = new google.maps.Marker({
        position: location,
        map: map,
      });
    }
  </script>
  <div id="map" style="height:500px;width:100%;"></div>
  <body onload="initMap()"></body>
  ```

- **How to visualize GeoJSON**:
  Google Maps can directly handle GeoJSON data using the `Data` layer. You can load GeoJSON data and display it on the map.

  **Example**:

  ```javascript
  map.data.loadGeoJson("path_to_your_geojson_file.json");
  ```

**Documentation**: [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview)

### 2. Leaflet.js

**Leaflet.js** is a popular open-source JavaScript library for interactive maps. It is lightweight, customizable, and integrates well with a variety of map tile providers.

- **How to visualize lat/lon coordinates**:
  You can easily plot markers on a Leaflet map by creating a `L.map()` and adding markers.

  **Example**:

  ```html
  <div id="map" style="height: 500px;"></div>
  <script>
    var map = L.map("map").setView([37.7749, -122.4194], 13); // Lat/Lon

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 18,
    }).addTo(map);

    L.marker([37.7749, -122.4194])
      .addTo(map)
      .bindPopup("San Francisco")
      .openPopup();
  </script>
  ```

- **How to visualize GeoJSON**:
  Leaflet can easily handle GeoJSON data and offers built-in functionality for rendering it on a map.

  **Example**:

  ```javascript
  var geojsonFeature = {
    type: "Feature",
    geometry: {
      type: "Point",
      coordinates: [-122.4194, 37.7749],
    },
    properties: {
      name: "San Francisco",
    },
  };

  L.geoJSON(geojsonFeature).addTo(map);
  ```

**Documentation**: [Leaflet.js Documentation](https://leafletjs.com/)

### 3. Mapbox

**Mapbox** provides high-quality, customizable maps, and supports advanced data visualizations with both lat/lon coordinates and GeoJSON data. It comes with a JavaScript library, **Mapbox GL JS**, for easy integration.

- **How to visualize lat/lon coordinates**:
  You can add points on the map using lat/lon coordinates.

  **Example**:

  ```html
  <div id="map" style="height: 500px;"></div>
  <script>
    mapboxgl.accessToken = "YOUR_MAPBOX_ACCESS_TOKEN";
    var map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/streets-v11",
      center: [-122.4194, 37.7749], // Starting position [lng, lat]
      zoom: 13,
    });

    var marker = new mapboxgl.Marker()
      .setLngLat([-122.4194, 37.7749])
      .addTo(map);
  </script>
  ```

- **How to visualize GeoJSON**:
  You can load GeoJSON data and visualize it on a Mapbox map.

  **Example**:

  ```javascript
  map.on("load", function () {
    map.addSource("places", {
      type: "geojson",
      data: "path_to_your_geojson_file.json",
    });

    map.addLayer({
      id: "places",
      type: "circle",
      source: "places",
      paint: {
        "circle-radius": 6,
        "circle-color": "#B42222",
      },
    });
  });
  ```

**Documentation**: [Mapbox GL JS Documentation](https://docs.mapbox.com/mapbox-gl-js/api/)

### 4. Kepler.gl (Open Source from Uber)

**Kepler.gl** is a web-based tool from Uber that is perfect for visualizing large-scale geospatial datasets. It supports CSVs, GeoJSON, and more complex data types. It requires no coding, making it easy to quickly upload and visualize your data.

- **How to visualize lat/lon coordinates**:
  You can upload a CSV or GeoJSON file containing your latitude and longitude coordinates, and Kepler.gl will automatically create an interactive map.

- **How to visualize GeoJSON**:
  You can directly upload GeoJSON files to Kepler.gl and visualize them as points, polygons, or lines.

**Website**: [Kepler.gl](https://kepler.gl/)

### 5. QGIS (Desktop Application)

**QGIS** is an open-source desktop application for geographic information system (GIS) analysis. It supports both latitude/longitude coordinates and GeoJSON and is great for detailed geospatial analysis and visualizations.

- **How to visualize lat/lon coordinates**:
  You can manually import a CSV file containing lat/lon data into QGIS and visualize it on a map.
- **How to visualize GeoJSON**:
  GeoJSON files can be directly opened and visualized in QGIS.

**Website**: [QGIS](https://www.qgis.org/en/site/)

### 6. OpenLayers

**OpenLayers** is an open-source JavaScript library that provides the ability to visualize geospatial data in a browser.

- **How to visualize lat/lon coordinates**:
  OpenLayers allows you to create a map and add layers of lat/lon coordinates.

  **Example**:

  ```javascript
  var map = new ol.Map({
    target: "map",
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM(),
      }),
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-122.4194, 37.7749]),
      zoom: 13,
    }),
  });

  var marker = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([-122.4194, 37.7749])),
  });
  ```

- **How to visualize GeoJSON**:
  You can load GeoJSON data directly into OpenLayers and display it as features.

**Documentation**: [OpenLayers Documentation](https://openlayers.org/)

### 7. Deck.gl (by Uber)

**Deck.gl** is another powerful, open-source WebGL-powered library for large-scale data visualization, with built-in support for geospatial data like lat/lon coordinates and GeoJSON.

- **How to visualize lat/lon coordinates**:
  You can use the **ScatterplotLayer** in Deck.gl to visualize coordinates.

- **How to visualize GeoJSON**:
  Use the **GeoJsonLayer** to visualize complex geographical data.

**Documentation**: [Deck.gl Documentation](https://deck.gl/)

---

### Summary of Tools:

- **Google Maps API**: Widely used and integrates well with other Google services.
- **Leaflet.js**: Lightweight and simple for basic maps with customization.
- **Mapbox**: High-quality, customizable maps with advanced features.
- **Kepler.gl**: Great for non-coders and large datasets.
- **QGIS**: Powerful desktop GIS tool for professional-level analysis.
- **OpenLayers**: A robust, open-source mapping library for the web.
- **Deck.gl**: Ideal for large-scale, WebGL-based data visualizations.

Each of these tools has its strengths depending on your needs.

- If you’re looking for browser-based visualization, **Leaflet.js**, **Mapbox**, or **Google Maps** would be ideal.
- For more detailed or professional GIS work, **QGIS** or **Kepler.gl** are great options. Let me know if you need more information on any of these!

## Spatial Data Routing Services

There is some overlap with the above libraries, which is actually good. I'm not sure if we will need routing to "fix" some of our data, but we might. Using the same library for both would be quicker.

Also, not all of these are free. Some are free up to a certain number of requests. So, if you decide to put your credit card in, be careful! Always check, or shutdown your account when done.

### 1. Google Maps Directions API

Google Maps provides a **Directions API** that returns step-by-step route directions between two geographic coordinates.

- **Features**: Supports driving, walking, biking, and public transit directions. Offers details such as distance, travel time, and alternative routes.
- **Pricing**: Free tier available (up to a certain number of requests), with paid plans for higher usage.
- **API Endpoint**: `https://maps.googleapis.com/maps/api/directions/json`
- **Documentation**: [Google Directions API](https://developers.google.com/maps/documentation/directions/start)

**Example**: Request for a route between two coordinates:

```
https://maps.googleapis.com/maps/api/directions/json?origin=37.7749,-122.4194&destination=34.0522,-118.2437&key=YOUR_API_KEY
```

### 2. OpenStreetMap (OSRM or GraphHopper)

OpenStreetMap (OSM) provides several routing engines that work with its map data, such as **OSRM (Open Source Routing Machine)** and **GraphHopper**.

#### a. OSRM (Open Source Routing Machine)

- **Features**: Provides fast routing between coordinates using OpenStreetMap data. Supports car, bike, and pedestrian routing.
- **Pricing**: Free and open-source, can also be self-hosted.
- **API Endpoint**: `https://router.project-osrm.org/route/v1/driving/{start_lng},{start_lat};{end_lng},{end_lat}`
- **Documentation**: [OSRM Documentation](http://project-osrm.org/docs/v5.5.1/api/)

**Example**:

```
https://router.project-osrm.org/route/v1/driving/-122.4194,37.7749;-118.2437,34.0522?overview=false
```

#### b. GraphHopper

- **Features**: Uses OpenStreetMap data and provides car, biking, and walking routes. You can host it yourself or use their API.
- **Pricing**: Free tier available for low usage; paid plans for higher usage.
- **API Endpoint**: `https://graphhopper.com/api/1/route`
- **Documentation**: [GraphHopper API](https://www.graphhopper.com/route-api/)

**Example**:

```
https://graphhopper.com/api/1/route?point=37.7749,-122.4194&point=34.0522,-118.2437&vehicle=car&key=YOUR_API_KEY
```

### 3. Mapbox Directions API

Mapbox offers a powerful **Directions API** that can return routes between geographic coordinates.

- **Features**: Supports driving, walking, cycling, and public transit. Provides estimated duration, distance, and step-by-step navigation.
- **Pricing**: Free tier available with limited usage; paid plans for higher usage.
- **API Endpoint**: `https://api.mapbox.com/directions/v5/mapbox/driving/{start_lng},{start_lat};{end_lng},{end_lat}`
- **Documentation**: [Mapbox Directions API](https://docs.mapbox.com/api/navigation/directions/)

**Example**:

```
https://api.mapbox.com/directions/v5/mapbox/driving/-122.4194,37.7749;-118.2437,34.0522?access_token=YOUR_API_KEY
```

### 4. HERE Routing API

HERE provides a robust **Routing API** that supports multiple modes of transportation and routes between geographic coordinates.

- **Features**: Offers routing for driving, public transit, walking, and more. Provides detailed traffic data and route optimization.
- **Pricing**: Free tier available with limited usage; paid plans for higher usage.
- **API Endpoint**: `https://router.hereapi.com/v8/routes`
- **Documentation**: [HERE Routing API](https://developer.here.com/documentation/routing-api/)

**Example**:

```
https://router.hereapi.com/v8/routes?transportMode=car&origin=37.7749,-122.4194&destination=34.0522,-118.2437&apiKey=YOUR_API_KEY
```

### 5. Bing Maps Directions API

Bing Maps also offers a **Directions API** to provide route information between two coordinates.

- **Features**: Supports driving, walking, and transit directions with step-by-step instructions.
- **Pricing**: Free tier available with limited usage; paid plans for higher usage.
- **API Endpoint**: `http://dev.virtualearth.net/REST/v1/Routes`
- **Documentation**: [Bing Maps Directions API](https://docs.microsoft.com/en-us/bingmaps/rest-services/routes/calculate-a-route)

**Example**:

```
http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=37.7749,-122.4194&wp.1=34.0522,-118.2437&key=YOUR_API_KEY
```

### 6. TomTom Routing API

TomTom provides a **Routing API** that includes advanced routing algorithms and traffic-aware routes.

- **Features**: Offers car, pedestrian, bike, and public transit routing, with real-time traffic data.
- **Pricing**: Free tier available with limited usage; paid plans for higher usage.
- **API Endpoint**: `https://api.tomtom.com/routing/1/calculateRoute/{start_lng},{start_lat}:{end_lng},{end_lat}`
- **Documentation**: [TomTom Routing API](https://developer.tomtom.com/routing-api/documentation)

**Example**:

```
https://api.tomtom.com/routing/1/calculateRoute/-122.4194,37.7749:34.0522,-118.2437/json?key=YOUR_API_KEY
```

---

### Summary of Services:

- **Google Maps Directions API**: Most widely used, highly reliable, but comes with costs.
- **OSRM / GraphHopper**: Open-source solutions based on OpenStreetMap, great for self-hosted or free solutions.
- **Mapbox Directions API**: Excellent for detailed mapping and navigation with a good free tier.
- **HERE Routing API**: Advanced routing with real-time traffic and multiple transport modes.
- **Bing Maps Directions API**: Another reliable alternative with good free tier access.
- **TomTom Routing API**: Focuses on navigation with traffic insights.

---

## GeoJson Visualization Properties

So, geojson features have a properties section in each feature. The properties section is a place to add additional key:value pairs associated with a feature. Some libraries like **MapBox** or **Leaflet** use specific key:value pairs to change the visualization of a feature (colors, alpha, icons, etc.). Not all of these properties are supported universally, and are different between libraries. However, I listed a bunch below as a reference. (source chat gpt).

Below is a list of common properties that are typically supported by **Leaflet** and **Mapbox** for **Points**, **LineStrings**, **MultiLineStrings**, and **Polygons**. These properties generally affect the **appearance** and **behavior** of the features. While the specifics might differ slightly between the two libraries, the core concepts are similar.

### 1. **Points** (Markers or Circles)

Points are typically rendered as markers, circle markers, or icons on the map. The following properties can be applied:

#### **Common Properties for Points:**

- **icon**: (Leaflet-specific) Allows you to specify a custom icon for the marker.
  - `L.icon({iconUrl: 'icon.png', iconSize: [32, 32]})`
- **radius**: (Used for circle markers) Defines the radius of the point in pixels or meters.
  - Example: `{ "radius": 10 }`
- **color**: The color of the point (usually for circle markers).
  - Example: `{ "color": "#FF0000" }` (Red color)
- **fillColor**: The color used to fill the marker (for circles and circle markers).
  - Example: `{ "fillColor": "#FFAAAA" }`
- **fillOpacity**: The opacity of the fill color. A value between 0 and 1.
  - Example: `{ "fillOpacity": 0.6 }`
- **opacity**: The overall opacity of the point (stroke or fill). A value between 0 and 1.
  - Example: `{ "opacity": 1.0 }`
- **weight**: (Leaflet-specific) The width of the point's outline (for circles).
  - Example: `{ "weight": 2 }`
- **popupContent**: (Optional, but commonly used) A popup to display additional information when the marker is clicked.
  - Example: `marker.bindPopup("This is a point!")`

#### **Leaflet-Specific Example:**

```javascript
L.circleMarker([51.5, -0.09], {
  color: "#3388ff", // Border color
  fillColor: "#3388ff", // Fill color
  fillOpacity: 0.5,
  radius: 10, // Circle radius
  weight: 2, // Border thickness
}).addTo(map);
```

#### **Mapbox-Specific Example:**

```javascript
map.addLayer({
  id: "point",
  type: "circle",
  source: "points",
  paint: {
    "circle-radius": 6, // Radius of the circle
    "circle-color": "#FF0000", // Circle color
    "circle-opacity": 0.8,
  },
});
```

### 2. **LineStrings and MultiLineStrings**

Lines are used to represent paths, routes, or boundaries. The following properties are commonly supported:

#### **Common Properties for LineStrings/MultiLineStrings:**

- **color / line-color**: The color of the line.
  - Example: `{ "color": "#FF0000" }` (Red color)
- **weight / line-width**: The thickness of the line.
  - Example: `{ "weight": 4 }` or `{ "line-width": 4 }`
- **opacity / line-opacity**: The opacity of the line. A value between 0 and 1.
  - Example: `{ "opacity": 0.5 }` or `{ "line-opacity": 0.5 }`
- **dashArray**: (Leaflet-specific) Allows the creation of dashed or dotted lines.
  - Example: `{ "dashArray": "5, 10" }` (5px dash followed by 10px space)
- **line-join**: (Mapbox-specific) Determines how the corners of the line are joined.
  - Example: `{ "line-join": "round" }`
- **line-cap**: (Mapbox-specific) Determines how the ends of the lines are drawn (butt, round, square).
  - Example: `{ "line-cap": "round" }`

#### **Leaflet-Specific Example:**

```javascript
L.polyline(
  [
    [51.505, -0.09],
    [51.51, -0.1],
    [51.51, -0.12],
  ],
  {
    color: "blue", // Line color
    weight: 5, // Line thickness
    opacity: 0.7, // Line opacity
    dashArray: "5, 5", // Dashes (5px line, 5px space)
  }
).addTo(map);
```

#### **Mapbox-Specific Example:**

```javascript
map.addLayer({
  id: "line-layer",
  type: "line",
  source: "lines",
  paint: {
    "line-color": "#FF0000", // Red line
    "line-width": 4, // Thickness of the line
    "line-opacity": 0.7, // Opacity
    "line-dasharray": [2, 4], // Dashed line (2px line, 4px space)
  },
});
```

### 3. **Polygons**

Polygons represent areas or boundaries. The following properties are commonly supported:

#### **Common Properties for Polygons:**

- **fillColor / fill-color**: The color used to fill the polygon.
  - Example: `{ "fillColor": "#FFAAAA" }` or `{ "fill-color": "#FFAAAA" }`
- **color / line-color**: The color of the polygon's outline.
  - Example: `{ "color": "#3388ff" }`
- **weight / line-width**: The thickness of the polygon's outline.
  - Example: `{ "weight": 3 }` or `{ "line-width": 3 }`
- **fillOpacity / fill-opacity**: The opacity of the fill color. A value between 0 and 1.
  - Example: `{ "fillOpacity": 0.6 }` or `{ "fill-opacity": 0.6 }`
- **opacity / line-opacity**: The opacity of the polygon's outline. A value between 0 and 1.
  - Example: `{ "opacity": 0.8 }`
- **dashArray**: (Leaflet-specific) If you want a dashed or dotted outline for the polygon.
  - Example: `{ "dashArray": "10, 10" }`

#### **Leaflet-Specific Example:**

```javascript
L.polygon(
  [
    [51.509, -0.08],
    [51.503, -0.06],
    [51.51, -0.047],
  ],
  {
    color: "green", // Border color
    fillColor: "#3388ff", // Fill color
    fillOpacity: 0.5, // Fill opacity
    weight: 3, // Border thickness
  }
).addTo(map);
```

#### **Mapbox-Specific Example:**

```javascript
map.addLayer({
  id: "polygon-layer",
  type: "fill",
  source: "polygons",
  paint: {
    "fill-color": "#00FF00", // Fill color
    "fill-opacity": 0.5, // Fill opacity
    "fill-outline-color": "#0000FF", // Border color
  },
});
```

### Additional Properties (Both Leaflet and Mapbox):

- **popupContent**: Popups are common for points and polygons to show more information when clicked.
- **tooltip**: (Leaflet-specific) Provides additional information in a hoverable tooltip.
- **interactive**: If set to `false`, the feature will not respond to mouse or touch events.
  - Example: `{ "interactive": false }`
- **zIndex**: Controls the stacking order of layers.
  - Example: `{ "zIndex": 1000 }`

### Mapbox-Specific Properties:

Mapbox supports a wide range of additional properties, especially for styling and interactivity:

- **line-gradient**: Apply a gradient along a line, useful for visualizing changes over the length of a line.
  - Example: `{ "line-gradient": ["interpolate", ["linear"], ["line-progress"], 0, "blue", 1, "red"] }`
- **text-field**: Display labels for features such as points, lines, or polygons.
  - Example: `{ "text-field": ["get", "name"] }`
- **circle-blur**: Applies a blur effect to points.
  - Example: `{ "circle-blur": 0.5 }`
- **icon-image**: Use custom icons or symbols for points.
  - Example: `{ "icon-image": "marker-icon" }`
- **symbol-placement**: Control how text or symbols are placed (e.g., along a line).
  - Example: `{ "symbol-placement": "line" }`

---

### Summary of Key Properties:

| Feature Type    | Key Properties for Leaflet and Mapbox                                       |
| --------------- | --------------------------------------------------------------------------- |
| **Points**      | `icon`, `radius`, `color`, `fillColor`, `fillOpacity`, `weight`, `popup`    |
| **LineStrings** | `color`, `weight`, `opacity`, `dashArray`, `line-join`, `line-cap`, `popup` |
| **Polygons**    | `fillColor`, `color`, `weight`, `fillOpacity`, `opacity`, `popup`           |

Both \*\*Leaflet

---

## Geojson.io Specific
```json
// COLOR RULES
// Colors can be in short form:
//   "#ace"
// or long form
//   "#aaccee"
// with or without the # prefix.
// Colors are interpreted the same as in CSS,
// in #RRGGBB and #RGB order.
// But other color formats or named colors
// are not supported
{
    "type": "FeatureCollection",
    "features": [{ "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [0, 0]
        },
        "properties": {
            // OPTIONAL: default ""
            // A title to show when this item is clicked or
            // hovered over
            "title": "A title",

            // OPTIONAL: default ""
            // A description to show when this item is clicked or
            // hovered over
            "description": "A description",

            // OPTIONAL: default "medium"
            // specify the size of the marker. sizes
            // can be different pixel sizes in different
            // implementations
            // Value must be one of
            // "small"
            // "medium"
            // "large"
            "marker-size": "medium",

            // OPTIONAL: default ""
            // a symbol to position in the center of this icon
            // if not provided or "", no symbol is overlaid
            // and only the marker is shown
            // Allowed values include
            // - Icon ID
            // - An integer 0 through 9
            // - A lowercase character "a" through "z"
            "marker-symbol": "bus",

            // OPTIONAL: default "7e7e7e"
            // the marker's color
            //
            // value must follow COLOR RULES
            "marker-color": "#fff",

            // OPTIONAL: default "555555"
            // the color of a line as part of a polygon, polyline, or
            // multigeometry
            //
            // value must follow COLOR RULES
            "stroke": "#555555",

            // OPTIONAL: default 1.0
            // the opacity of the line component of a polygon, polyline, or
            // multigeometry
            //
            // value must be a floating point number greater than or equal to
            // zero and less or equal to than one
            "stroke-opacity": 1.0,

            // OPTIONAL: default 2
            // the width of the line component of a polygon, polyline, or
            // multigeometry
            //
            // value must be a floating point number greater than or equal to 0
            "stroke-width": 2,

            // OPTIONAL: default "555555"
            // the color of the interior of a polygon
            //
            // value must follow COLOR RULES
            "fill": "#555555",

            // OPTIONAL: default 0.6
            // the opacity of the interior of a polygon. Implementations
            // may choose to set this to 0 for line features.
            //
            // value must be a floating point number greater than or equal to
            // zero and less or equal to than one
            "fill-opacity": 0.5
        }
    }]
}
```