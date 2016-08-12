### Sketch Object Recognition Using Deep Recurrent Neural Networks


This project contains code and pre-trained sketch recognition models described in our [ACMMM 2016 paper](https://arxiv.org/abs/1607.08764)


### License

This code is released under the MIT License (Please refer to the LICENSE file for details).

### Citation
Please cite our paper if you happen to use our code and/or models:
	
		
@article{2016arXiv160708764K,
Author = {Kiran Sarvadevabhatla, Ravi and Surya, Shiv and Kruthiventi, Srinivas.~S and Babu R, Venkatesh}
Title = {SwiDeN : Convolutional Neural Networks For Depiction Invariant Object Recognition},
Journal = {ArXiv e-prints},
eprint = {1607.08764},
Keywords = {Computer Science - Computer Vision and Pattern Recognition},
Year = {2016},
Month = {july},
}

### Dependencies and Installation

We provide two kinds of models -- CNN-based and RNN-based. Barring SketchCNN, the CNN-based models are [Caffe](http://caffe.berkeleyvision.org)-based. The RNN-based models have been obtained using the [Lasagne](http://lasagne.readthedocs.io) framework. The code has been tested on Ubuntu 14.04 on the following NVIDIA GPUs: TITAN X, NVIDIA K40, NVIDIA K20. 

To install Caffe, follow the instructions [here](http://caffe.berkeleyvision.org/install_apt.html)

To install Lasagne, follow the instructions [here](http://lasagne.readthedocs.io/en/latest/user/installation.html)
																												     
### Using code and models

Refer to README.txt within the folders for details.

### Q&A

If you have a question or suggestion, please email jogendranathkundu@gmail.com and ravika@gmail.com
