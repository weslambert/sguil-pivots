`genEventFIR.py` is a Python script used to generate an event in FIR (Fast Incident Response).  It can be placed in `/usr/lib/sguil`.   

`fir.conf` is a configuration file that stores the address of your FIR instance and your desired user's API key.   

`extdata.tcl` should replace the existing file in `/usr/lib/sguil` and is used to call `genEventFIR.py`.   

`squil.tk` defines the menu(s) and `proc(s)` to call when choosing an option in the Sguil client.    

After copying and modifying the above files as needed, hop into the Sguil client and right-click the status or an event.

From there, you should have the option to `Generate a Case/Event`, then choose from the options.
