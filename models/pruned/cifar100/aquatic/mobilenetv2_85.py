import torch
import torch.nn as nn
import torch.nn.functional as F

class MobileNetV2(nn.Module):
	def __init__(self, num_classes=10):
		super().__init__()

		self.conv1 = nn.Conv2d(3, 26, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.bn1 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv1 = nn.Conv2d(26, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn1 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv2 = nn.Conv2d(17, 17, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=17, bias=False)
		self.layers_0_bn2 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv3 = nn.Conv2d(17, 14, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn3 = nn.BatchNorm2d(14, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_shortcut_0 = nn.Conv2d(26, 14, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_shortcut_1 = nn.BatchNorm2d(14, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv1 = nn.Conv2d(14, 50, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn1 = nn.BatchNorm2d(50, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv2 = nn.Conv2d(50, 50, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=50, bias=False)
		self.layers_1_bn2 = nn.BatchNorm2d(50, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv3 = nn.Conv2d(50, 12, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn3 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_shortcut_0 = nn.Conv2d(14, 12, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_shortcut_1 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv1 = nn.Conv2d(12, 68, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn1 = nn.BatchNorm2d(68, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv2 = nn.Conv2d(68, 68, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=68, bias=False)
		self.layers_2_bn2 = nn.BatchNorm2d(68, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv3 = nn.Conv2d(68, 12, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn3 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_shortcut = nn.Sequential()
		self.layers_3_conv1 = nn.Conv2d(12, 116, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn1 = nn.BatchNorm2d(116, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv2 = nn.Conv2d(116, 116, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=116, bias=False)
		self.layers_3_bn2 = nn.BatchNorm2d(116, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv3 = nn.Conv2d(116, 22, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn3 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv1 = nn.Conv2d(22, 99, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn1 = nn.BatchNorm2d(99, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv2 = nn.Conv2d(99, 99, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=99, bias=False)
		self.layers_4_bn2 = nn.BatchNorm2d(99, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv3 = nn.Conv2d(99, 22, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn3 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_shortcut = nn.Sequential()
		self.layers_5_conv1 = nn.Conv2d(22, 110, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn1 = nn.BatchNorm2d(110, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv2 = nn.Conv2d(110, 110, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=110, bias=False)
		self.layers_5_bn2 = nn.BatchNorm2d(110, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv3 = nn.Conv2d(110, 22, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn3 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_shortcut = nn.Sequential()
		self.layers_6_conv1 = nn.Conv2d(22, 130, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn1 = nn.BatchNorm2d(130, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv2 = nn.Conv2d(130, 130, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=130, bias=False)
		self.layers_6_bn2 = nn.BatchNorm2d(130, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv3 = nn.Conv2d(130, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv1 = nn.Conv2d(13, 192, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn1 = nn.BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv2 = nn.Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192, bias=False)
		self.layers_7_bn2 = nn.BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv3 = nn.Conv2d(192, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_shortcut = nn.Sequential()
		self.layers_8_conv1 = nn.Conv2d(13, 170, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn1 = nn.BatchNorm2d(170, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv2 = nn.Conv2d(170, 170, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=170, bias=False)
		self.layers_8_bn2 = nn.BatchNorm2d(170, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv3 = nn.Conv2d(170, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_shortcut = nn.Sequential()
		self.layers_9_conv1 = nn.Conv2d(13, 128, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn1 = nn.BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv2 = nn.Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=128, bias=False)
		self.layers_9_bn2 = nn.BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv3 = nn.Conv2d(128, 13, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn3 = nn.BatchNorm2d(13, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_shortcut = nn.Sequential()
		self.layers_10_conv1 = nn.Conv2d(13, 199, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_bn1 = nn.BatchNorm2d(199, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_conv2 = nn.Conv2d(199, 199, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=199, bias=False)
		self.layers_10_bn2 = nn.BatchNorm2d(199, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_conv3 = nn.Conv2d(199, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_bn3 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_shortcut_0 = nn.Conv2d(13, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_shortcut_1 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv1 = nn.Conv2d(18, 205, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn1 = nn.BatchNorm2d(205, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv2 = nn.Conv2d(205, 205, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=205, bias=False)
		self.layers_11_bn2 = nn.BatchNorm2d(205, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv3 = nn.Conv2d(205, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn3 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_shortcut = nn.Sequential()
		self.layers_12_conv1 = nn.Conv2d(18, 218, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn1 = nn.BatchNorm2d(218, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv2 = nn.Conv2d(218, 218, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=218, bias=False)
		self.layers_12_bn2 = nn.BatchNorm2d(218, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv3 = nn.Conv2d(218, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn3 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_shortcut = nn.Sequential()
		self.layers_13_conv1 = nn.Conv2d(18, 242, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn1 = nn.BatchNorm2d(242, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv2 = nn.Conv2d(242, 242, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=242, bias=False)
		self.layers_13_bn2 = nn.BatchNorm2d(242, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv3 = nn.Conv2d(242, 25, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn3 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv1 = nn.Conv2d(25, 436, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn1 = nn.BatchNorm2d(436, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv2 = nn.Conv2d(436, 436, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=436, bias=False)
		self.layers_14_bn2 = nn.BatchNorm2d(436, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv3 = nn.Conv2d(436, 25, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn3 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_shortcut = nn.Sequential()
		self.layers_15_conv1 = nn.Conv2d(25, 324, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn1 = nn.BatchNorm2d(324, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv2 = nn.Conv2d(324, 324, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=324, bias=False)
		self.layers_15_bn2 = nn.BatchNorm2d(324, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv3 = nn.Conv2d(324, 25, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn3 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_shortcut = nn.Sequential()
		self.layers_16_conv1 = nn.Conv2d(25, 285, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn1 = nn.BatchNorm2d(285, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv2 = nn.Conv2d(285, 285, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=285, bias=False)
		self.layers_16_bn2 = nn.BatchNorm2d(285, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv3 = nn.Conv2d(285, 103, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn3 = nn.BatchNorm2d(103, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_shortcut_0 = nn.Conv2d(25, 103, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_shortcut_1 = nn.BatchNorm2d(103, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.conv2 = nn.Conv2d(103, 678, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.bn2 = nn.BatchNorm2d(678, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.linear = nn.Linear(in_features=678, out_features=100, bias=True)

	def forward(self, x):
		x = F.relu(self.bn1(self.conv1(x)))
		out = F.relu(self.layers_0_bn1(self.layers_0_conv1(x)))
		out = F.relu(self.layers_0_bn2(self.layers_0_conv2(out)))
		out = self.layers_0_bn3(self.layers_0_conv3(out))
		x = out + self.layers_0_shortcut_1(self.layers_0_shortcut_0(x))
		out = F.relu(self.layers_1_bn1(self.layers_1_conv1(x)))
		out = F.relu(self.layers_1_bn2(self.layers_1_conv2(out)))
		out = self.layers_1_bn3(self.layers_1_conv3(out))
		x = out + self.layers_1_shortcut_1(self.layers_1_shortcut_0(x))
		out = F.relu(self.layers_2_bn1(self.layers_2_conv1(x)))
		out = F.relu(self.layers_2_bn2(self.layers_2_conv2(out)))
		out = self.layers_2_bn3(self.layers_2_conv3(out))
		x = out + self.layers_2_shortcut(x)
		out = F.relu(self.layers_3_bn1(self.layers_3_conv1(x)))
		out = F.relu(self.layers_3_bn2(self.layers_3_conv2(out)))
		out = self.layers_3_bn3(self.layers_3_conv3(out))
		x = out
		out = F.relu(self.layers_4_bn1(self.layers_4_conv1(x)))
		out = F.relu(self.layers_4_bn2(self.layers_4_conv2(out)))
		out = self.layers_4_bn3(self.layers_4_conv3(out))
		x = out + self.layers_4_shortcut(x)
		out = F.relu(self.layers_5_bn1(self.layers_5_conv1(x)))
		out = F.relu(self.layers_5_bn2(self.layers_5_conv2(out)))
		out = self.layers_5_bn3(self.layers_5_conv3(out))
		x = out + self.layers_5_shortcut(x)
		out = F.relu(self.layers_6_bn1(self.layers_6_conv1(x)))
		out = F.relu(self.layers_6_bn2(self.layers_6_conv2(out)))
		out = self.layers_6_bn3(self.layers_6_conv3(out))
		x = out
		out = F.relu(self.layers_7_bn1(self.layers_7_conv1(x)))
		out = F.relu(self.layers_7_bn2(self.layers_7_conv2(out)))
		out = self.layers_7_bn3(self.layers_7_conv3(out))
		x = out + self.layers_7_shortcut(x)
		out = F.relu(self.layers_8_bn1(self.layers_8_conv1(x)))
		out = F.relu(self.layers_8_bn2(self.layers_8_conv2(out)))
		out = self.layers_8_bn3(self.layers_8_conv3(out))
		x = out + self.layers_8_shortcut(x)
		out = F.relu(self.layers_9_bn1(self.layers_9_conv1(x)))
		out = F.relu(self.layers_9_bn2(self.layers_9_conv2(out)))
		out = self.layers_9_bn3(self.layers_9_conv3(out))
		x = out + self.layers_9_shortcut(x)
		out = F.relu(self.layers_10_bn1(self.layers_10_conv1(x)))
		out = F.relu(self.layers_10_bn2(self.layers_10_conv2(out)))
		out = self.layers_10_bn3(self.layers_10_conv3(out))
		x = out + self.layers_10_shortcut_1(self.layers_10_shortcut_0(x))
		out = F.relu(self.layers_11_bn1(self.layers_11_conv1(x)))
		out = F.relu(self.layers_11_bn2(self.layers_11_conv2(out)))
		out = self.layers_11_bn3(self.layers_11_conv3(out))
		x = out + self.layers_11_shortcut(x)
		out = F.relu(self.layers_12_bn1(self.layers_12_conv1(x)))
		out = F.relu(self.layers_12_bn2(self.layers_12_conv2(out)))
		out = self.layers_12_bn3(self.layers_12_conv3(out))
		x = out + self.layers_12_shortcut(x)
		out = F.relu(self.layers_13_bn1(self.layers_13_conv1(x)))
		out = F.relu(self.layers_13_bn2(self.layers_13_conv2(out)))
		out = self.layers_13_bn3(self.layers_13_conv3(out))
		x = out
		out = F.relu(self.layers_14_bn1(self.layers_14_conv1(x)))
		out = F.relu(self.layers_14_bn2(self.layers_14_conv2(out)))
		out = self.layers_14_bn3(self.layers_14_conv3(out))
		x = out + self.layers_14_shortcut(x)
		out = F.relu(self.layers_15_bn1(self.layers_15_conv1(x)))
		out = F.relu(self.layers_15_bn2(self.layers_15_conv2(out)))
		out = self.layers_15_bn3(self.layers_15_conv3(out))
		x = out + self.layers_15_shortcut(x)
		out = F.relu(self.layers_16_bn1(self.layers_16_conv1(x)))
		out = F.relu(self.layers_16_bn2(self.layers_16_conv2(out)))
		out = self.layers_16_bn3(self.layers_16_conv3(out))
		x = out + self.layers_16_shortcut_1(self.layers_16_shortcut_0(x))
		x = F.relu(self.bn2(self.conv2(x)))
		x = F.avg_pool2d(x,4)
		x = x.view(x.size(0), -1)
		x = self.linear(x)
		return x

def mobilenetv2(**kwargs):
	return MobileNetV2(**kwargs)
