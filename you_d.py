#!/data/data/com.termux/files/usr/bin/python3
#Made by prince kumar 
#Date 13 jun 2021
#All import goes here
import time 
import random
import argparse
from pytube import YouTube
#Make a function for Progress
def progBar():
    print("\033[31;1m ■", end=" ")
#Make a function for complete 
def comDown():
    print("\033[36;1m Downloding complete")
#Now add arguments
parser = argparse.ArgumentParser()
parser.add_argument("u" , type=str ,help="Enter Video url")
parser.add_argument("--v" , type=str ,help="Type --v v for downloding videos")
parser.add_argument("--a" , type=str ,help="Type --a a for downloding Audio")
parser.add_argument("--t" , type=str ,help="Type --t t for thumbnail url ")
args = parser.parse_args()
    
#Print title of the video 
try:
    yt = YouTube(args.u,on_progress_callback=progBar())
    print("")
    print(yt.title)
except VideoUnavailable:
    print("\033[35;1m Provide video url")
except KeyboardInterrupt:
    print("\033[33;1m Exiting Tool")
#Make a function for download video 
def downVideo():
    dv = yt.streams.get_by_itag('22')
    dv.download("/storage/emulated/0/")
    comDown()
    print("\033[34;1m Video file saved into internal storage")
#Make a function for downloading audio..
def downAudio():
    da = yt.streams.get_by_itag('140')
    da.download("/storage/emulated/0/Audio")
    comDown()
    print("\033[34;1m Audio file saved into Audio folder")

#Now process the user demand ----------
if ( args.v == "v" or args.v == "V" ):
    print("\033[0;1m Starting download...")
    downVideo()
else:
    pass
if (args.a == "a" or args.a == "A" ):
    print("\033[0;1m Starting downloading audio...")
    downAudio()
else:
    pass
if (args.t == "t" or args.t == "T" ):
    print("\033[34;1m Genarating Thumbnail url..")
    print()
    print(yt.thumbnail_url)
else :
    print(" Type -h or --help for uses..")






