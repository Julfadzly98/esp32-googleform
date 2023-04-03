from boot import connect
import urequests
from time import sleep

pin = machine.Pin(0, 1,  machine.Pin.OUT) #D2D4

connect()



while True:
  sleep(1) # do every 60 seconds
  h = {'content-type' : 'application/x-www-form-urlencoded'}
  form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeIplALqZE19SQyhaeirgWAINPK5KjUn3uwXGOXT8QJfBM7IQ/formResponse?usp=pp_url&'
  form_data = 'entry.561083855=' + 'entry.561083855=' str(pin)
  r = urequests.post(form_url, data=form_data, headers=h)
  r.status_code
  r.close()
  print("check google form")
