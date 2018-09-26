import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

key = sys.argv[1]
bus = sys.argv[2]


full_url = \
'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'\
% (key, bus)

#seen in class notes
response = urllib.urlopen(full_url)
data = response.read().decode("utf-8")
parsedjson = json.loads(data)
