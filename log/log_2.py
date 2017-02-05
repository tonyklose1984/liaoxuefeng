#coding:utf-8

import logging
FORMAT = '%(asctime)s %(clientip)s %(user)4s %(message)s'
logging.basicConfig(format=FORMAT)
d={'clientip':"192.168.0.1",'user':'tony'}
logging.warning("Protocol problem: %s","connection reset",extra=d)