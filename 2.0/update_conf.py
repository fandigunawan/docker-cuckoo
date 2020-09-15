#!/usr/bin/env python

import os
import sys
import ConfigParser


#Setting reporting.conf
reporting_cfg = ConfigParser.ConfigParser()
reporting_cfg.read("/cuckoo/conf/reporting.conf")
with open("/cuckoo/conf/reporting.conf", 'w') as cfile:
    if os.environ.get('ES_HOST'):
        reporting_cfg.set('elasticsearch', 'enabled', "yes")
        if os.environ.get('ES_PORT'):
            reporting_cfg.set('elasticsearch', 'hosts', "%s:%s" % (os.environ['ES_HOST'],os.environ['ES_PORT']))
        else:
            reporting_cfg.set('elasticsearch', 'hosts', os.environ['ES_HOST'])

    if os.environ.get('MONGO_HOST'):
        reporting_cfg.set('mongodb', 'enabled', "yes")
        reporting_cfg.set('mongodb', 'host', os.environ['MONGO_HOST'])
    if os.environ.get('MONGO_TCP_PORT'):
        reporting_cfg.set('mongodb', 'port', os.environ['MONGO_TCP_PORT'])

    reporting_cfg.write(cfile)

#Setting cuckoo.conf
cuckoo_cfg = ConfigParser.ConfigParser()
cuckoo_cfg.read("/cuckoo/conf/cuckoo.conf")
with open("/cuckoo/conf/cuckoo.conf", 'w') as cfile:
    if os.environ.get('RESULTSERVER_HOST'):
        cuckoo_cfg.set('resultserver', 'ip', os.environ['RESULTSERVER_HOST'])
    if os.environ.get('RESULTSERVER_PORT'):
        cuckoo_cfg.set('resultserver', 'port', os.environ['RESULTSERVER_PORT'])

    if os.environ.get('MACHINERY'):
        cuckoo_cfg.set('cuckoo', 'machinery', os.environ['MACHINERY'])

    if os.environ.get('DATABASE_CONNECTION'):
        cuckoo_cfg.set('database', 'connection', os.environ['DATABASE_CONNECTION'])

    if os.environ.get('API_TOKEN'):
        cuckoo_cfg.set('cuckoo', 'api_token', os.environ['API_TOKEN'])

    if os.environ.get('WEB_SECRET'):
        cuckoo_cfg.set('cuckoo', 'web_secret', os.environ['WEB_SECRET'])

    cuckoo_cfg.write(cfile)


#Setting processing.conf
processing_cfg = ConfigParser.ConfigParser()
processing_cfg.read("/cuckoo/conf/processing.conf")
with open("/cuckoo/conf/processing.conf", 'w') as cfile:
    if os.environ.get('ALLOWED_DNS'):
        processing_cfg.set('network', 'whitelist_dns', 'yes')
        processing_cfg.set('network','allowed_dns',os.environ['ALLOWED_DNS'])

    if os.environ.get('EXTRACT_DLL'):
        processing_cfg.set('procmemory', 'extract_dll', os.environ['EXTRACT_DLL'])

    if os.environ.get('ENABLE_STRINGS'):
        processing_cfg.set('strings', 'enabled', os.environ['ENABLE_STRINGS'])

    if os.environ.get('ENABLE_SURICATA'):
        processing_cfg.set('suricata', 'enabled', os.environ['ENABLE_SURICATA'])

    processing_cfg.write(cfile)


#Setting auxiliary.conf
auxiliary_cfg = ConfigParser.ConfigParser()
auxiliary_cfg.read("/cuckoo/conf/auxiliary.conf")
with open("/cuckoo/conf/auxiliary.conf", 'w') as cfile:
    if os.environ.get('ENABLE_MITM'):
        auxiliary_cfg.set('mitm', 'enabled', os.environ['ENABLE_MITM'])

    auxiliary_cfg.write(cfile)

xen_cfg = ConfigParser.ConfigParser()
xen_cfg.read("/cuckoo/conf/xenserver.conf")
with open("/cuckoo/conf/xenserver.conf", 'w') as cfile:
    # xen server configuration
    if os.environ.get('XEN_SRVUSERNAME'):
        xen_cfg.set('xenserver', 'user', os.environ['XEN_SRVUSERNAME'])
    
    if os.environ.get('XEN_SRVPASSWORD'):
        xen_cfg.set('xenserver', 'password', os.environ['XEN_SRVPASSWORD'])

    if os.environ.get('XEN_SRVURL'):
        xen_cfg.set('xenserver', 'url', os.environ['XEN_SRVURL'])

    #if os.environ.get('XEN_MACHINES'):
    #    xen_cfg.set('xenserver', 'machines', os.environ['XEN_MACHINES'])

    if os.environ.get('XEN_SRVINTERFACE'):
        xen_cfg.set('xenserver', 'interface', os.environ['XEN_SRVINTERFACE'])

    # VM configuration
    if os.environ.get('XEN_VMUUID'):
        xen_cfg.set('cuckoo1', 'uuid', os.environ['XEN_VMUUID'])

    if os.environ.get('XEN_VMSNAPSHOT'):
        xen_cfg.set('cuckoo1', 'snapshot', os.environ['XEN_VMSNAPSHOT'])

    if os.environ.get('XEN_VMPLATFORM'):
        xen_cfg.set('cuckoo1', 'platform', os.environ['XEN_VMPLATFORM'])
    
    if os.environ.get('XEN_VMIP'):
        xen_cfg.set('cuckoo1', 'ip', os.environ['XEN_VMIP'])

    xen_cfg.write(cfile)

#Setting memory.conf
memory_cfg = ConfigParser.ConfigParser()
memory_cfg.read("/cuckoo/conf/memory.conf")
with open("/cuckoo/conf/memory.conf", 'w') as cfile:
    if os.environ.get('MEM_GUESTPROFILE'):
        memory_cfg.set('basic', 'guest_profile', os.environ['MEM_GUESTPROFILE'])

    memory_cfg.write(cfile)


sys.exit()
