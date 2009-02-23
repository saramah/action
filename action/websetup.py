"""Setup the action application"""
import logging

from paste.deploy import appconfig
from pylons import config

from action.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_config(command, filename, section, vars):
    """Place any commands to setup action here"""
    conf = appconfig('config:' + filename)
    load_environment(conf.global_conf, conf.local_conf)

    #populate the db on 'paster setup-app'
    import action.model as model

    log.info("Setting up database connectivity...")
    engine = config['pylons.g'].sa_engine
    log.info("Creating tables...")
    model.metadata.create_all(bind=engine)
    log.info("Beginning the database session...")
    model.Session.begin()
    log.info("Success!")
