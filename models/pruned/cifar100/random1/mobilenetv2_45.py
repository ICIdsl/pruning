import torch
import torch.nn as nn
import torch.nn.functional as F

class MobileNetV2(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 27, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.bn1 = nn.BatchNorm2d(27, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_conv1 = nn.Conv2d(27, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_bn1 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_conv2 = nn.Conv2d(17, 17, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=17, bias=False)
        self.layers_0_bn2 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_conv3 = nn.Conv2d(17, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_shortcut_0 = nn.Conv2d(27, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_shortcut_1 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv1 = nn.Conv2d(16, 55, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn1 = nn.BatchNorm2d(55, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv2 = nn.Conv2d(55, 55, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=55, bias=False)
        self.layers_1_bn2 = nn.BatchNorm2d(55, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv3 = nn.Conv2d(55, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn3 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_shortcut_0 = nn.Conv2d(16, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_shortcut_1 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv1 = nn.Conv2d(24, 81, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn1 = nn.BatchNorm2d(81, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv2 = nn.Conv2d(81, 81, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=81, bias=False)
        self.layers_2_bn2 = nn.BatchNorm2d(81, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv3 = nn.Conv2d(81, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn3 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv1 = nn.Conv2d(24, 116, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn1 = nn.BatchNorm2d(116, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv2 = nn.Conv2d(116, 116, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=116, bias=False)
        self.layers_3_bn2 = nn.BatchNorm2d(116, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv3 = nn.Conv2d(116, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv1 = nn.Conv2d(32, 119, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn1 = nn.BatchNorm2d(119, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv2 = nn.Conv2d(119, 119, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=119, bias=False)
        self.layers_4_bn2 = nn.BatchNorm2d(119, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv3 = nn.Conv2d(119, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv1 = nn.Conv2d(32, 127, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn1 = nn.BatchNorm2d(127, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv2 = nn.Conv2d(127, 127, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=127, bias=False)
        self.layers_5_bn2 = nn.BatchNorm2d(127, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv3 = nn.Conv2d(127, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv1 = nn.Conv2d(32, 140, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn1 = nn.BatchNorm2d(140, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv2 = nn.Conv2d(140, 140, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=140, bias=False)
        self.layers_6_bn2 = nn.BatchNorm2d(140, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv3 = nn.Conv2d(140, 63, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn3 = nn.BatchNorm2d(63, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv1 = nn.Conv2d(63, 231, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn1 = nn.BatchNorm2d(231, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv2 = nn.Conv2d(231, 231, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=231, bias=False)
        self.layers_7_bn2 = nn.BatchNorm2d(231, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv3 = nn.Conv2d(231, 63, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn3 = nn.BatchNorm2d(63, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv1 = nn.Conv2d(63, 211, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn1 = nn.BatchNorm2d(211, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv2 = nn.Conv2d(211, 211, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=211, bias=False)
        self.layers_8_bn2 = nn.BatchNorm2d(211, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv3 = nn.Conv2d(211, 63, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn3 = nn.BatchNorm2d(63, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv1 = nn.Conv2d(63, 183, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn1 = nn.BatchNorm2d(183, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv2 = nn.Conv2d(183, 183, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=183, bias=False)
        self.layers_9_bn2 = nn.BatchNorm2d(183, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv3 = nn.Conv2d(183, 63, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn3 = nn.BatchNorm2d(63, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv1 = nn.Conv2d(63, 231, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn1 = nn.BatchNorm2d(231, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv2 = nn.Conv2d(231, 231, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=231, bias=False)
        self.layers_10_bn2 = nn.BatchNorm2d(231, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv3 = nn.Conv2d(231, 94, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn3 = nn.BatchNorm2d(94, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_shortcut_0 = nn.Conv2d(63, 94, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_shortcut_1 = nn.BatchNorm2d(94, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv1 = nn.Conv2d(94, 259, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn1 = nn.BatchNorm2d(259, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv2 = nn.Conv2d(259, 259, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=259, bias=False)
        self.layers_11_bn2 = nn.BatchNorm2d(259, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv3 = nn.Conv2d(259, 94, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn3 = nn.BatchNorm2d(94, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv1 = nn.Conv2d(94, 268, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn1 = nn.BatchNorm2d(268, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv2 = nn.Conv2d(268, 268, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=268, bias=False)
        self.layers_12_bn2 = nn.BatchNorm2d(268, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv3 = nn.Conv2d(268, 94, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn3 = nn.BatchNorm2d(94, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv1 = nn.Conv2d(94, 277, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn1 = nn.BatchNorm2d(277, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv2 = nn.Conv2d(277, 277, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=277, bias=False)
        self.layers_13_bn2 = nn.BatchNorm2d(277, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv3 = nn.Conv2d(277, 149, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn3 = nn.BatchNorm2d(149, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv1 = nn.Conv2d(149, 516, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn1 = nn.BatchNorm2d(516, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv2 = nn.Conv2d(516, 516, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=516, bias=False)
        self.layers_14_bn2 = nn.BatchNorm2d(516, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv3 = nn.Conv2d(516, 149, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn3 = nn.BatchNorm2d(149, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv1 = nn.Conv2d(149, 410, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn1 = nn.BatchNorm2d(410, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv2 = nn.Conv2d(410, 410, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=410, bias=False)
        self.layers_15_bn2 = nn.BatchNorm2d(410, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv3 = nn.Conv2d(410, 149, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn3 = nn.BatchNorm2d(149, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv1 = nn.Conv2d(149, 321, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn1 = nn.BatchNorm2d(321, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv2 = nn.Conv2d(321, 321, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=321, bias=False)
        self.layers_16_bn2 = nn.BatchNorm2d(321, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv3 = nn.Conv2d(321, 303, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn3 = nn.BatchNorm2d(303, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_shortcut_0 = nn.Conv2d(149, 303, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_shortcut_1 = nn.BatchNorm2d(303, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv2 = nn.Conv2d(303, 1232, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.bn2 = nn.BatchNorm2d(1232, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.avgpool = nn.AvgPool2d(kernel_size=4, stride=4, padding=0)
        self.linear = nn.Linear(in_features=1232, out_features=100, bias=True)

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
