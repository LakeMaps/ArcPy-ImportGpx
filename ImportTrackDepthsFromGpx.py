import arcpy
import os
import numpy
import xml.etree.ElementTree as etree

GPX_ELEMENT_NAME = '{http://www.topografix.com/GPX/1/1}name'
GPX_ELEMENT_TIME = '{http://www.topografix.com/GPX/1/1}time'
GPX_ELEMENT_TRACK = '{http://www.topografix.com/GPX/1/1}trk'
GPX_ELEMENT_TRACK_POINT = '{http://www.topografix.com/GPX/1/1}trkpt'
GPX_ELEMENT_TRACK_POINT_EXTENSION = '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}TrackPointExtension'
GPX_ELEMENT_WATER_DEPTH = '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}depth'

gpx_file = arcpy.GetParameterAsText(0)
output_feature_class = arcpy.GetParameterAsText(1)

if arcpy.Exists(output_feature_class):
    arcpy.AddError('{0} already exists'.format(output_feature_class))
    arcpy.AddMessage('The given feature class must not exist as it will be created internally')
    raise arcpy.ExecuteError

tree = etree.parse(gpx_file)
tracks = tree.findall(GPX_ELEMENT_TRACK)
gpx_points = []

arcpy.env.autoCancelling = False

for track in tracks:
    if arcpy.env.isCancelled:
        break
    name = track.findtext(GPX_ELEMENT_NAME)
    points = track.findall('.//' + GPX_ELEMENT_TRACK_POINT)
    for track_point in points:
        if arcpy.env.isCancelled:
            break
        depth_element = track_point.find('.//' + GPX_ELEMENT_WATER_DEPTH)
        if depth_element is None:
            continue
        timestamp = track_point.findtext('.//' + GPX_ELEMENT_TIME)
        depth = float(depth_element.text)
        gpx_points.append((
            float(track_point.attrib.get('lon')), float(track_point.attrib.get('lat')), -depth, timestamp, name, depth))

feature_class_array = numpy.array(gpx_points, numpy.dtype(
    [
        ('x', numpy.float),
        ('y', numpy.float),
        ('z', numpy.float),
        ('Timestamp', numpy.bytes_, 32),
        ('Track Name', numpy.bytes_, 32),
        ('Water Depth', numpy.float)
    ]))
wgs84 = arcpy.SpatialReference(4326, 115700)
arcpy.da.NumPyArrayToFeatureClass(feature_class_array, output_feature_class, ('x', 'y', 'z'), wgs84)
