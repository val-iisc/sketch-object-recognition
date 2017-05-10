We fine-tuned the Sketch-CNN(sketch-a-net) multi-scale model for 160 class. 

Files involved:

-> Multi-scale(scales of 256, 224, 192, 128, 64) Sketch-CNN weights in mat file:

    -> net_u_256_57p3.mat 
    
    -> net_u_224_57p3.mat 
    
    -> net_u_192_57p3.mat
    
    -> net_u_128_57p3.mat 
    
    -> net_u_64_57p3.mat

The .mat files can be downloaded from [here](https://drive.google.com/folderview?id=0B-uAVJ5bK78SRUhydFBlU214Y28&usp=sharing)
    
-> Sketch-CNN model in lasagne and functions to get Multiscale(5*512) feature is given in sketchcnn_theano.py
