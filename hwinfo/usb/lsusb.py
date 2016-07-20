"""Module for inspecting USB device info"""

from hwinfo.util import CommandParser


class LsusbParser(CommandParser):

    ITEM_REGEXS = [
        r'Bus\s+(?P<usb_bus_id>\d+)\s+Device\s+(?P<usb_device_id>\d+).+ID\s(?P<usb_vendor_id>\w+):(?P<usb_product_id>\w+)\s(?P<usb_device_name>.+)'
    ]

    ITEM_SEPERATOR = "\n"

    MUST_HAVE_FIELDS = [
        'usb_bus_id',
        'usb_device_id',
        'usb_vendor_id',
        'usb_product_id',
        'usb_device_name'
    ]
