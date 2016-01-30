"""
Tool to create GDAL vrt files in ArcMap.
Created for ArcGIS 10

Takes 3 arguments
1 - Folder path for input data (Mandatory)
2 - Type of file, string with extension (Mandatory)
3 - Output filename, inkluding path (Mandatory)

Created by Klas Karlsson 2016-01-30
"""

import arcpy, subprocess

# Get parameters from GUI
InFolder = arcpy.GetParameterAsText(0)
arcpy.AddMessage("Source Folder: " + InFolder)  
InType = arcpy.GetParameterAsText(1)  
arcpy.AddMessage("File Type: " + InType)
VrtFile = arcpy.GetParameterAsText(2)
arcpy.AddMessage("Output VRT: " + VrtFile)  

# Create Call String
CallString = "gdalbuildvrt " + VrtFile + " " + InFolder + "\\*." + InType  
arcpy.AddMessage(CallString)

# Execute the command
process = subprocess.Popen(CallString, stdout=subprocess.PIPE, creationflags=0x08000000)
process.wait()
