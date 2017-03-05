import os, json
from pymongo import MongoClient
from flask import jsonify, request, Response, redirect
from twilio.rest import TwilioRestClient
BASE_PATH = str(os.path.realpath(__file__))
BASE_PATH = BASE_PATH.replace('basicServer_services.pyc', '')
BASE_PATH = BASE_PATH.replace('basicServer_services.pyo', '')
BASE_PATH = BASE_PATH.replace('basicServer_services.py', '')

CLASS_PATH = BASE_PATH.replace('classes', '')
connection_string = "mongodb://localhost"
connection = MongoClient(connection_string)
database = connection.Smart_Lot

def register_services(app, WSGI_PATH_PREFIX):
    BaseServices(app, WSGI_PATH_PREFIX)


class BaseServices:
    def __init__(self, app, WSGI_PATH_PREFIX):
        self.session_users = {}
        self.app = app
        print'----------------------------------------------------------------------------'
        print '                        Getting Elastic Config'
        # self.connections = self.app.config['Managers'].get('Database').connections
        # db = self.app.config['Managers'].get('Database')
        # self.connections = db.connections
        # con_config = self.connections['rca'][0]
        # con_config['http_auth'] = (con_config['user'], con_config['password'])
        # self.parthealth = 'rca-rca'
        # self.rcaMap = 'rca-rca_map'
        # self.reflexChain = 'rca-reflex_chain'
        # self.keymap = {
        #     'Data Models': 'file_type',
        #     'Systems': 'source',
        #     'TSL Gap': 'metric_tslgap',
        #     'DOS': 'metric_dos',
        #     'PAL': 'metric_pal',
        #     'FAC': 'metric_fac',
        #     'OTD': 'metric_otd'
        # }
        print'----------------------------------------------------------------------------'
        print '                        Elastic is Stretching'
        print'----------------------------------------------------------------------------'
        print '                        Register MDMDQ API'
        print'----------------------------------------------------------------------------'
        #       ----------------------------------------------------------------------------
        #                                 MDMDQ Services
        #       ----------------------------------------------------------------------------
        #         self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/dates', 'dates', self.dates, methods=['POST'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/demo', 'demo', self.demo, methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/giveJson', 'giveJson', self.giveJson, methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/add', 'add', self.add, methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/buttonPressed', 'buttonPressed', self.buttonPressed, methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/testPymongo', 'testPymongo', self.testPymongo,
                              methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/vehicleExit', 'vehicleExit', self.vehicleExit,
                              methods=['POST', 'GET'])

        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/getAllParkingData', 'getAllParkingData', self.getAllParkingData,
                              methods=['POST', 'GET'])



    def demo(self):
        return  'In DEMO method'

    def giveJson(self):
        _d = {i:i*'S' for i in xrange(55)}
        return jsonify(_d)

    def getparams(self, request):
        return request.form if (request.method == 'POST') else request.args


    def buttonPressed(self):
        print "**************BUTTON PRESSED******************"
        params_data = request.form if (request.method == 'POST') else request.args
        id = params_data.get("id")
        status = params_data.get("status")
        print "id = ",id
        print "status = ",status
        self.updateTotalOccupied(id,+1)

        # self.sendMessage("**************BUTTON PRESSED******************")
        return "**************BUTTON PRESSED******************"

    def add(self):
        #http://0.0.0.0:5050/basicServer/services/add?a=100&b=200
        params = self.getparams(request)
        a =params.get('a',5)
        b =params.get('b',10)
        # print params
        # a = 5
        # b= 10
        c = int(a)+int(b)
        return str(c)
    def testPymongo(self):
        user = database.totalAvailable.find_one()
        # print user
        record = self.getTotalCount("IN102")
        print "total count from DB=",record["total"]
        print "total occupied from DB=", record["occupied"]
        # print { k: user[k] for k in user}
        return jsonify({ k: str(record[k]) for k in record})

    def vehicleExit(self):
        print "**************VEHICLE LEFT******************"
        params_data = request.form if (request.method == 'POST') else request.args
        id = params_data.get("id")
        status = params_data.get("status")
        print "id = ", id
        print "status = ", status
        # id = "IN101"
        self.updateTotalOccupied(id, -1)
        # self.sendMessage("**************VEHICLE LEFT******************")
        return "**************VEHICLE LEFT******************"

    def updateTotalOccupied(self,parkingLot,incrementValue=1):
        record = self.getTotalCount(parkingLot)
        calculatedCount = int(record["occupied"])
        calculatedCount = calculatedCount + incrementValue
        result = database.totalAvailable.update_one({"id":parkingLot},{"$set":{"occupied":calculatedCount}})
        return True
        # print "result from update",result["acknowledged"]

    def getTotalCount(self, parkingLot):
        record = database.totalAvailable.find_one({"id":parkingLot})
        return record

    def getAllParkingData(self):
        records = database.totalAvailable.find()
        _list = []
        _dict = {}
        for rec in records:
            # print rec
            _list.append(rec)
            # del _dict['_id']
            print "***************",rec["id"]
            id = rec['id']
            _dict[id] = {"total":rec["total"],"occupied":rec["occupied"]}

        # return "oooooo"
        print _dict
        return jsonify( _dict)






