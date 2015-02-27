"""
TITLE:          Google Geocoder

CREATION DATE:  7/22/2014
CREATED BY:     Tom Lee

STATUS:         It works. Enter the input and output files manually.
                Input file is a text file, one address per row.
"""

#Import modules
import urllib2
from bs4 import BeautifulSoup
from time import strftime
import time

#Print start
time = strftime("%Y-%m-%d %H:%M:%S")
print "Geocoding started " + str(time)


#Geocode function
def geocode(fAddress):
    fAddress = fAddress.replace(" ", "+")
    try:
        url="http://maps.googleapis.com/maps/api/geocode/xml?address=%s" % fAddress
        response = urllib2.urlopen(url)
        xmlgeocode = response.read()
        soup = BeautifulSoup(xmlgeocode)

        status = str(soup.status.string)
        address = str(soup.formatted_address.string)
        lat = str(soup.geometry.location.lat.string)
        lng = str(soup.geometry.location.lng.string)
        loc_type = str(soup.location_type.string)

    except:
        try:
            #If there is an error, wait 2 seconds and try again
            import time
            time.sleep(2)
            fAddress = fAddress.replace(".", "+")
            fAddress = fAddress.replace(" ", "+")
                        
            url="http://maps.googleapis.com/maps/api/geocode/xml?address=%s" % fAddress
            response = urllib2.urlopen(url)
            xmlgeocode = response.read()
            soup = BeautifulSoup(xmlgeocode)

            status = str(soup.status.string)
            address = str(soup.formatted_address.string)
            lat = str(soup.geometry.location.lat.string)
            lng = str(soup.geometry.location.lng.string)
            loc_type = str(soup.location_type.string)

        except:
            #If it doesn't work a second time, return an error
            status = "ERROR"
            address = str(fAddress)
            lat = "0"
            lng = "0"
            loc_type = "Error"

    return [status, loc_type, lat, lng, address]

#START

#Input
inputFile = open(r"C:\Users\Lee\Documents\Misc\Scripts\Addresses_20150130.txt", 'r')

#Output file - start writing
outTxtFile = r"C:\Users\Lee\Documents\Misc\Scripts\Addresses_out20150130.txt"
outFile = open(outTxtFile, "w")

#Geocode input using function
for line in inputFile.readlines():
    inAddress = str(line)
    inAddress = inAddress.strip()
    geocodeResult = geocode(inAddress)

    #Process output of function
    status = geocodeResult[0]
    loc_type = geocodeResult[1]
    lat = geocodeResult[2]
    lng = geocodeResult[3]
    outAddress = geocodeResult[4]
    print status, loc_type, outAddress

    #write to output file
    outFile.write(str(status + "|" + loc_type + "|" + str(lat) + "|" + str(lng) + "|" + outAddress + "|" + inAddress + "\n"))

#Close output file
outFile.close()

#Print end
time = strftime("%Y-%m-%d %H:%M:%S")
print "Geocoding Completed " + str(time)




