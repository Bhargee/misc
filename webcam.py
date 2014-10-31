import numpy as np
import cv2
import roslib
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class webcam:
    def __init__(self):
        self.pub = rospy.Publisher("image_topic_webcam", Image)
        self.bridge = CvBridge()

    def main(self):
        cap = cv2.VideoCapture('test.mp4')
        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            try:
              self.pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
            except CvBridgeError, e:
              print e
	   
            cv2.imshow('frame', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
               break

        cap.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    wc = webcam()
    rospy.init_node('webcam', anonymous=False)
    wc.main()
    main()
