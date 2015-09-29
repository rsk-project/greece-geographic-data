from osgeo import ogr

def kml2geojson(kml_file):
    drv = ogr.GetDriverByName('KML')
    kml_ds = drv.Open(kml_file)
    for kml_lyr in kml_ds:
        for feat in kml_lyr:
            print feat.ExportToJson()

kml2geojson('kml/county.kml')