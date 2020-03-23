# metrohm_autolab_python
This exemplifies how to run a Metrohm Autolab PGSTAT302N with FRA/EIS and the true linear CV option in Python using the SDK

# Installing all the prerequisites
Go install the SDK and make sure to install **both** the Nova 1.11 and Nova 2.x version. You will then need to install pythonnet of the latest version
do this by
'''
pip install pythonnet
'''
This will give you the possibility of laoding a dll and interface it relatively esay from python 3.7+.

# Make you own procedures
After having installed the SDK and Nova 1.11 and 2.x you can go ahead and program your own procedures. Any procedure is comprised of commands that have CommandParameters i.e. you make a procedure with the command of applying a potential which then has the command parameter "applycurrent" (you specify that name) with a "Setpoint value" that you set to say 1e-5A.
What this code does is essentially nothing but loading a predefined procedure and allowing you to redefine the setpoint values.
This results in having general procedures like having **one** general Chronoamperometry prodeure where you then change values like duration or stop criteria. The herein shown examples are nothing but templates as procedures can be arbitraily complex.

# How does it work?
This code simply loads a predefined procedure:
```python
self.proc = self.inst.LoadProcedure(self.proceduresd[name])
```

```python
for comm, params in setpoints.items():
    for param, value in params.items():
        self.proc.Commands[comm].CommandParameters[param].Value = value
```
You can design a procedure in Nova 2.x but sometimes they are 
