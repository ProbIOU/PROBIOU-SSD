import os 

losses = ['Piou', 'Ciou', 'Iou', 'Giou', 'Diou', 'SmoothL1']
work_n = ['PIOU', 'CIOU','IOU','GIOU','DIOU', 'SL1']

for i in range(len(losses)):
    os.system('python tools/train.py --loss '+losses[i]+' --work_name SSD300_VOC_FPN_'+work_n[i])
