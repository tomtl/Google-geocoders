"""
Title:          Geocoder

Creation date:  7/22/2014
Created by:     Tom Lee

Status:         It works. Input and output text files need to be
                manually entered.
"""

#Import modules
from geopy import geocoders
from time import strftime

#Print start
time = strftime("%Y-%m-%d %H:%M:%S")
print "Geocoding started " + str(time)


#Google geocode function
def goGeocode(fAddress):
    g = geocoders.GoogleV3()
    try:
        place, (lat, lng) = g.geocode(fAddress)
        print "%s: %.5f, %.5f" % (place, lat, lng)
        
    except:
        print "Error", fAddress
        lat = 0.000
        lng = 0.000
        place = fAddress

    return (lat, lng, place)


#START HERE
inputFile = open(r"C:\Users\Lee\Documents\Misc\Scripts\Addresses_20140819.txt", 'r')

#Output file - start writing
outTxtFile = r"C:\Users\Lee\Documents\Misc\Scripts\Addresses_out20140819b.txt"
outFile = open(outTxtFile, "w")

#Read through input file and use geocode function
for line in inputFile.readlines():
    address = str(line)
    address = address.strip()
    result = goGeocode(address)
    #reformat geocode output
    lat = result[0]
    lng = result[1]
    place = result[2:]
    place = "%s" %(place)
    print lat, lng, place
    #write to output file
    outFile.write(str(str(lat) + "," + str(lng) + "," + place + "\n"))

#Close output file
outFile.close()

#Print end
time = strftime("%Y-%m-%d %H:%M:%S")
print "Geocoding Completed " + str(time)
