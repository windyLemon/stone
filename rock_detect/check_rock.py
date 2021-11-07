import torch as t
from rock_detect.utils.util import read_image
from torchvision import transforms as tvtsf
from rock_detect.utils.array_tool import tonumpy,totensor
from rock_detect.backbone import Backbone
from torch.nn import functional as F
from threading import Timer
import socket
import schedule


class NetOutput:
    def __init__(self, use_cuda=False, net_arch='densenet121'):
        net_save_url = {'vgg16': '/Users/jhchen/PycharmProjects/stones/rock_detect/checkpoints/vgg16',
                        'resnet50': '/Users/jhchen/PycharmProjects/stones/rock_detect/checkpoints/resnet50',
                        'densenet121': '/Users/jhchen/PycharmProjects/stones/rock_detect/checkpoints/densetnet(2).pth'}

        self.model = Backbone(net_arch=net_arch)
        self.use_cuda = use_cuda
        if self.use_cuda == True:
            state_dict = t.load(net_save_url[net_arch])
            self.model.load_state_dict(state_dict['model'])
            self.model.cuda()
        else:
            state_dict = t.load(net_save_url[net_arch], map_location=t.device('cpu'))
            self.model.load_state_dict(state_dict['model'])
        self.model.eval()

    def check_rock_dist(self, img_url):
        img = read_image(img_url, color=True)
        img = img / 255.
        normalize = tvtsf.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
        img = normalize(t.from_numpy(img))
        img = t.unsqueeze(img, 0)
        if self.use_cuda == True:
            img = img.cuda()
        score = list(tonumpy(F.softmax(self.model(img), dim=1))[0])
        return score











