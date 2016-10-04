from werkzeug.serving import run_simple

import json
from backend.ATBackend import ATBackendServer

settings = json.load(open('config.json'))


if __name__ == '__main__':
    backend = ATBackendServer(settings['elasticsearch_host'], settings['elasticsearch_index'],
                              settings['elasticsearch_type'],
                              ['cnnmodel_epoch_0.model', ''])
    run_simple(settings['backend_host'], settings['backend_port'], backend.application)
