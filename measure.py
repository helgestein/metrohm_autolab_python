from autolab import Autolab

autolab_conf = dict(basep = r"C:\Program Files\Metrohm Autolab\Autolab SDK 1.11",
                    procp = r"C:\Users\Helge\OneDrive\Documents\git\auro-master\auro-master\conf\echemprocedures",
                    hwsetupf = r"C:\ProgramData\Metrohm Autolab\12.0\HardwareSetup.AUT88172.xml",
                    micsetupf = r"C:\Program Files\Metrohm Autolab\Autolab SDK 1.11\Hardware Setup Files\Adk.bin",
                    proceuduresd = {'cp': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\CP.nox',
                                    'ca': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\CA.nox',
                                    'cv': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\CV.nox',
                                    'eis': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\EIS.nox',
                                    'ocp': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\OCP.nox',
                                    'on': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\ON.nox',
                                    'off': r'C:\\Users\\Helge\\OneDrive\\Documents\\git\\auro-master\\auro-master\\conf\\echemprocedures\\OFF.nox'})

a = Autolab(autolab_conf)

conf_ca = {'procedure': 'ca',
           'setpoints': {'applypotential': {'Setpoint value': 0.01},
                         'recordsignal': {'Duration': 10}},
           'plot': 'tCV',
           'onoffafter': 'off',
           'safepath': r'C:\Users\Helge\OneDrive\Documents\git\auro-master\auro-master\temp',
           'filename': 'ca.nox',
           'parseinstructions': ['recordsignal']}
a.performMeasurement(conf_ca)

conf_cp = {'procedure': 'cp',
           'setpoints': {'applycurrent': {'Setpoint value': 10**-4},
                         'recordsignal': {'Duration': 10}},
           'plot': 'tCV',
           'onoffafter': 'off',
           'safepath': r'C:\Users\Helge\OneDrive\Documents\git\auro-master\auro-master\temp',
           'filename': 'cp.nox',
           'parseinstructions': ['recordsignal']}

a.performMeasurement(conf_cp)

conf_cv = {'procedure': 'cv',
           'setpoints': {
               'FHSetSetpointPotential': {'Setpoint value':0},
               'FHWait': {'Time':2},
               'CVLinearScanAdc164': {'StartValue': 0.0,
                                      'UpperVertex': 0.5,
                                      'LowerVertex': -0.5,
                                      'NumberOfStopCrossings': 2,
                                      'ScanRate': 0.1}},
           'plot': 'tCV',
           'onoffafter': 'off',
           'safepath': r'C:\Users\Helge\OneDrive\Documents\Engineering\autolab\data',
           'filename': 'cv.nox',
           'parseinstructions': ['CVLinearScanAdc164']}
a.performMeasurement(conf_cv)

conf_eis = {'procedure': 'eis',
            'setpoints': {'FHSetSetpointPotential': {'Setpoint value': 0.01}},
            'plot': 'impedance',
            'onoffafter': 'off',
            'safepath': r"C:\Users\Helge\OneDrive\Documents\git\auro-master\auro-master\temp",
            'filename': 'eis.nox',
            'parseinstructions': ['FIAMeasPotentiostatic']}
a.performMeasurement(conf_eis)
