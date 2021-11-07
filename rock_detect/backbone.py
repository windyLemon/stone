from torchvision.models import vgg16, resnet50, densenet121
import torch.nn as nn


class Backbone(nn.Module):
    def __init__(self,net_arch = 'resnet50'):
        super(Backbone, self).__init__()
        if net_arch == 'vgg16':

            model = vgg16(pretrained=False)

            extractor = list(model.features)
            extractor.append(nn.AdaptiveAvgPool2d(output_size=(7, 7)))

            classifier = model.classifier

            classifier = list(classifier)
            del classifier[6]

            del classifier[5]
            del classifier[2]
            classifier.append(nn.Linear(in_features=4096, out_features=3, bias=True))
        elif net_arch == 'resnet50':
            model = resnet50(pretrained=False)
            extractor = list()

            extra_conv1 = model.conv1
            extractor.append(extra_conv1)
            extra_bn1 = model.bn1
            extractor.append(extra_bn1)
            extra_relu = model.relu
            extractor.append(extra_relu)
            extra_maxpool = model.maxpool
            extractor.append(extra_maxpool)
            extra_layer1 = list(model.layer1)
            extractor += extra_layer1
            extra_layer2 = list(model.layer2)
            extractor += extra_layer2
            extra_layer3 = list(model.layer3)
            extractor += extra_layer3
            extra_layer4 = list(model.layer4)
            extractor += extra_layer4
            extra_avgpool = model.avgpool
            extractor.append(extra_avgpool)
            backbone = resnet50(pretrained=False)

            classifier = list()

            classifier.append(nn.Linear(in_features=2048, out_features=3, bias=True))
        elif net_arch == 'densenet121':
            model = densenet121(pretrained=False)

            extractor = list(model.features)
            extractor.append(nn.AdaptiveAvgPool2d(output_size=(1, 1)))

            classifier = list()

            classifier.append(nn.Linear(in_features=1024, out_features=3, bias=True))



        self.extractor = nn.Sequential(*extractor)
        self.classifier = nn.Sequential(*classifier)


    def forward(self,x):
        feature = self.extractor(x)

        features = feature.view(feature.size(0), -1)

        scores = self.classifier(features)
        return scores





