'''
simpleorbit
extremely simplified modeling of the ground track of a satellite
'''

def getPeriod():
	period = 1
	return period

def getInclination():
	return None
	
def groundcoord(t):
	return (0,0)

if __name__ == '__main__':
	print str(groundcoord(0))