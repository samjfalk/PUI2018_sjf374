import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# if you add more than one word as argument it will give you an error as well--from class
if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_sjf374.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

#choose the first input as key and the second one as the bus
key = sys.argv[1]
bus = sys.argv[2]

def bus_location(key, bus):
	#in case it is input as lower case-- mta does not recognize it
	bus = bus.upper()
	#input variables into the URL
	full_url = \
	'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'\
	% (key, bus)

	#seen in class notes
	response = urllib.urlopen(full_url)
	data = response.read().decode("utf-8")
	parsedjson = json.loads(data, parse_constant= True)

	#filter down dictionaries to dictionary with vehicle activity
	busactivity = parsedjson['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	print ('Bus Line : ' + bus)

	#find how many buses
	print ('Number of Active Buses : ' + str(len(busactivity)))

	#show each bus and their corresponding location
	i = 1
	for x in busactivity:
	    print ('Bus %s is at latitude %s and longitude %s' \
	    	% (i, str(x['MonitoredVehicleJourney']['VehicleLocation']['Latitude']), str(x['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])))
	    i+=1

bus_location(key, bus)