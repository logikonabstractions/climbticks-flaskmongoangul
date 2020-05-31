""" Entry point for REST api using Flask """

# basic python imports
import os
import sys
import requests
from logger import logger

# flask-specific imports
from flask import  jsonify, request, make_response, send_from_directory
from app import app

"""First, setting up some basic elements. Those could probably be moved to some init/config file eventually .

    We first find the path to the root of our repository, which is just the index.py location. **This assumes that the index.py lives at the root of the directory**. We then add it to the environemnet variable. 
"""

ROOTH_PATH = os.path.dirname(os.path.relpath(__file__))
os.environ.update({'ROOTH_PATH':ROOTH_PATH})
sys.path.append(os.path.join(ROOTH_PATH, 'modules'))

"""Setup logging. Again could probably be done in some submethod or something.

    I should re-check the Dekko logging structure & recover some of that setup as it was pretty sweet. Since it is short & sweet, let's just mention we're also definining a PORT variable on which the app will listen.
"""

log_file = os.path.join(ROOTH_PATH, 'logfile.log')
LOG = logger.get_root_logger(os.environ.get('ROOT_LOGGER', 'root'), filename=log_file)

PORT = os.environ.get('PORT')



@app.errorhandler(404)
def not_found(error):
    """ Basic error handling """
    LOG.error(error)
    return make_response(jsonify({'error':'Not found'}), 404)

@app.route('/')
def index():
    """ Static index file """
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    """ static folder serve """
    file_name = path.split('/')[-1]
    dir_name = os.path.join('dist','/'.join(path.split('/')[:-1]))
    return send_from_directory(dir_name, file_name)

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    LOG.info(f'Hello! Running env:{os.environ.get("ENV")}')
    app.config['DEBUG'] = os.environ.get('ENV') == "development"
    app.run(host="0.0.0.0", port=int(PORT))