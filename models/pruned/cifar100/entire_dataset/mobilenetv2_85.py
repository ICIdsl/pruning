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
		self.layers_0_conv3 = nn.Conv2d(16, 14, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn3 = nn.BatchNorm2d(14, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_shortcut_0 = nn.Conv2d(26, 14, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_shortcut_1 = nn.BatchNorm2d(14, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv1 = nn.Conv2d(14, 48, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn1 = nn.BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv2 = nn.Conv2d(48, 48, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=48, bias=False)
		self.layers_1_bn2 = nn.BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv3 = nn.Conv2d(48, 12, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn3 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_shortcut_0 = nn.Conv2d(14, 12, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_shortcut_1 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv1 = nn.Conv2d(12, 70, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn1 = nn.BatchNorm2d(70, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv2 = nn.Conv2d(70, 70, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=70, bias=False)
		self.layers_2_bn2 = nn.BatchNorm2d(70, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv3 = nn.Conv2d(70, 12, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn3 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_shortcut = nn.Sequential()
		self.layers_3_conv1 = nn.Conv2d(12, 114, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn1 = nn.BatchNorm2d(114, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv2 = nn.Conv2d(114, 114, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=114, bias=False)
		self.layers_3_bn2 = nn.BatchNorm2d(114, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv3 = nn.Conv2d(114, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn3 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv1 = nn.Conv2d(26, 101, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn1 = nn.BatchNorm2d(101, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv2 = nn.Conv2d(101, 101, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=101, bias=False)
		self.layers_4_bn2 = nn.BatchNorm2d(101, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv3 = nn.Conv2d(101, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn3 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_shortcut = nn.Sequential()
		self.layers_5_conv1 = nn.Conv2d(26, 112, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn1 = nn.BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv2 = nn.Conv2d(112, 112, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=112, bias=False)
		self.layers_5_bn2 = nn.BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv3 = nn.Conv2d(112, 26, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn3 = nn.BatchNorm2d(26, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_shortcut = nn.Sequential()
		self.layers_6_conv1 = nn.Conv2d(26, 132, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn1 = nn.BatchNorm2d(132, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv2 = nn.Conv2d(132, 132, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=132, bias=False)
		self.layers_6_bn2 = nn.BatchNorm2d(132, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv3 = nn.Conv2d(132, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv1 = nn.Conv2d(10, 191, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn1 = nn.BatchNorm2d(191, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv2 = nn.Conv2d(191, 191, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=191, bias=False)
		self.layers_7_bn2 = nn.BatchNorm2d(191, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv3 = nn.Conv2d(191, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_shortcut = nn.Sequential()
		self.layers_8_conv1 = nn.Conv2d(10, 178, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn1 = nn.BatchNorm2d(178, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv2 = nn.Conv2d(178, 178, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=178, bias=False)
		self.layers_8_bn2 = nn.BatchNorm2d(178, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv3 = nn.Conv2d(178, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_shortcut = nn.Sequential()
		self.layers_9_conv1 = nn.Conv2d(10, 123, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn1 = nn.BatchNorm2d(123, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv2 = nn.Conv2d(123, 123, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=123, bias=False)
		self.layers_9_bn2 = nn.BatchNorm2d(123, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv3 = nn.Conv2d(123, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_shortcut = nn.Sequential()
		self.layers_10_conv1 = nn.Conv2d(10, 195, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_bn1 = nn.BatchNorm2d(195, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_conv2 = nn.Conv2d(195, 195, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=195, bias=False)
		self.layers_10_bn2 = nn.BatchNorm2d(195, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_conv3 = nn.Conv2d(195, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_bn3 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_10_shortcut_0 = nn.Conv2d(10, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_10_shortcut_1 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv1 = nn.Conv2d(17, 221, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn1 = nn.BatchNorm2d(221, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv2 = nn.Conv2d(221, 221, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=221, bias=False)
		self.layers_11_bn2 = nn.BatchNorm2d(221, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv3 = nn.Conv2d(221, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn3 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_shortcut = nn.Sequential()
		self.layers_12_conv1 = nn.Conv2d(17, 213, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn1 = nn.BatchNorm2d(213, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv2 = nn.Conv2d(213, 213, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=213, bias=False)
		self.layers_12_bn2 = nn.BatchNorm2d(213, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv3 = nn.Conv2d(213, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn3 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_shortcut = nn.Sequential()
		self.layers_13_conv1 = nn.Conv2d(17, 238, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn1 = nn.BatchNorm2d(238, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv2 = nn.Conv2d(238, 238, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=238, bias=False)
		self.layers_13_bn2 = nn.BatchNorm2d(238, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv3 = nn.Conv2d(238, 25, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn3 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv1 = nn.Conv2d(25, 437, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn1 = nn.BatchNorm2d(437, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv2 = nn.Conv2d(437, 437, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=437, bias=False)
		self.layers_14_bn2 = nn.BatchNorm2d(437, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv3 = nn.Conv2d(437, 25, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn3 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_shortcut = nn.Sequential()
		self.layers_15_conv1 = nn.Conv2d(25, 318, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn1 = nn.BatchNorm2d(318, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv2 = nn.Conv2d(318, 318, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=318, bias=False)
		self.layers_15_bn2 = nn.BatchNorm2d(318, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv3 = nn.Conv2d(318, 25, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn3 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_shortcut = nn.Sequential()
		self.layers_16_conv1 = nn.Conv2d(25, 274, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn1 = nn.BatchNorm2d(274, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv2 = nn.Conv2d(274, 274, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=274, bias=False)
		self.layers_16_bn2 = nn.BatchNorm2d(274, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv3 = nn.Conv2d(274, 109, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn3 = nn.BatchNorm2d(109, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_shortcut_0 = nn.Conv2d(25, 109, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_shortcut_1 = nn.BatchNorm2d(109, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.conv2 = nn.Conv2d(109, 670, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.bn2 = nn.BatchNorm2d(670, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.linear = nn.Linear(in_features=670, out_features=100, bias=True)

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
