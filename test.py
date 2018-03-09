#!/usr/bin/env python
# encoding: utf-8
username = 'BDTEST@business-api.mondialrelay.com'
password = ''
customerid = 'BDTEST'
debug = True

from mondialrelay.picking import *
from base64 import decodestring

with API(username, password, customerid, debug=debug) as mondialrelay_api:
    print "Test connection"
    print mondialrelay_api.test_connection()

with Picking(username, password, customerid, debug=debug) as picking_api:
    print "Send a new picking to MondialRelay - Label PDF"

    data = {}
    data['OrderNo'] = '123456'
    data['SenderFirstname'] = 'NaN-TIC'
    data['SenderStreetname'] = 'Rambla Iberia'
    data['SenderCountryCode'] = 'ES'
    data['SenderPostCode'] = '08205'
    data['SenderCity'] = 'Sabadell'
    data['SenderPhoneNo'] = '+34935531803'
    data['SenderEmail'] = 'info@nan-tic.com'
    data['RecipientFirstname'] = 'Raimon Esteve'
    data['RecipientStreetname'] = 'Durruti, 1937, 4art 2ona'
    data['RecipientCountryCode'] = 'FR'
    data['RecipientPostCode'] = '66210'
    data['RecipientCity'] = 'Mont Luis'
    data['RecipientPhoneNo'] = '+34935531803'
    data['RecipientEmail'] = 'info@domain.com'
    data['DeliveryInstruction'] = 'Testing MondialRelay API'
    data['DeliveryLocation'] = 'FR-66974'

    reference, label, error = picking_api.create(data)
    if error:
        print error
    else:
        print "Picking send %s" % reference
        with open("/tmp/mondialrelay-label.pdf","wb") as f:
            f.write(label)
        print "Generated PDF label in /tmp/mondialrelay-label.pdf"
