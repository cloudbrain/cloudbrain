__author__ = 'marion'

from websocket import create_connection
import json
import time

# add the shared settings file to namespace
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
import settings


class SpacebrewRouter(object):
    def __init__(self, server='127.0.0.1', port=9000):
        self.server = server
        self.port = port
        self.ws = create_connection("ws://%s:%s" % (self.server, self.port))

        self.ws.send(json.dumps({"admin": [{"admin": True, "no_msgs": False}]}))

        message = {
            "config": {
                "name": 'router',
                "remoteAddress": self.server
            }
        }

        self.ws.send(json.dumps(message))


    def link(self, pub_metric, sub_metric, publisher, subscriber, sub_ip):
        message = {
            "route": {
                "type": "add",
                "publisher": {
                    "clientName": publisher,
                    "name": pub_metric,
                    "type": "string",
                    "remoteAddress": self.server
                },
                "subscriber": {
                    "clientName": subscriber,
                    "name": sub_metric,
                    "type": "string",
                    "remoteAddress": sub_ip
                }

            }
        }
        self.ws.send(json.dumps(message))
        print json.dumps(message)

    def unlink(self, pub_metric, sub_metric, publisher, subscriber, sub_ip):
        message = {"route":
                       {"type": "remove",
                        "publisher": {
                            "clientName": publisher,
                            "name": pub_metric,
                            "type": "string",
                            "remoteAddress": self.server
                        },
                        "subscriber": {
                            "clientName": subscriber,
                            "name": sub_metric,
                            "type": "string",
                            "remoteAddress": sub_ip
                        }},
                   "targetType": "admin"}

        self.ws.send(json.dumps(message))


if __name__ == "__main__":
    router = SpacebrewRouter(server=settings.CLOUDBRAIN_ADDRESS)
    router.link('eeg', 'muse-001', 'cloudbrain')
    router.link('acc', 'muse-001', 'cloudbrain')
    router.link('concentration', 'muse-001', 'cloudbrain')
    router.link('mellow', 'muse-002', 'cloudbrain')
    time.sleep(1)
    router.unlink("eeg",'muse-001', 'cloudbrain')