A hypno remote soundboard that can be used long-distance over the internet.

See https://longjumpingcamel51.github.io/hypno_remote.htm if you just need a soundboard locally.


## USAGE

 - Start server.py on your device or deploy it using a service such as Heroku. Use the environment variable PORT to specify a port. If none is specified, 4080 will be used.

 - Open http://x.x.x.x:4080/dom on the dom's device and have them specify which commands they want.
 
 - Have the dom send the partner code they used during setup to the sub
 
 - Open http://x.x.x.x:4080/sub on the sub's device, have them enter the partner code and select a TTS voice to use.

 - Tap commands on the dom's device. They will be played from the sub's device.
