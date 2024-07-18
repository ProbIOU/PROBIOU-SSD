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
- conda create --name probiou-ssd python=3.6
- conda activate probiou-ssd
- pip install -r requirements.txt

## Datasets
- PASCAL VOC:Download VOC2007, VOC2012 dataset, then put VOCdevkit in the data directory or run get_voc_dataset.sh in data folder


## Training

### Training VOC
```Shell
python tools/train.py --loss <loss_type> --work_name <save_path>
```

Also yo can activate python -m visdom.server in an additional tmux window to track the losses.

## Evaluation
- To evaluate a trained network:

```Shell
python tools/ap.py --trained_model {your_weight_address} --ProbIoU [True/False]
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


## Cite our work


```
@article{Murrugarra_Llerena_2024,
   title={Probabilistic Intersection-Over-Union for Training and Evaluation of Oriented Object Detectors},
   volume={33},
   ISSN={1941-0042},
   url={http://dx.doi.org/10.1109/TIP.2023.3348697},
   DOI={10.1109/tip.2023.3348697},
   journal={IEEE Transactions on Image Processing},
   publisher={Institute of Electrical and Electronics Engineers (IEEE)},
   author={Murrugarra-Llerena, Jeffri and Kirsten, Lucas N. and Zeni, Luis Felipe and Jung, Claudio R.},
   year={2024},
   pages={671–681} }
```

## FOR QUESTION

email me at: jeffri.mllerena@inf.ufrgs.br
