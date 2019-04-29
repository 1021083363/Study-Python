import pyb
leds = [pyb.LED(i) for i in range(1,5)]
for l in leds:
	l.off()
n = 0
try:
	while True:
		n = (n+1)%4
		leds[n].toggle()
		pyb.delay(200)
finally:
	for l in leds:
		l.off()