import numpy as np
from scipy.io import loadmat
import lasagne
from lasagne.layers import *
from theano import tensor as T
import theano
import math

# Set hte directory path
dir = '/data1/jogendra/eotd2/'

def build_theanocnn(net_path):
	dnet = loadmat(net_path)
	input_var = T.tensor4('inputs')
	l_in = InputLayer(shape=(None, 1, 256, 256), input_var=input_var)
	############# sketchcnn starts here.
	l_conv1 = Conv2DLayer(l_in, 64, (15,15), stride=(3,3), W=np.rollaxis(np.rollaxis(dnet['n1'][0,0]['filters'],-2),-1), b=dnet['n1'][0,0]['biases'].ravel(), flip_filters=False)
	l_mp1 = MaxPool2DLayer(l_conv1, 3, stride=2)  # see border
	l_conv2 = Conv2DLayer(l_mp1, 128, (5,5), stride=(1,1), W=np.rollaxis(np.rollaxis(dnet['n4'][0,0]['filters'],-2),-1), b=dnet['n4'][0,0]['biases'].ravel(), flip_filters=False) 
	l_mp2 = MaxPool2DLayer(l_conv2, 3, stride=2)
	l_conv3 = Conv2DLayer(l_mp2, 256, (3,3), stride=(1,1), pad=1, W=np.rollaxis(np.rollaxis(dnet['n7'][0,0]['filters'],-2),-1), b=dnet['n7'][0,0]['biases'].ravel(), flip_filters=False) 
	l_conv4 = Conv2DLayer(l_conv3, 256, (3,3), stride=(1,1), pad=1, W=np.rollaxis(np.rollaxis(dnet['n9'][0,0]['filters'],-2),-1), b=dnet['n9'][0,0]['biases'].ravel(), flip_filters=False)  
	l_conv5 = Conv2DLayer(l_conv4, 256, (3,3), stride=(1,1), pad=1, W=np.rollaxis(np.rollaxis(dnet['n11'][0,0]['filters'],-2),-1), b=dnet['n11'][0,0]['biases'].ravel(), flip_filters=False)  
	l_mp3 = MaxPool2DLayer(l_conv5, 3, stride=2)
	############ conv layer ends here.
	l_conv6 = Conv2DLayer(l_mp3, 512, (7,7), stride=(1,1), W=np.rollaxis(np.rollaxis(dnet['n14'][0,0]['filters'],-2),-1), b=dnet['n14'][0,0]['biases'].ravel(), flip_filters=False)  
	# droupout
	l_conv7 = Conv2DLayer(l_conv6, 512, (1,1), stride=(1,1), W=np.rollaxis(np.rollaxis(dnet['n17'][0,0]['filters'],-2),-1), b=dnet['n17'][0,0]['biases'].ravel(), flip_filters=False) 
	out_fea = lasagne.layers.get_output(l_conv7).mean(axis=3).mean(axis=2)
	val_fn = theano.function([input_var], out_fea)
	return val_fn

fea_fun1 = build_theanocnn('%sSketch_RNN/sketchcnn_tf/net_u_256_57p3.mat'%(dir))
fea_fun2 = build_theanocnn('%sSketch_RNN/sketchcnn_tf/net_u_224_57p3.mat'%(dir))
fea_fun3 = build_theanocnn('%sSketch_RNN/sketchcnn_tf/net_u_192_57p3.mat'%(dir))
fea_fun4 = build_theanocnn('%sSketch_RNN/sketchcnn_tf/net_u_128_57p3.mat'%(dir))
fea_fun5 = build_theanocnn('%sSketch_RNN/sketchcnn_tf/net_u_64_57p3.mat'%(dir))

def get_feature(b_img1, b_img2, b_img3, b_img4, b_img5, b_size, seql, fea_size):
	max_bs = 1000.0
	init_i = 0
	
	len = b_size*seql
	var1 = np.zeros([len,fea_size], dtype=np.dtype('<f'))
	for i in range(int(math.ceil(len/max_bs))):
		end_i = init_i + max_bs
		if end_i > len:
			var1[init_i:,:] = np.concatenate((fea_fun1(b_img1[init_i:,:,:,:]), fea_fun2(b_img2[init_i:,:,:,:]), 
			fea_fun3(b_img3[init_i:,:,:,:]), fea_fun4(b_img4[init_i:,:,:,:]), fea_fun5(b_img5[init_i:,:,:,:])), axis=1)
		else:
			var1[init_i:end_i,:] = np.concatenate((fea_fun1(b_img1[init_i:end_i,:,:,:]), fea_fun2(b_img2[init_i:end_i,:,:,:]), 
			fea_fun3(b_img3[init_i:end_i,:,:,:]), fea_fun4(b_img4[init_i:end_i,:,:,:]), fea_fun5(b_img5[init_i:end_i,:,:,:])), axis=1)
		
		init_i = end_i
	
	var2 = np.reshape(var1 ,(b_size, seql, fea_size))
	return var2
	


	
