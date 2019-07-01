class Techniques(object):
    '''generic template for MITRE ATT&CK techniques
    
        requires a signature for technique behavior
        of the following form:
        {
            'commands': [
                {
                    'command': <command>,
                    'arguments': [<optional arguments>]
                }
            ],
            'requirements': [requirements] (i.e. previous unsuccessful 
                                            login if we're looking for brute force)
        }'''

    def __init__(self):
        self.indicators = {}
    
    def validateIndicator(self, indicator: dict):
        '''@TODO: validate indicators dictionary'''
        pass
    
    def loadIndicator(self, indicators: dict):
        '''load a dictionary containing indicators for a MITRE ATT&CK Tactic'''
        self.indicators.append(indicators)