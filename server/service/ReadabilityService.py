

class ReadabilityService(object):

    def readability(self, req):
        stringlength = len(req["reqData"])
        response = { "resultCode":0, "docScore":0, "lineScores": [{"lineNo":0, "lineTxt":"one", "lineScore":42}]}
        return response
