#!/usr/bin/env sh
# Create the face_48 lmdb inputs
# N.B. set the path to the face_48 train + val data dirs

EXAMPLE='D:/EclipseWorkspace/caffe_exe'
DATA='D:/EclipseWorkspace/caffe_exe'
TOOLS='D:/caffe/caffe-master/Build/x64/Release'

TRAIN_DATA_ROOT='D:/EclipseWorkspace/caffe_exe/train/'
VAL_DATA_ROOT='D:/EclipseWorkspace/caffe_exe/val/'

# Set RESIZE=true to resize the images to 60 x 60. Leave as false if images have
# already been resized using another tool.
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=227
  RESIZE_WIDTH=227
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_face_48.sh to the path" \
       "where the face_48 training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_face_48.sh to the path" \
       "where the face_48 validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle=true\
    --backend=lmdb\
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    $EXAMPLE/face_train_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    --backend=lmdb\
    $VAL_DATA_ROOT \
    $DATA/val.txt \
    $EXAMPLE/face_val_lmdb

echo "Done."
#Status API Training Shop Blog About

