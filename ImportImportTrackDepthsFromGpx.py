import arcpy
import os
import xml.etree.ElementTree as etree

GPX_ELEMENT_NAME = '{http://www.topografix.com/GPX/1/1}name'
GPX_ELEMENT_TRACK = '{http://www.topografix.com/GPX/1/1}trk'
GPX_ELEMENT_TRACK_POINT = '{http://www.topografix.com/GPX/1/1}trkpt'
GPX_ELEMENT_TRACK_POINT_EXTENSION = '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}TrackPointExtension'
GPX_ELEMENT_WATER_DEPTH = '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}depth'

gpx_file = arcpy.GetParameterAsText(0)
output_feature_class = arcpy.GetParameterAsText(1)

if arcpy.Exists(output_feature_class):
    arcpy.AddError("{0} already exists".format(output_feature_class))
    arcpy.AddMessage("The given feature class must not exist as it will be created internally")
    raise arcpy.ExecuteError

feature_class = arcpy.CreateFeatureclass_management(
    os.path.dirname(output_feature_class), os.path.basename(output_feature_class), 'POINT', has_z='ENABLED')[0]
tree = etree.parse(gpx_file)
tracks = tree.findall(GPX_ELEMENT_TRACK)

arcpy.env.autoCancelling = False

with arcpy.da.InsertCursor(feature_class, ['SHAPE@XY', 'SHAPE@Z']) as cursor:
    for track in tracks:
        if arcpy.env.isCancelled:
            break
        name = track.find(GPX_ELEMENT_NAME).text
        points = track.findall('.//' + GPX_ELEMENT_TRACK_POINT)
        for track_point in points:
            if arcpy.env.isCancelled:
                break
            depth = float(track_point.find('.//' + GPX_ELEMENT_WATER_DEPTH).text)
            xy = (float(track_point.attrib.get('lon')), float(track_point.attrib.get('lat')))
            cursor.insertRow([xy, -depth])
