Install pip3 and PyMISP:    
`sudo apt-get install python3-pip`    
`sudo pip3 install pymisp`    

Navigate to Sguil dir and clone PyMISP GH Repo:    
`cd /usr/lib/sguil`    
`git clone https://github.com/MISP/PyMISP.git && cd PyMISP`    

Install:    
`git submodule update --init`     
`sudo pip3 install -I .`     

Set up authentication to MISP instance:    
`cd /usr/lib/sguil/PyMISP/examples`    
`cp keys.py.sample keys.py`    
`sudo vi keys.py`  (Specify URL key and API key)    

Add the following to top of /usr/lib/sguil/PyMISP/examples/create_events.py:    

    import sys
    sys.path.append('/usr/lib/sguil/PyMISP')
    
Clone this repo and copy the following files to their proper directories:    
Copy `sguil.tk` to `/usr/bin/sguil.tk`.    
Copy `extdata.tcl` to `/usr/lib/sguil/extdata.tcl`.   
