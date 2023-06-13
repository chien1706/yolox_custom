import copy
import os

import cv2
import numpy as np
from pycocotools.coco import COCO
import sys
sys.path.append("/mnt/nvme0n1/trinhchien/Vincom/YOLOX/yolox/data/")
from dataloading import get_yolox_datadir
from datasets.datasets_wrapper import CacheDataset, cache_read_img


class CARDETECTION(CacheDataset):
    def __init__(self,
        root_dir='/mnt/nvme0n1/trinhchien/Vincom/YOLOX/datasets/dataset-vehicles/',
        # json_file="instances_train2017.json",
        name="train2017",
        img_size=(416, 416),
        preproc=None,
        cache=False,
        cache_type="ram",
        mode = 'train',
    ):
    

