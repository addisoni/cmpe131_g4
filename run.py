from app import myapp_obj
import os,sys

#Use host/debug args below if port is already taken or additional debug parameters are needed
if __name__ == '__main__':
	myapp_obj.run(debug=True,host='0.0.0.0', port=5000)
	#myapp_obj.run()
	sys.exit(1)

