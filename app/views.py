from flask import Flask, jsonify, Blueprint
from flask_pymongo import PyMongo

from app import mongo

honeypotRoutes = Blueprint('info', __name__)

'''
    For now, these are only applicable for cowrie instances:
        In the future (after dissertation is complete), expand to different honeypots

    idea:
        Pull IoC's (e.g. domains/IPs) from urls field and create a feed (out of scope of dissertation))
'''

@honeypotRoutes.route('/honeypot/sessions')
def getAllHoneypotSessions():
    '''returns all sessions for all sensors'''
    return jsonify({'success': True, 'response': 'get_events function'}), 200


@honeypotRoutes.route('/honeypot/sessions/<ident>')
def getHoneypotEvents(ident):
    '''returns all sessions for a sensor'''
    return jsonify({'success': True, 'response': 'get_events function'}), 200


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@honeypotRoutes.route('/honeypot/sessions/cowrie', methods=['GET'])
def getHoneypotSessions():
    '''returns all sessions for a honeypot type e.g. cowrie'''
    try:
        data = [resource for resource in mongo.db.hpfeed.find({ 'channel': 'cowrie.sessions' }, { '_id': 0 })]
    except:
        return jsonify({ 'success': False, 'response': 'An Error Occurred Communicating with the Database' }), 500
    return jsonify({ 'success': True, 'response': data }), 200


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@honeypotRoutes.route('/honeypot/sessions/cowrie/logins', methods=['GET'])
def getHoneypotLogins():
    '''returns all sessions where there was a successful login'''
    try:
        data = [resource for resource in mongo.db.hpfeed.find({ 'payload.commands': { '$ne': [] } }, { '_id': 0 })]
    except:
        return jsonify({ 'success': False, 'response': 'An Error Occurred Communicating with the Database' }), 500
    try:
        formattedResponses = []
        for session in data:
            formattedResponse = {
                "metadata": {
                    "session": session['payload']['session'],
                    "channel": session['channel'],
                    "sensor-uuid": session['ident'],
                    "protocol": session['payload']['protocol'],
                    "timestamps": {
                        "startTime": session['payload']['startTime'],
                        "endTime": session['timestamp']
                    }
                },
                "payload": {
                    "commands": list(filter(None, session['payload']['commands'])),
                    "credentials": {
                        "username": session['payload']['loggedin'][0],
                        "password": session['payload']['loggedin'][1]
                    },
                    "IOCs": {
                        "urls": session['payload']['urls'],
                        "hashes": session['payload']['hashes']
                    }
                }
            }
            formattedResponses.append(formattedResponse)
        return jsonify({ 'success': True, 'response': formattedResponses }), 200
    except:
        return jsonify({ 'success': False, 'response': 'An Error Occurred Retuning the Data' }), 500


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@honeypotRoutes.route('/honeypot/sensor/cowrie', methods=['GET'])
def getHoneypotSensors():
    '''returns the idents of all registered sensors of a given honeypot type'''
    try:
        data = [resource for resource in mongo.db.hpfeed.find({ 'channel': 'cowrie.sessions' }, { '_id': 0, 'ident': 1, 'channel': 1 }).distinct('ident')]
    except:
        return jsonify({ 'success': False, 'response': 'An Error Occurred Communicating with the Database' })
    return jsonify({ 'success': True, 'response': data }), 200


# @TODO: Replace cowrie in address with a generalized parameter to query different honeypots
@honeypotRoutes.route('/honeypot/sensor/<ident>', methods=['GET'])
def getHoneypotSensor(ident):
    '''returns all sessions associated with an individual honeypot sensor e.g cowrie with ident=ident
        the ident parameter is contained within '''
    try:
        data = [resource for resource in mongo.db.hpfeed.find({ 'ident': ident }, { '_id': 0 })]
    except:
        return jsonify({ 'success': False, 'response': 'An Error Occurred Communicating with the Database' }), 500
    return jsonify({ 'success': True, 'response': data }), 200

    