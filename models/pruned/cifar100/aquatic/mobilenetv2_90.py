import torch
import torch.nn as nn
import torch.nn.functional as F

class MobileNetV2(nn.Module):
	def __init__(self, num_classes=10):
		super().__init__()

		self.conv1 = nn.Conv2d(3, 26, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.bn1 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv1 = nn.Conv2d(26, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn1 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv2 = nn.Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=16, bias=False)
		self.layers_0_bn2 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv3 = nn.Conv2d(16, 9, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn3 = nn.BatchNorm2d(9, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_shortcut_0 = nn.Conv2d(26, 9, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_shortcut_1 = nn.BatchNorm2d(9, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv1 = nn.Conv2d(9, 46, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn1 = nn.BatchNorm2d(46, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv2 = nn.Conv2d(46, 46, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=46, bias=False)
		self.layers_1_bn2 = nn.BatchNorm2d(46, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv3 = nn.Conv2d(46, 3, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn3 = nn.BatchNorm2d(3, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_shortcut_0 = nn.Conv2d(9, 3, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_shortcut_1 = nn.BatchNorm2d(3, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv1 = nn.Conv2d(3, 48, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn1 = nn.BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv2 = nn.Conv2d(48, 48, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=48, bias=False)
		self.layers_2_bn2 = nn.BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv3 = nn.Conv2d(48, 3, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn3 = nn.BatchNorm2d(3, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_shortcut = nn.Sequential()
		self.layers_3_conv1 = nn.Conv2d(3, 115, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn1 = nn.BatchNorm2d(115, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv2 = nn.Conv2d(115, 115, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=115, bias=False)
		self.layers_3_bn2 = nn.BatchNorm2d(115, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv3 = nn.Conv2d(115, 6, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn3 = nn.BatchNorm2d(6, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv1 = nn.Conv2d(6, 82, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn1 = nn.BatchNorm2d(82, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv2 = nn.Conv2d(82, 82, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=82, bias=False)
		self.layers_4_bn2 = nn.BatchNorm2d(82, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv3 = nn.Conv2d(82, 6, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn3 = nn.BatchNorm2d(6, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_shortcut = nn.Sequential()
		self.layers_5_conv1 = nn.Conv2d(6, 103, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn1 = nn.BatchNorm2d(103, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv2 = nn.Conv2d(103, 103, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=103, bias=False)
		self.layers_5_bn2 = nn.BatchNorm2d(103, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv3 = nn.Conv2d(103, 6, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn3 = nn.BatchNorm2d(6, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_shortcut = nn.Sequential()
		self.layers_6_conv1 = nn.Conv2d(6, 125, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn1 = nn.BatchNorm2d(125, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv2 = nn.Conv2d(125, 125, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=125, bias=False)
		self.layers_6_bn2 = nn.BatchNorm2d(125, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv3 = nn.Conv2d(125, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv1 = nn.Conv2d(7, 95, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn1 = nn.BatchNorm2d(95, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv2 = nn.Conv2d(95, 95, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=95, bias=False)
		self.layers_7_bn2 = nn.BatchNorm2d(95, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv3 = nn.Conv2d(95, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_shortcut = nn.Sequential()
		self.layers_8_conv1 = nn.Conv2d(7, 78, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn1 = nn.BatchNorm2d(78, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv2 = nn.Conv2d(78, 78, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=78, bias=False)
		self.layers_8_bn2 = nn.BatchNorm2d(78, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv3 = nn.Conv2d(78, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_shortcut = nn.Sequential()
		self.layers_9_conv1 = nn.Conv2d(7, 76, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn1 = nn.BatchNorm2d(76, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv2 = nn.Conv2d(76, 76, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=76, bias=False)
		self.layers_9_bn2 = nn.BatchNorm2d(76, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv3 = nn.Conv2d(76, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_shortcut = nn.Sequential()
		self.layers_10_conv1 = nn.Conv2d(7, 182, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_bn1 = nn.BatchNorm2d(182, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_conv2 = nn.Conv2d(182, 182, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=182, bias=False)
		self.layers_10_bn2 = nn.BatchNorm2d(182, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_conv3 = nn.Conv2d(182, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_shortcut_0 = nn.Conv2d(7, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_shortcut_1 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv1 = nn.Conv2d(10, 122, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn1 = nn.BatchNorm2d(122, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv2 = nn.Conv2d(122, 122, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=122, bias=False)
		self.layers_11_bn2 = nn.BatchNorm2d(122, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv3 = nn.Conv2d(122, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_shortcut = nn.Sequential()
		self.layers_12_conv1 = nn.Conv2d(10, 137, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn1 = nn.BatchNorm2d(137, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv2 = nn.Conv2d(137, 137, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=137, bias=False)
		self.layers_12_bn2 = nn.BatchNorm2d(137, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv3 = nn.Conv2d(137, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_shortcut = nn.Sequential()
		self.layers_13_conv1 = nn.Conv2d(10, 226, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn1 = nn.BatchNorm2d(226, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv2 = nn.Conv2d(226, 226, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=226, bias=False)
		self.layers_13_bn2 = nn.BatchNorm2d(226, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv3 = nn.Conv2d(226, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn3 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv1 = nn.Conv2d(18, 187, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn1 = nn.BatchNorm2d(187, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv2 = nn.Conv2d(187, 187, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=187, bias=False)
		self.layers_14_bn2 = nn.BatchNorm2d(187, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv3 = nn.Conv2d(187, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn3 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_shortcut = nn.Sequential()
		self.layers_15_conv1 = nn.Conv2d(18, 183, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn1 = nn.BatchNorm2d(183, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv2 = nn.Conv2d(183, 183, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=183, bias=False)
		self.layers_15_bn2 = nn.BatchNorm2d(183, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv3 = nn.Conv2d(183, 18, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn3 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_shortcut = nn.Sequential()
		self.layers_16_conv1 = nn.Conv2d(18, 231, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn1 = nn.BatchNorm2d(231, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv2 = nn.Conv2d(231, 231, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=231, bias=False)
		self.layers_16_bn2 = nn.BatchNorm2d(231, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv3 = nn.Conv2d(231, 108, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn3 = nn.BatchNorm2d(108, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_shortcut_0 = nn.Conv2d(18, 108, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_shortcut_1 = nn.BatchNorm2d(108, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.conv2 = nn.Conv2d(108, 517, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.bn2 = nn.BatchNorm2d(517, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.linear = nn.Linear(in_features=517, out_features=100, bias=True)

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
