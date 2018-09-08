#!/usr/bin/env python3

import sys
import geoip2.database

as_reader = geoip2.database.Reader('/geoip/GeoLite2-ASN.mmdb')
city_reader = geoip2.database.Reader('/geoip/GeoLite2-City.mmdb')

for line in sys.stdin:

    try:
        ips = line.strip()

        as_request = as_reader.asn(ips)
        city_request = city_reader.city(ips)

        asnum = as_request.autonomous_system_number
        asorg = as_request.autonomous_system_organization
        city = city_request.country.name

        print('{0}, {1}, {2}, {3}'.format(ips, asnum, asorg, city))

    except:

        print(ips)
        continue

as_reader.close()
city_reader.close()
