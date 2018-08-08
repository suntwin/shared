import argparse
import sys
import config as cfg
from resources import Res
from connection import Connection

try:
	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		parser.add_argument("-profile","-p",help="Mandatory parameter mention a profile for adding credentials")
		parser.add_argument("--tag","-t",help="optional parameter which when passed with tag only information, retrieves the resources")
		parser.add_argument("--value","-v",help="optional parameter which when passed with tag only information, retrieves the resources")


		args = parser.parse_args()
		region_name = cfg.settings['region_name']
		profile_name = args.profile

		
		# get session
		conn = Connection(region_name,profile_name)
		
		# get service
		ec2 = conn.get_aws_service('ec2')

		# get resource access 
		res = Res(ec2)


	# if the script runs without any argument, it means get all the instances with notags
		
		if(args.tag ==None and args.value==None):
			res_list = res.get_ec2_resources_on_taginfo(taginfo="notag")
			print(res_list)
	# if the script runs with only tag key and no value
		if(args.tag and args.value==None):
			#print("inside args tag",args.tag)
			res_list = res.get_ec2_resources_on_taginfo(tagonly=args.tag)
			print(res_list)
	# if the script runs with both tag key and  value
		if(args.tag and args.value):
			#print("inside args tag",args.tag)
			res_list = res.get_ec2_resources_on_taginfo(key=args.tag,value=args.value)
			print(res_list)
except Exception as e:
	print(e.message)















