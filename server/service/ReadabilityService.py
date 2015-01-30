

class ReadabilityService(object):

    def readability(self, req):
        stringlength = len(req["reqData"])
        wc = self.wordcount(req["reqData"])
        response = { "resultCode":0, "docScore":0, "characterCount": stringlength,
                     "wordCount": wc, "lineScores": [{"lineNo":0, "lineTxt":"one", "lineScore":42}]}
        return response

    def version(self):
        return "0.0.1"

    def wordcount(self, str):
        return len(str.split())
        
