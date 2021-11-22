from PIL import Image
import numpy as np
import os

class Merge_Input_target():
    def __init__(self, root_dir_input, root_dir_target): # root_dir_input equivalent to day  root_dir_target equivalent to day
        self.root_dir_input = root_dir_input
        self.root_dir_target = root_dir_target
        self.list_inputs = os.listdir(self.root_dir_input)
        self.list_targets = os.listdir(self.root_dir_target)

    def __len__(self):
        return len(self.list_inputs)

    def merge(self, index):
        img_input = self.list_inputs[index]
        img_target = self.list_targets[index]
        img_input_path = os.path.join(self.root_dir_input, img_input)
        img_target_path = os.path.join(self.root_dir_target, img_target)
        image_input_array = np.array(Image.open(img_input_path))
        image_target_array = np.array(Image.open(img_target_path))
        image = np.concatenate((image_input_array, image_target_array), axis=0)
        return image


if __name__ == "__main__":
    dataset = Merge_Input_target("data/train/", "data/train/")
    for x, in zip()