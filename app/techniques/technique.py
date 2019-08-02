class Techniques(object):
    '''generic template for MITRE ATT&CK techniques
        These function very similarly to YARA rules by detecting strings

        In future, change the strings to regex to match commands instead of hard-coded commands
    
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
        self.commands = {}
        self.indicators = []
    
    def validateIndicator(self, indicator: dict):
        '''@TODO: validate indicators dictionary'''
        pass
    
    def loadIndicator(self, indicators: dict):
        '''load a dictionary containing indicators for a MITRE ATT&CK Tactic'''
        self.indicators.append(indicators)
    
    def analyze(self, session: dict):
        import sys
        '''analyzes a session and looks for loaded indicators within the session data'''
        strings = [command.split() for command in session['payload']['commands']][0]
        for indicator in self.indicators:
            for string in strings:
                if string.strip(';') in indicator['strings']:
                    print('\nTechnique detected:', indicator['ID'], ':', indicator['name'], '\nAlerted by string:', string, 'in commands executed', file=sys.stderr)

    
    def analyzeSessions(self, sessions: list):
        '''analyze a list of sessions against all loaded indicators'''
        pass