#!/usr/bin/python
import itertools

def distance(p):
	return ((p[0][0]-p[1][0])**2+(p[0][1]-p[1][1])**2)**0.5

def dis_list(point_list):
	#this function take the full point list and return the distance between 	# all pair of points
	s = itertools.combinations(point_list, 2)
	distance_list = [distance(i) for i in list(s)]
	return distance_list

def sp_dislist(dis_list,len_pointlist):
	#this will take distance list as input and split it into more lists
	while 
	a = [dis_list[i] for i in len_pointlist-1] 
	
