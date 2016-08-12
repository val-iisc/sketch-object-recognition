### Sketch Object Recognition Using Deep Recurrent Neural Networks


This project contains code and pre-trained sketch recognition models described in our [ACMMM 2016 paper](https://arxiv.org/pdf/1608.03369v1.pdf)


### License

This code is released under the MIT License (Please refer to the LICENSE file for details).

### Citation
Please cite our paper if you happen to use our code and/or models:

If you use these models in your research, please cite:

	@article{RK2015,
		author = {Ravi Kiran Sarvadevabhatla and Jogendra Kundu and Venkatesh Babu R},
		title = {Enabling My Robot To Play Pictionary : Recurrent Neural Networks For Sketch Recognition},
		journal = {arXiv preprint arXiv:1608.03369},
		year = {2016}
	}

### Dependencies and Installation

We provide two kinds of models -- CNN-based and RNN-based. Barring SketchCNN, the CNN-based models are [Caffe](http://caffe.berkeleyvision.org)-based. The RNN-based models have been obtained using the [Lasagne](http://lasagne.readthedocs.io) framework. The code has been tested on Ubuntu 14.04 on the following NVIDIA GPUs: TITAN X, NVIDIA K40, NVIDIA K20. 

To install Caffe, follow the instructions [here](http://caffe.berkeleyvision.org/install_apt.html)

To install Lasagne, follow the instructions [here](http://lasagne.readthedocs.io/en/latest/user/installation.html)
																									     
### Using code and models

Refer to README.txt within the folders for details.

### Q&A

If you have a question or suggestion, please email jogendranathkundu@gmail.com and ravika@gmail.com
