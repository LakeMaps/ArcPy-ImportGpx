<p align="center">
    <a href="https://github.com/LakeMaps">
        <img src="https://avatars.githubusercontent.com/u/20632669?s=200" alt="Lake Maps NL" />
    </a>
</p>
<h1 align="center"><code>ImportGpx</code> ArcGIS Pro Script Tool</h1>

An [ArcGIS Pro](http://www.esri.com/arcgis/products/arcgis-pro/overview/) script tool to import track depths from a [GPX file] that uses Garmin's Track Point Extension. This was tested and is primarily used with GPX files produced by a [Garmin echoMAP™ 42dv](https://buy.garmin.com/en-CA/CA/p/148128).

  [GPX file]:https://en.wikipedia.org/wiki/GPS_Exchange_Format

Build status
------------

| Branch        | Build Status            |
| ------------- | ----------------------- |
| `master`      | [![Build Status][1]][3] |
| `development` | [![Build Status][2]][3] |

  [1]:https://travis-ci.org/LakeMaps/ArcPy-ImportGpx.svg?branch=master
  [2]:https://travis-ci.org/LakeMaps/ArcPy-ImportGpx.svg?branch=development
  [3]:https://travis-ci.org/LakeMaps/ArcPy-ImportGpx

Installation
------------

How do I get this into an ArcGIS Pro project?

1. Download this repository
2. Open or create an ArcGIS Pro project
1. Right-click a toolbox in the Project, select *New > Script*

    <img alt="New > Script" src="https://user-images.githubusercontent.com/1623628/29491094-758b9214-852b-11e7-9470-ed52b842721d.png">

2. Populate the metadata fields for the script

    The *Script File* field should contain the path to the script in the downloaded copy of this repository—the remaining fields do not need to contain anything in particuar. The *Parameters* tab for the script should have the following two rows, one input file and one output feature class:

    | Label | Name | Data Type | Type | Direction | Category | Filter |
    | ----- | ---- | --------- | ---- | --------- | -------- | ------ |
    | GPX file | `GPX_file` | File | Required | Input | | File\* |
    | Output feature class | `Output_feature_class` | Feature Class | Required | Output | | Feature Type\*\* |

    \* Add "gpx" to the list of extensions for the File Filter
    \*\* Select *Point* for the Feature Type Filter

    <img alt="Script General Information" src="https://user-images.githubusercontent.com/1623628/29491076-f0d9e354-852a-11e7-8549-03c7f1e87dc3.PNG">
    <img alt="Script Parameters" src="https://user-images.githubusercontent.com/1623628/29491073-f0ceb2ea-852a-11e7-92b7-7b29f72aca1a.PNG">
