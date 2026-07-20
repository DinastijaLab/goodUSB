import usb_hid
import storage

usb_hid.set_interface_name('Standard USB Keyboard')
storage.getmount('/').label = 'MO_util'