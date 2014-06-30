class ReadabilityService(object):

    def readability(self, req):
        stringlength = len(req["text"])
        response = { "length":"%s" %(stringlength)}
        return response
