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
        self.layers_1_conv1 = nn.Conv2d(16, 51, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn1 = nn.BatchNorm2d(51, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv2 = nn.Conv2d(51, 51, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=51, bias=False)
        self.layers_1_bn2 = nn.BatchNorm2d(51, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv3 = nn.Conv2d(51, 22, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn3 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_shortcut_0 = nn.Conv2d(16, 22, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_shortcut_1 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv1 = nn.Conv2d(22, 78, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn1 = nn.BatchNorm2d(78, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv2 = nn.Conv2d(78, 78, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=78, bias=False)
        self.layers_2_bn2 = nn.BatchNorm2d(78, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv3 = nn.Conv2d(78, 22, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn3 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv1 = nn.Conv2d(22, 116, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn1 = nn.BatchNorm2d(116, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv2 = nn.Conv2d(116, 116, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=116, bias=False)
        self.layers_3_bn2 = nn.BatchNorm2d(116, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv3 = nn.Conv2d(116, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv1 = nn.Conv2d(32, 120, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn1 = nn.BatchNorm2d(120, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv2 = nn.Conv2d(120, 120, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=120, bias=False)
        self.layers_4_bn2 = nn.BatchNorm2d(120, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv3 = nn.Conv2d(120, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv1 = nn.Conv2d(32, 122, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn1 = nn.BatchNorm2d(122, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv2 = nn.Conv2d(122, 122, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=122, bias=False)
        self.layers_5_bn2 = nn.BatchNorm2d(122, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv3 = nn.Conv2d(122, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv1 = nn.Conv2d(32, 135, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn1 = nn.BatchNorm2d(135, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv2 = nn.Conv2d(135, 135, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=135, bias=False)
        self.layers_6_bn2 = nn.BatchNorm2d(135, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv3 = nn.Conv2d(135, 57, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn3 = nn.BatchNorm2d(57, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv1 = nn.Conv2d(57, 222, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn1 = nn.BatchNorm2d(222, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv2 = nn.Conv2d(222, 222, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=222, bias=False)
        self.layers_7_bn2 = nn.BatchNorm2d(222, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv3 = nn.Conv2d(222, 57, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn3 = nn.BatchNorm2d(57, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv1 = nn.Conv2d(57, 208, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn1 = nn.BatchNorm2d(208, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv2 = nn.Conv2d(208, 208, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=208, bias=False)
        self.layers_8_bn2 = nn.BatchNorm2d(208, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv3 = nn.Conv2d(208, 57, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn3 = nn.BatchNorm2d(57, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv1 = nn.Conv2d(57, 159, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn1 = nn.BatchNorm2d(159, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv2 = nn.Conv2d(159, 159, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=159, bias=False)
        self.layers_9_bn2 = nn.BatchNorm2d(159, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv3 = nn.Conv2d(159, 57, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn3 = nn.BatchNorm2d(57, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv1 = nn.Conv2d(57, 218, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn1 = nn.BatchNorm2d(218, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv2 = nn.Conv2d(218, 218, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=218, bias=False)
        self.layers_10_bn2 = nn.BatchNorm2d(218, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv3 = nn.Conv2d(218, 72, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn3 = nn.BatchNorm2d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_shortcut_0 = nn.Conv2d(57, 72, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_shortcut_1 = nn.BatchNorm2d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv1 = nn.Conv2d(72, 243, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn1 = nn.BatchNorm2d(243, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv2 = nn.Conv2d(243, 243, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=243, bias=False)
        self.layers_11_bn2 = nn.BatchNorm2d(243, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv3 = nn.Conv2d(243, 72, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn3 = nn.BatchNorm2d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv1 = nn.Conv2d(72, 249, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn1 = nn.BatchNorm2d(249, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv2 = nn.Conv2d(249, 249, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=249, bias=False)
        self.layers_12_bn2 = nn.BatchNorm2d(249, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv3 = nn.Conv2d(249, 72, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn3 = nn.BatchNorm2d(72, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv1 = nn.Conv2d(72, 247, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn1 = nn.BatchNorm2d(247, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv2 = nn.Conv2d(247, 247, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=247, bias=False)
        self.layers_13_bn2 = nn.BatchNorm2d(247, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv3 = nn.Conv2d(247, 129, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn3 = nn.BatchNorm2d(129, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv1 = nn.Conv2d(129, 491, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn1 = nn.BatchNorm2d(491, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv2 = nn.Conv2d(491, 491, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=491, bias=False)
        self.layers_14_bn2 = nn.BatchNorm2d(491, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv3 = nn.Conv2d(491, 129, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn3 = nn.BatchNorm2d(129, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv1 = nn.Conv2d(129, 377, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn1 = nn.BatchNorm2d(377, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv2 = nn.Conv2d(377, 377, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=377, bias=False)
        self.layers_15_bn2 = nn.BatchNorm2d(377, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv3 = nn.Conv2d(377, 129, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn3 = nn.BatchNorm2d(129, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv1 = nn.Conv2d(129, 305, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn1 = nn.BatchNorm2d(305, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv2 = nn.Conv2d(305, 305, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=305, bias=False)
        self.layers_16_bn2 = nn.BatchNorm2d(305, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv3 = nn.Conv2d(305, 257, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn3 = nn.BatchNorm2d(257, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_shortcut_0 = nn.Conv2d(129, 257, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_shortcut_1 = nn.BatchNorm2d(257, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv2 = nn.Conv2d(257, 1177, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.bn2 = nn.BatchNorm2d(1177, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.avgpool = nn.AvgPool2d(kernel_size=4, stride=4, padding=0)
        self.linear = nn.Linear(in_features=1177, out_features=100, bias=True)

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
