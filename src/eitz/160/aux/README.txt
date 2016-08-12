train_split_files.txt, val_split_files.txt and test_split_files.txt contain the paths and label ids of augmented sketches used to train validate and test our sketch recognition models

The filepaths correspond to augmented sketch files present at the following location : http://val.serc.iisc.ernet.in/eotd/png-transforms-256x256-250.tar.gz

The provided split files are (almost) in Caffe-compatible format (i.e. can be mentioned in Caffe prototxt for training/testing). However, some of the filepaths contain spaces. Such files cannot be properly processed by Caffe. To circumvent this, create a parallel file with softlinks which point to these files, for e.g.

== train_split_files_softlinks.txt ==
train-1-57-3.png 0
train-2-57-3.png 0
train-3-57-3.png 0

where (running ls -l on each softlink path)

lrwxrwxrwx 1 sketchrec sketchrec 88 May 21 11:13 /home/sketchrec/train-1-57-3.png -> png-transforms-256x256-250/airplane/631.png
lrwxrwxrwx 1 sketchrec sketchrec 88 May 21 11:13 /home/sketchrec/train-1-57-3.png -> png-transforms-256x256-250/airplane/632.png
lrwxrwxrwx 1 sketchrec sketchrec 88 May 21 11:13 /home/sketchrec/train-1-57-3.png -> png-transforms-256x256-250/airplane/633.png

etc.
