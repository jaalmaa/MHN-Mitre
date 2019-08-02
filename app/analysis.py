'''
    this file contains views for accessing the MITRE ATT&CK analysis 
    for honeypot sessions
'''

from flask import Flask, jsonify, Blueprint
from flask_pymongo import PyMongo
import requests

from app import mongo
from app.techniques.technique import Techniques

from app.techniques.collection import *
from app.techniques.commandAndControl import *
from app.techniques.credentialAccess import *
from app.techniques.defenseEvasion import T1146
from app.techniques.discovery import *
from app.techniques.execution import *
from app.techniques.impact import *
from app.techniques.initialAccess import *
from app.techniques.lateralMovement import *
from app.techniques.persistence import *
from app.techniques.privilegeEscalation import *

# initialize techniques object (stores indicators for analysis)
# @TODO: Write a function to go through all imported packages from app.techniques and load the modules from each of the subpackages
# This is fine for now as it is just a proof of concept, but any further development requires some serious refactoring 
techniques = Techniques()
techniques.loadIndicator(T1146.clearHistory)

analysisRoutes = Blueprint('analysis', __name__)

@analysisRoutes.route('/analysis', methods=['GET'])
def getAnalysis():
    '''returns analysis for all honeypots'''
    return jsonify({'success': True, 'response': 'analysis'})


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@analysisRoutes.route('/analysis/cowrie', methods=['GET'])
def getHoneypotAnalysis():
    '''returns analysis for a specific honeypot'''
    sessions = requests.get('http://localhost:5000/honeypot/sessions/cowrie/logins').json()         # @TODO: Get from config && @TODO: Instead of request, use helper function to access the DB and get the correct format
    analyzed_sessions = []
    test_session = sessions['response'][6]
    analysis = techniques.analyze(test_session)
    analyzed_sessions.append(analysis)

    return jsonify({ 'success': True, 'response': sessions })