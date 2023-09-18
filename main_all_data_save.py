# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:04:55 2023

@author: hp
"""

import pygame
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2
import pickle
import atexit
from datetime import datetime
import os
# from pykinect2 import PyKinectV2
# from pykinect2.PyKinectV2 import *
# from pykinect2 import PyKinectRuntime

import ctypes
import _ctypes
import pygame
import sys

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

from basic_info import main
import threading

# from PyKinectBodyGame_savedata import BodyGameRuntime
ID = main()



# PATH = 'F:\final thesis\kinect real time v2\kinect real time'

# make_new_path = os.path.join(PATH, ID)
if not os.path.exists(ID):
    os.makedirs(ID)
    
    
    
kinectC = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)
depth_frames = []
# set the path to where you want the files to be stored
# now it just defaults to where the program is stored
def all_done():
    #filename = 'Kinect_Depth'
    filename = ID+'/Kinect_Depth'
    outfile = open(filename, 'wb')
    pickle.dump(depth_frames, outfile)
# set the path to where you want the files to be stored
writerC = cv2.VideoWriter(ID+'/Kinect_Color.mp4', cv2.VideoWriter_fourcc(*'XVID'),25, (1920, 1080))

class BodyGameRuntime(object):
    def __init__(self, target_time:str):  #sample targe_time format = '06:01:00' (hour:minute:second)
        pygame.init()
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
        self._bodies = None
        self.target_time = target_time
    def run(self):
        joints_list=[]

        loop_controller = True
        while loop_controller:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if current_time == self.target_time:
                print("Your Requrested Target Time =", current_time, "is reached")
                loop_controller = False

        while True:
            if self._kinect.has_new_body_frame(): 
                self._bodies = self._kinect.get_last_body_frame()
            if kinectC.has_new_color_frame():
                if self._bodies is not None: 
                    frameC = kinectC.get_last_color_frame()
                    frameC = np.reshape(frameC, (1080, 1920, 4))
                    frameCR = cv2.cvtColor(frameC, cv2.COLOR_RGBA2RGB)
                    frameC = cv2.resize(frameCR, (0, 0), fx=0.5, fy=0.5)
                    #video file writer
                    writerC.write(frameCR)
            
                    frameDR = kinect.get_last_depth_frame()
                    frameD = np.reshape(frameDR, (424, 512))
                    frameD = frameD.astype(np.uint8)
                    frameD = np.reshape(frameD, (424, 512))
                    #depth frame file writer
                    depth_frames.append(frameDR)

                    for i in range(0, self._kinect.max_body_count):
                        body = self._bodies.bodies[i]
                        if not body.is_tracked: 
                            continue 
                        
                        joints = body.joints 
                        # convert joint coordinates to color space 
                        ####################
                        joint_list=[]
                        for j in range(0, PyKinectV2.JointType_Count):
                            #print(j.Position.x)
                            joint_list.append(joints[j].Position.x)
                            joint_list.append(joints[j].Position.y)
                            joint_list.append(joints[j].Position.z)
                        joints_list.append(joint_list)
                    np.savetxt(ID+"/data_skeleton.csv", joints_list, delimiter=",")
                cv2.imshow('frameC', frameC)
                cv2.imshow('farmeD', frameD)
            
                frame = None
        
            key = cv2.waitKey(1)
            if key == 27: break
        atexit.register(all_done)

        
__main__ = "Kinect v2 Body Game"
target_time = input("Set the target time: ")
game = BodyGameRuntime(target_time);

# t1 = threading.Thread(target=game.run)
# t2 = threading.Thread(target=game.run)

# t1.start()
# t2.start()
game.run();
