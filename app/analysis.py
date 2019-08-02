'''
    this file contains views for accessing the MITRE ATT&CK analysis 
    for honeypot sessions
'''

from flask import Flask, jsonify, Blueprint
from flask_pymongo import PyMongo
import os
import requests
import yara
import sys

from app import mongo
from app.techniques.technique import Techniques

techniques = Techniques()
# TODO: more elegant way of listing all of the rule files and creating a dict

analysisRoutes = Blueprint('analysis', __name__)

def prettyPrintAnalysis(analysis: list):
    for element in analysis:
        if element['techniques'] != []:
            print('Techniques Identified: {0}\nCommand Executed:\n{1}\n'.format(element['techniques'], element['command']))

@analysisRoutes.route('/analysis', methods=['GET'])
def getAnalysis():
    '''returns analysis for all honeypots'''
    return jsonify({'success': True, 'response': 'analysis'})


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@analysisRoutes.route('/analysis/cowrie', methods=['GET'])
def getHoneypotAnalysis():
    '''returns analysis for a specific honeypot'''
    rules = techniques.loadRules({
    'T1070': os.path.abspath('app/techniques/defenseEvasion/T1070'),
    'T1107': os.path.abspath('app/techniques/defenseEvasion/T1107'),
    'T1139': os.path.abspath('app/techniques/defenseEvasion/T1139'),
    'T1146': os.path.abspath('app/techniques/defenseEvasion/T1146'),
    'T1148': os.path.abspath('app/techniques/defenseEvasion/T1148')
    })
    sessions = requests.get('http://localhost:5000/honeypot/sessions/cowrie/logins').json()         # @TODO: Get from config && @TODO: Instead of request, use helper function to access the DB and get the correct format
    analysis = []
    for session in sessions['response']:
        commands = [command for command in session['payload']['commands']]
        for command in commands:
            analysis.append({'command': command, 'techniques': rules.match(data=command)})
    prettyPrintAnalysis(analysis)

    return jsonify({ 'success': True, 'response': 'analysis complete' })