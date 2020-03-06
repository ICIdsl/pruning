import torch
import torch.nn as nn
import torch.nn.functional as F

class MobileNetV2(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 27, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.bn1 = nn.BatchNorm2d(27, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_conv1 = nn.Conv2d(27, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_bn1 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_conv2 = nn.Conv2d(18, 18, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=18, bias=False)
        self.layers_0_bn2 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_conv3 = nn.Conv2d(18, 15, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_bn3 = nn.BatchNorm2d(15, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_shortcut_0 = nn.Conv2d(27, 15, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_shortcut_1 = nn.BatchNorm2d(15, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv1 = nn.Conv2d(15, 50, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn1 = nn.BatchNorm2d(50, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv2 = nn.Conv2d(50, 50, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=50, bias=False)
        self.layers_1_bn2 = nn.BatchNorm2d(50, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv3 = nn.Conv2d(50, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_shortcut_0 = nn.Conv2d(15, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_shortcut_1 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv1 = nn.Conv2d(16, 68, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn1 = nn.BatchNorm2d(68, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv2 = nn.Conv2d(68, 68, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=68, bias=False)
        self.layers_2_bn2 = nn.BatchNorm2d(68, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv3 = nn.Conv2d(68, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv1 = nn.Conv2d(16, 117, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn1 = nn.BatchNorm2d(117, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv2 = nn.Conv2d(117, 117, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=117, bias=False)
        self.layers_3_bn2 = nn.BatchNorm2d(117, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv3 = nn.Conv2d(117, 28, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn3 = nn.BatchNorm2d(28, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv1 = nn.Conv2d(28, 102, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn1 = nn.BatchNorm2d(102, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv2 = nn.Conv2d(102, 102, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=102, bias=False)
        self.layers_4_bn2 = nn.BatchNorm2d(102, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv3 = nn.Conv2d(102, 28, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn3 = nn.BatchNorm2d(28, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv1 = nn.Conv2d(28, 112, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn1 = nn.BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv2 = nn.Conv2d(112, 112, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=112, bias=False)
        self.layers_5_bn2 = nn.BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv3 = nn.Conv2d(112, 28, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn3 = nn.BatchNorm2d(28, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv1 = nn.Conv2d(28, 130, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn1 = nn.BatchNorm2d(130, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv2 = nn.Conv2d(130, 130, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=130, bias=False)
        self.layers_6_bn2 = nn.BatchNorm2d(130, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv3 = nn.Conv2d(130, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv1 = nn.Conv2d(13, 200, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn1 = nn.BatchNorm2d(200, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv2 = nn.Conv2d(200, 200, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=200, bias=False)
        self.layers_7_bn2 = nn.BatchNorm2d(200, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv3 = nn.Conv2d(200, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv1 = nn.Conv2d(13, 178, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn1 = nn.BatchNorm2d(178, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv2 = nn.Conv2d(178, 178, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=178, bias=False)
        self.layers_8_bn2 = nn.BatchNorm2d(178, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv3 = nn.Conv2d(178, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv1 = nn.Conv2d(13, 141, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn1 = nn.BatchNorm2d(141, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv2 = nn.Conv2d(141, 141, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=141, bias=False)
        self.layers_9_bn2 = nn.BatchNorm2d(141, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv3 = nn.Conv2d(141, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv1 = nn.Conv2d(13, 204, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn1 = nn.BatchNorm2d(204, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv2 = nn.Conv2d(204, 204, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=204, bias=False)
        self.layers_10_bn2 = nn.BatchNorm2d(204, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv3 = nn.Conv2d(204, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn3 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_shortcut_0 = nn.Conv2d(13, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_shortcut_1 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv1 = nn.Conv2d(26, 217, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn1 = nn.BatchNorm2d(217, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv2 = nn.Conv2d(217, 217, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=217, bias=False)
        self.layers_11_bn2 = nn.BatchNorm2d(217, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv3 = nn.Conv2d(217, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn3 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv1 = nn.Conv2d(26, 225, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn1 = nn.BatchNorm2d(225, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv2 = nn.Conv2d(225, 225, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=225, bias=False)
        self.layers_12_bn2 = nn.BatchNorm2d(225, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv3 = nn.Conv2d(225, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn3 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv1 = nn.Conv2d(26, 239, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn1 = nn.BatchNorm2d(239, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv2 = nn.Conv2d(239, 239, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=239, bias=False)
        self.layers_13_bn2 = nn.BatchNorm2d(239, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv3 = nn.Conv2d(239, 36, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn3 = nn.BatchNorm2d(36, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv1 = nn.Conv2d(36, 451, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn1 = nn.BatchNorm2d(451, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv2 = nn.Conv2d(451, 451, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=451, bias=False)
        self.layers_14_bn2 = nn.BatchNorm2d(451, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv3 = nn.Conv2d(451, 36, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn3 = nn.BatchNorm2d(36, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv1 = nn.Conv2d(36, 324, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn1 = nn.BatchNorm2d(324, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv2 = nn.Conv2d(324, 324, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=324, bias=False)
        self.layers_15_bn2 = nn.BatchNorm2d(324, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv3 = nn.Conv2d(324, 36, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn3 = nn.BatchNorm2d(36, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv1 = nn.Conv2d(36, 283, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn1 = nn.BatchNorm2d(283, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv2 = nn.Conv2d(283, 283, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=283, bias=False)
        self.layers_16_bn2 = nn.BatchNorm2d(283, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv3 = nn.Conv2d(283, 119, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn3 = nn.BatchNorm2d(119, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_shortcut_0 = nn.Conv2d(36, 119, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_shortcut_1 = nn.BatchNorm2d(119, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv2 = nn.Conv2d(119, 861, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.bn2 = nn.BatchNorm2d(861, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.avgpool = nn.AvgPool2d(kernel_size=4, stride=4, padding=0)
        self.linear = nn.Linear(in_features=861, out_features=100, bias=True)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = F.relu(x)
        x_main = x
        x_main = self.layers_0_conv1(x_main)
        x_main = self.layers_0_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_0_conv2(x_main)
        x_main = self.layers_0_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_0_conv3(x_main)
        x_main = self.layers_0_bn3(x_main)
        x_residual = x
        x_residual = self.layers_0_shortcut_0(x_residual)
        x_residual = self.layers_0_shortcut_1(x_residual)
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_1_conv1(x_main)
        x_main = self.layers_1_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_1_conv2(x_main)
        x_main = self.layers_1_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_1_conv3(x_main)
        x_main = self.layers_1_bn3(x_main)
        x_residual = x
        x_residual = self.layers_1_shortcut_0(x_residual)
        x_residual = self.layers_1_shortcut_1(x_residual)
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_2_conv1(x_main)
        x_main = self.layers_2_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_2_conv2(x_main)
        x_main = self.layers_2_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_2_conv3(x_main)
        x_main = self.layers_2_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x = self.layers_3_conv1(x)
        x = self.layers_3_bn1(x)
        x = F.relu(x)
        x = self.layers_3_conv2(x)
        x = self.layers_3_bn2(x)
        x = F.relu(x)
        x = self.layers_3_conv3(x)
        x = self.layers_3_bn3(x)
        x_main = x
        x_main = self.layers_4_conv1(x_main)
        x_main = self.layers_4_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_4_conv2(x_main)
        x_main = self.layers_4_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_4_conv3(x_main)
        x_main = self.layers_4_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_5_conv1(x_main)
        x_main = self.layers_5_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_5_conv2(x_main)
        x_main = self.layers_5_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_5_conv3(x_main)
        x_main = self.layers_5_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x = self.layers_6_conv1(x)
        x = self.layers_6_bn1(x)
        x = F.relu(x)
        x = self.layers_6_conv2(x)
        x = self.layers_6_bn2(x)
        x = F.relu(x)
        x = self.layers_6_conv3(x)
        x = self.layers_6_bn3(x)
        x_main = x
        x_main = self.layers_7_conv1(x_main)
        x_main = self.layers_7_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_7_conv2(x_main)
        x_main = self.layers_7_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_7_conv3(x_main)
        x_main = self.layers_7_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_8_conv1(x_main)
        x_main = self.layers_8_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_8_conv2(x_main)
        x_main = self.layers_8_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_8_conv3(x_main)
        x_main = self.layers_8_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_9_conv1(x_main)
        x_main = self.layers_9_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_9_conv2(x_main)
        x_main = self.layers_9_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_9_conv3(x_main)
        x_main = self.layers_9_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_10_conv1(x_main)
        x_main = self.layers_10_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_10_conv2(x_main)
        x_main = self.layers_10_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_10_conv3(x_main)
        x_main = self.layers_10_bn3(x_main)
        x_residual = x
        x_residual = self.layers_10_shortcut_0(x_residual)
        x_residual = self.layers_10_shortcut_1(x_residual)
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_11_conv1(x_main)
        x_main = self.layers_11_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_11_conv2(x_main)
        x_main = self.layers_11_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_11_conv3(x_main)
        x_main = self.layers_11_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_12_conv1(x_main)
        x_main = self.layers_12_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_12_conv2(x_main)
        x_main = self.layers_12_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_12_conv3(x_main)
        x_main = self.layers_12_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x = self.layers_13_conv1(x)
        x = self.layers_13_bn1(x)
        x = F.relu(x)
        x = self.layers_13_conv2(x)
        x = self.layers_13_bn2(x)
        x = F.relu(x)
        x = self.layers_13_conv3(x)
        x = self.layers_13_bn3(x)
        x_main = x
        x_main = self.layers_14_conv1(x_main)
        x_main = self.layers_14_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_14_conv2(x_main)
        x_main = self.layers_14_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_14_conv3(x_main)
        x_main = self.layers_14_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_15_conv1(x_main)
        x_main = self.layers_15_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_15_conv2(x_main)
        x_main = self.layers_15_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_15_conv3(x_main)
        x_main = self.layers_15_bn3(x_main)
        x_residual = x
        x = x_main + x_residual
        x_main = x
        x_main = self.layers_16_conv1(x_main)
        x_main = self.layers_16_bn1(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_16_conv2(x_main)
        x_main = self.layers_16_bn2(x_main)
        x_main = F.relu(x_main)
        x_main = self.layers_16_conv3(x_main)
        x_main = self.layers_16_bn3(x_main)
        x_residual = x
        x_residual = self.layers_16_shortcut_0(x_residual)
        x_residual = self.layers_16_shortcut_1(x_residual)
        x = x_main + x_residual
        x = self.conv2(x)
        x = self.bn2(x)
        x = F.relu(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.linear(x)
        return x

def mobilenetv2(**kwargs):
    return MobileNetV2(**kwargs)
