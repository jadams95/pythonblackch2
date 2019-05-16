import httplib, sys
from optparse import OptionParser
usageString = "Usage:%prog[options] hostname"
parse = OptionParser(usage=usageString)
parser.add_option("-p", "--port", dest="port", metavar="PORT", default=80, type="int", help="Port to connect to")
(opts,args) = parser.parse_args()
if len(args) < 1:
	parser.error("Hostname is required")

host = arrgs[0]