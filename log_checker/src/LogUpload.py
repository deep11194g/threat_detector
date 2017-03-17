from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from RequestLog import RequestLog

class LogUpload(APIView):

	def post(self, request):
		logFile = request.FILES.getlist('logFile')

		if(len(logFile) != 1):
			return Response('Please add only 1 log file. No more no less')

		fileContent = logFile[0].read()
		requestTexts = fileContent.split('\n')

		responseString = 'Probable threat attack logs: <br/><br/>'

		for requestText in requestTexts:
			requestText = requestText.strip()
			
			if(len(requestText) > 1):
				requestLog = RequestLog(requestText)
				requestLog.extractValuesFromLogEntry()

				print requestLog.logFileEntry

				flag = 'Yes, ' if(requestLog.isThreat()) else 'No, '
				print flag	
				responseString += (flag + requestText + "<br/>")

		return Response(responseString)
