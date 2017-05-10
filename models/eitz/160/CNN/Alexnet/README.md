We fine-tuned the Alexnet model for sketches. 

Files involved in fine-tuning

-> bvlc_alexnet.caffemodel (ImageNet-trained Alexnet model)

-> solver_sketch_57_43_3.prototxt

-> train_val_sketch_57_43_3.prototxt

To perform fine-tuning, run:

./build/tools/caffe train -solver solver_sketch_57_43_3.prototxt -weights bvlc_alexnet.caffemodel 

We obtained the best validation accuracy at 10500 iterations. The resulting (sketch-recognition) model is caffe_alexnet_train_sketch_57_43_3_iter_10500.caffemodel . The model can be downloaded from [here](https://drive.google.com/file/d/0B-uAVJ5bK78SdXl4UnZtRFF1cmc/view?usp=sharing)

The ImageNet-trained Alexnet model can be downloaded from [here](http://dl.caffe.berkeleyvision.org/bvlc_alexnet.caffemodel)

