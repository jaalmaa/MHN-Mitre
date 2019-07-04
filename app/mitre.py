'''
    this file contains views for accessing the MITRE ATT&CK analysis 
    for honeypot sessions
'''

from flask import Flask, jsonify, Blueprint
from flask_pymongo import PyMongo

from app import mongo
from techniques.technique import Techniques

from techniques.collection import *
from techniques.commandAndControl import *
from techniques.credentialAccess import *
from techniques.defenseEvasion import *
from techniques.discovery import *
from techniques.execution import *
from techniques.impact import *
from techniques.initialAccess import *
from techniques.lateralMovement import *
from techniques.persistence import *
from techniques.privilegeEscalation import *

# initialize techniques object (stores indicators for analysis)
techniques = Techniques()

mitreRoutes = Blueprint('mitre', __name__)

@mitreRoutes.route('/analysis', methods=['GET'])
def getAnalysis():
    '''returns analysis for all honeypots'''
    return jsonify({'success': True, 'response': 'analysis'})


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@mitreRoutes.route('/analysis/cowrie', methods=['GET'])
def getHoneypotAnalysis():
    '''returns analysis for a specific honeypot'''
    return jsonify({'success': True, 'response': 'honeypot analysis'})