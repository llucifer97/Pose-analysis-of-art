#!/bin/bash
# This is our first script.
#/home/ayush/Desktop/pipeline/wgadata
#/home/ayush/Desktop/pipeline/wga_json
echo "Changing directory....to openpose"
cd ~ 
cd /home/ayush/openpose

echo "Folder changed to openpose"
ls
 read -p "Please enter img_dir json_dir: " img_dir json_dir 
echo "now starting the openpose"
echo "It may take some time please wait.................."

./build/examples/openpose/openpose.bin --image_dir $img_dir --write_json $json_dir --model_pose COCO

echo "Finished writing the json files!"

cd ~
cd /home/ayush/Desktop/pipeline/
echo "starting jupyter notebook!"
jupyter notebook
