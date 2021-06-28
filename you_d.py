#!/data/data/com.termux/files/usr/bin/python3
#Made by prince kumar 
#Date 13 jun 2021
#All import goes here
import time 
import random
import os 
from pytube.cli import on_progress
import argparse
from pytube import YouTube
#Make a function for Progress
#Make a function to update ...
def repoUpdate():
    os.system("git pull https://github.com/princekrvert/YOU_D.git > /dev/null 2>&1 & sleep 0.5 ")
    print("\033[35;1m Updating.....")
    os.system("clear")
repoUpdate()
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
    yt = YouTube(args.u,on_progress_callback=on_progress)
    print("")
    print(yt.title)
except VideoUnavailable:
    print("\033[35;1m Provide video url")
except KeyboardInterrupt:
    print("\033[33;1m Exiting Tool")
#Make a function for download video 
def downVideo(vtag):
    dv = yt.streams.get_by_itag(vtag)
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
    print("\033[0;1m Video quality...")
    print()
    print("\033[32;1m [01] \033[36;1m 1080p")
    print("\033[32;1m [02] \033[36;1m 720p")
    print("\033[32;1m [03] \033[36;1m 360p")
    v_q = input("\033[37;1m :: ")
    if ( v_q == "01" or v_q == "1"):
        downVideo(137)
    elif ( v_q == "02" or v_q == "2"):
        downVideo(22)
    elif ( v_q == "03" or v_q == "3"):
        downVideo(18)
    else:
        print("\033[31;1m Invalid option...")
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






