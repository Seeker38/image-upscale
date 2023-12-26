## How to use
Run the jupyter notebook file ISR_with_DL, which already use the pretrain model of deep learning.
- The images folder contains the orignal BMP images.
- The source folder contains the Low Resolution Images.
- The output folder contains the comparison between the original, low resolution images and SCRNN images.
- The SCRNN folder contains Deep Learning model.
## Abstract
This is an implementation of SRCNN using keras. You can conduct simple experiments of super resolution on Set5 or your own images.

## SCRNN Model
### Train
run `python train.py`  
Use GPU is recommended for faster runtime. 
There is a pretrained model in './model' or root folder, so you don't have to train model.
### Test
run `python test.py`  
Outputs are restored in './result'. 
If you want to try super resolution to your own images, please put them in './test'.

## References
[https://github.com/YapengTian/SRCNN-Keras](https://github.com/YapengTian/SRCNN-Keras)