class RequestLog:

	logFileEntry = ''
	httpMethod = ''
	url = ''
	httpVersion = ''
	originHeader = ''
	sslCipher = ''
	sslProtocol = ''
	datetime = ''
	lbName = ''
	clientIp = ''
	backendIp = ''
	requestProcessingTime = 0.0
	backendProcessingTime = 0.0
	responseProcessingTime = 0.0
	elbStatusCode = ''
	backendStatusCode = ''
	sentBytes = 0
	receivedBytes = 0


	def __init__(self, logFileEntry):
		self.logFileEntry = logFileEntry


	# Use the log entry line to extract values
	def extractValuesFromLogEntry(self):
		tokens = self.logFileEntry.split()

		print tokens

		# Merge consecutive values which are inside quotes
		for i in range(0, len(tokens) - 2):
			if(tokens[i] and tokens[i].startswith('"') and not tokens[i].endswith('"')):
				for j in range(i + 1, len(tokens)):
					tokens[i] += (' ' + tokens[j])
					
					if(tokens[j].endswith('"')):
						tokens[j] = None
						break
					tokens[j] = None

		tokens = [x for x in tokens if x is not None]

		# Make sure there are 17 values in the list for 17 log details
		for i in range(17 - len(tokens)) :
			tokens.append('') 

		print tokens

		# Assign values
		self.httpMethod = tokens[0]
		self.url = tokens[1]
		self.httpVersion = tokens[2]
		self.originHeader = tokens[3]
		self.sslCipher = tokens[4]
		self.sslProtocol = tokens[5]
		self.datetime = tokens[6]
		self.lbName = tokens[7]
		self.clientIp = tokens[8]
		self.backendIp = tokens[9]
		self.requestProcessingTime = tokens[10]
		self.backendProcessingTime = tokens[11]
		self.responseProcessingTime = tokens[12]
		self.elbStatusCode = tokens[13]
		self.backendStatusCode = tokens[14]
		self.sentBytes = tokens[15]
		self.receivedBytes = tokens[16]


	# Aggregate all threat check functions and return a final mandate
	def isThreat(self):
		return self.originHeaderCheck() or self.originIpCheck()

	# Check if origin header is threatening
	def originHeaderCheck(self):
		return (self.originHeader == '"MATLAB R2013a"')

	# Check is origin IP is outside of India or not
	def originIpCheck(self):
		return False
