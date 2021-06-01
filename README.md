## ProbIOU Loss 

Base code [here](https://github.com/Zzh-tju/DIoU-SSD-pytorch)

### Losses

Losses can be chosen with the `--losstype` option in the arguments in train.py file. The valid options are currently: `[Iou|Giou|Diou|Ciou|SmoothL1|Piou]`.


## Fold-Structure
The fold structure as follow:
- config/
	- config.py
	- __init__.py
- data/
	- __init__.py
 	- VOC.py
	- VOCdevkit/
- model/
	- build_ssd.py
	- __init__.py
	- backbone/
	- neck/
	- head/
	- utils/
- utils/
	- box/
	- detection/
	- loss/
	- __init__.py
- tools/
	- train.py
	- eval.py
	- test.py
- work_dir/
	

## Environment
- pytorch 0.4.1
- python3+
- visdom 
	- for real-time loss visualization during training!
	```Shell
	pip install visdom
	```
	- Start the server (probably in a screen or tmux)
	```Shell
	python visdom
	```
  * Then (during training) navigate to http://localhost:8097/ (see the Train section below for training details).


## Datasets
- PASCAL VOC:Download VOC2007, VOC2012 dataset, then put VOCdevkit in the data directory


## Training

### Training VOC
- The pretrained model refer [pretrained-models.pytorch](https://github.com/Cadene/pretrained-models.pytorch),you can download it.

- In the DIoU-SSD-pytorch fold:
```Shell
python tools/train.py
```

- Note:
  * For training, default NVIDIA GPU.
  * You can set the parameters in the train.py (see 'tools/train.py` for options) 
  * In the config,you can set the work_dir to save your training weight.(see 'configs/config.py`) 

## Evaluation
- To evaluate a trained network:

```Shell
python tools/ap.py --trained_model {your_weight_address}
```

For example: (the output is AP50, AP75 and AP of our CIoU loss)
```
Results:
0.033
0.015
0.009
0.011
0.008
0.083
0.044
0.042
0.004
0.014
0.026
0.034
0.010
0.006
0.009
0.006
0.009
0.013
0.106
0.011
0.025
~~~~~~~~

--------------------------------------------------------------
Results computed with the **unofficial** Python eval code.
Results should be very close to the official MATLAB eval code.
--------------------------------------------------------------
0.7884902583981603 0.5615516772893671 0.5143832356646468
```

## Test
- To test a trained network:

```Shell
python test.py -- trained_model {your_weight_address}
```
if you want to visual the box, you can add the command --visbox True(default False)
