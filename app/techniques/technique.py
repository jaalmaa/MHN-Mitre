import yara

class Techniques(object):

    def __init__(self):
        self.commands = {}
        self.indicators = []
    
    def validateIndicator(self, indicator: dict):
        '''@TODO: validate indicators dictionary'''
        pass
    
    def loadRules(self, files: dict):
        '''load a dictionary containing indicators for a MITRE ATT&CK Tactic'''
        return yara.compile(filepaths=files)
    
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