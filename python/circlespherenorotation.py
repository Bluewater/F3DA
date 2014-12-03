'''
circlespherenorotation
Points for the ground track
on a non-rotating sphere
of a satellite in a circular orbit
'''

import sys #arguments
import math #trigonometric functions

PARAM_STARTINGLONG = 'startinglongitudedegrees'
PARAM_TIMET = 'time_t'

ORDERED_PARAMETERS = [None, PARAM_TIMET, PARAM_STARTINGLONG]
PERIOD_DAYS = 0.5

def getlongitude(timedays,offsetdegrees,perioddays):
    '''return the longitude in degrees
    of an eastward-orbiting satellite
    in an orbit with inclination 0
    and specified period'''
    timedays = float(timedays)
    offsetdegrees = float(offsetdegrees)
    degreesperday = 360/perioddays
    longitudedegrees = timedays * degreesperday + offsetdegrees
    return longitudedegrees

def getparameters(args, ordered_parameters):
    '''return a dict of parameters'''
    paramdict = {}
    for i in range(0,min(len(args),len(ordered_parameters))):
        parameter = ordered_parameters[i]
        value = args[i]
        if not parameter==None:
            paramdict[parameter]=value
        pass
    return paramdict

def main(args):
    '''core logic'''
    msg(args)
    paramdict = getparameters(args, ORDERED_PARAMETERS)
    msg(paramdict)
    longitudedegrees = getlongitude(paramdict[PARAM_TIMET],paramdict[PARAM_STARTINGLONG],PERIOD_DAYS)
    msg(longitudedegrees)
    return None

def msg(msgin):
    print str(msgin)
    return None

if __name__ == '__main__':
    main(sys.argv)
