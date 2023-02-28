# pH_Module_Controller
This repo interfaces with the pH module controller submethod library.

Note, there is a small bug in the Hamilton 


## Usage Instructions
1. Make sure to git pull the latest version of PyHamilton
2. **Bug fix** In `C:\Program Files (x86)\HAMILTON\Library\Hamilton pH Module\Hamilton pH Station Washer Module.hsl`, add
the line `variable o_strErrorCode("");` to line 916.
3. Copy the file `Configuration COM 1.xls` to `C:\Program Files (x86)\HAMILTON\Config\Hamilton pH Module`. Edit
this file directly to change your configuration, or use the Configuration demo method.
4. Run `py robot_method.py`
