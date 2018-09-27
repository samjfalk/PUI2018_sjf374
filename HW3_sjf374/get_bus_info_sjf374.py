import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# if you add more than one word as argument it will give you an error as well--from class
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info_sjf374.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

#choose the first input as key and the second one as the bus
key = sys.argv[1]
bus = sys.argv[2]
file = sys.argv[3]

def bus_location(key, bus, file):
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

	#open file to write
	fout = open(file, "w")

	#create headers
	fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

	#show each bus and their corresponding location
	for x in busactivity:
		lat = str(x['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
		Long = str(x['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
		try:
			stopname =  str(x['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
		except:
			stopname= 'N/A'
		try:
			status =  str(x['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
		except:
			status = 'N/A'

		fout.write(lat+','+Long+','+stopname+','+status+'\n')

bus_location(key, bus, file)

