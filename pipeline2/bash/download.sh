#!/bin/bash
# This is our first script.
#/home/ayush/Desktop/pipeline/wgadata
#/home/ayush/Desktop/pipeline/wga_json
curl http://127.0.0.1:5000/pts
cd ~
cd /home/ayush/Desktop/pipeline/new_img


wget https://www.wga.hu/art/a/aken/brothers.jpg 
wget https://www.wga.hu/art/a/aken/vegetab1.jpg 
wget https://www.wga.hu/art/a/alcibar/v_josefa.jpg 
wget https://www.wga.hu/art/a/amigoni/gentlema.jpg 
wget https://www.wga.hu/art/a/amigoni/joseph.jpg
echo "Changing directory....to openpose"
cd ~ 
cd /home/ayush/openpose

echo "Folder changed to openpose"
#ls
 #read -p "Please enter img_dir json_dir: " img_dir json_dir 
echo "now starting the openpose"
echo "It may take some time please wait.................."

./build/examples/openpose/openpose.bin --image_dir /home/ayush/Desktop/pipeline/new_img --write_json /home/ayush/Desktop/pipeline/new_json --model_pose COCO

echo "Finished writing the json files!"


