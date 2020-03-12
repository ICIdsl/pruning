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
        self.layers_0_conv3 = nn.Conv2d(18, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_0_shortcut_0 = nn.Conv2d(27, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_0_shortcut_1 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv1 = nn.Conv2d(16, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn1 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv2 = nn.Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64, bias=False)
        self.layers_1_bn2 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_conv3 = nn.Conv2d(64, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_bn3 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_1_shortcut_0 = nn.Conv2d(16, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_1_shortcut_1 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv1 = nn.Conv2d(24, 93, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn1 = nn.BatchNorm2d(93, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv2 = nn.Conv2d(93, 93, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=93, bias=False)
        self.layers_2_bn2 = nn.BatchNorm2d(93, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_2_conv3 = nn.Conv2d(93, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_2_bn3 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv1 = nn.Conv2d(24, 122, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn1 = nn.BatchNorm2d(122, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv2 = nn.Conv2d(122, 122, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=122, bias=False)
        self.layers_3_bn2 = nn.BatchNorm2d(122, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_3_conv3 = nn.Conv2d(122, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_3_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv1 = nn.Conv2d(32, 144, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn1 = nn.BatchNorm2d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv2 = nn.Conv2d(144, 144, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=144, bias=False)
        self.layers_4_bn2 = nn.BatchNorm2d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_4_conv3 = nn.Conv2d(144, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_4_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv1 = nn.Conv2d(32, 141, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn1 = nn.BatchNorm2d(141, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv2 = nn.Conv2d(141, 141, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=141, bias=False)
        self.layers_5_bn2 = nn.BatchNorm2d(141, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_5_conv3 = nn.Conv2d(141, 32, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_5_bn3 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv1 = nn.Conv2d(32, 155, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn1 = nn.BatchNorm2d(155, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv2 = nn.Conv2d(155, 155, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=155, bias=False)
        self.layers_6_bn2 = nn.BatchNorm2d(155, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_6_conv3 = nn.Conv2d(155, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_6_bn3 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv1 = nn.Conv2d(64, 283, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn1 = nn.BatchNorm2d(283, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv2 = nn.Conv2d(283, 283, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=283, bias=False)
        self.layers_7_bn2 = nn.BatchNorm2d(283, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_7_conv3 = nn.Conv2d(283, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_7_bn3 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv1 = nn.Conv2d(64, 266, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn1 = nn.BatchNorm2d(266, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv2 = nn.Conv2d(266, 266, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=266, bias=False)
        self.layers_8_bn2 = nn.BatchNorm2d(266, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_8_conv3 = nn.Conv2d(266, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_8_bn3 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv1 = nn.Conv2d(64, 236, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn1 = nn.BatchNorm2d(236, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv2 = nn.Conv2d(236, 236, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=236, bias=False)
        self.layers_9_bn2 = nn.BatchNorm2d(236, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_9_conv3 = nn.Conv2d(236, 64, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_9_bn3 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv1 = nn.Conv2d(64, 277, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn1 = nn.BatchNorm2d(277, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv2 = nn.Conv2d(277, 277, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=277, bias=False)
        self.layers_10_bn2 = nn.BatchNorm2d(277, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_conv3 = nn.Conv2d(277, 96, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_bn3 = nn.BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_10_shortcut_0 = nn.Conv2d(64, 96, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_10_shortcut_1 = nn.BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv1 = nn.Conv2d(96, 355, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn1 = nn.BatchNorm2d(355, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv2 = nn.Conv2d(355, 355, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=355, bias=False)
        self.layers_11_bn2 = nn.BatchNorm2d(355, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_11_conv3 = nn.Conv2d(355, 96, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_11_bn3 = nn.BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv1 = nn.Conv2d(96, 373, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn1 = nn.BatchNorm2d(373, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv2 = nn.Conv2d(373, 373, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=373, bias=False)
        self.layers_12_bn2 = nn.BatchNorm2d(373, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_12_conv3 = nn.Conv2d(373, 96, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_12_bn3 = nn.BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv1 = nn.Conv2d(96, 370, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn1 = nn.BatchNorm2d(370, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv2 = nn.Conv2d(370, 370, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=370, bias=False)
        self.layers_13_bn2 = nn.BatchNorm2d(370, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_13_conv3 = nn.Conv2d(370, 160, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_13_bn3 = nn.BatchNorm2d(160, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv1 = nn.Conv2d(160, 652, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn1 = nn.BatchNorm2d(652, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv2 = nn.Conv2d(652, 652, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=652, bias=False)
        self.layers_14_bn2 = nn.BatchNorm2d(652, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_14_conv3 = nn.Conv2d(652, 160, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_14_bn3 = nn.BatchNorm2d(160, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv1 = nn.Conv2d(160, 577, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn1 = nn.BatchNorm2d(577, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv2 = nn.Conv2d(577, 577, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=577, bias=False)
        self.layers_15_bn2 = nn.BatchNorm2d(577, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_15_conv3 = nn.Conv2d(577, 160, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_15_bn3 = nn.BatchNorm2d(160, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv1 = nn.Conv2d(160, 471, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn1 = nn.BatchNorm2d(471, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv2 = nn.Conv2d(471, 471, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=471, bias=False)
        self.layers_16_bn2 = nn.BatchNorm2d(471, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_conv3 = nn.Conv2d(471, 320, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_bn3 = nn.BatchNorm2d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layers_16_shortcut_0 = nn.Conv2d(160, 320, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layers_16_shortcut_1 = nn.BatchNorm2d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv2 = nn.Conv2d(320, 1261, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.bn2 = nn.BatchNorm2d(1261, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.avgpool = nn.AvgPool2d(kernel_size=4, stride=4, padding=0)
        self.linear = nn.Linear(in_features=1261, out_features=100, bias=True)

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
