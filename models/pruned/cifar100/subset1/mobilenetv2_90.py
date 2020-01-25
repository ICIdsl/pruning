import torch
import torch.nn as nn
import torch.nn.functional as F

class MobileNetV2(nn.Module):
	def __init__(self, num_classes=10):
		super().__init__()

		self.conv1 = nn.Conv2d(3, 24, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.bn1 = nn.BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv1 = nn.Conv2d(24, 17, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn1 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv2 = nn.Conv2d(17, 17, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=17, bias=False)
		self.layers_0_bn2 = nn.BatchNorm2d(17, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_conv3 = nn.Conv2d(17, 9, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_bn3 = nn.BatchNorm2d(9, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_0_shortcut_0 = nn.Conv2d(24, 9, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_0_shortcut_1 = nn.BatchNorm2d(9, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv1 = nn.Conv2d(9, 46, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn1 = nn.BatchNorm2d(46, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv2 = nn.Conv2d(46, 46, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=46, bias=False)
		self.layers_1_bn2 = nn.BatchNorm2d(46, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_conv3 = nn.Conv2d(46, 4, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_bn3 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_1_shortcut_0 = nn.Conv2d(9, 4, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_1_shortcut_1 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv1 = nn.Conv2d(4, 54, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn1 = nn.BatchNorm2d(54, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv2 = nn.Conv2d(54, 54, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=54, bias=False)
		self.layers_2_bn2 = nn.BatchNorm2d(54, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_conv3 = nn.Conv2d(54, 4, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_2_bn3 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_2_shortcut = nn.Sequential()
		self.layers_3_conv1 = nn.Conv2d(4, 114, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn1 = nn.BatchNorm2d(114, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv2 = nn.Conv2d(114, 114, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=114, bias=False)
		self.layers_3_bn2 = nn.BatchNorm2d(114, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_3_conv3 = nn.Conv2d(114, 4, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_3_bn3 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv1 = nn.Conv2d(4, 87, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn1 = nn.BatchNorm2d(87, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv2 = nn.Conv2d(87, 87, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=87, bias=False)
		self.layers_4_bn2 = nn.BatchNorm2d(87, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_conv3 = nn.Conv2d(87, 4, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_4_bn3 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_4_shortcut = nn.Sequential()
		self.layers_5_conv1 = nn.Conv2d(4, 106, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn1 = nn.BatchNorm2d(106, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv2 = nn.Conv2d(106, 106, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=106, bias=False)
		self.layers_5_bn2 = nn.BatchNorm2d(106, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_conv3 = nn.Conv2d(106, 4, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_5_bn3 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_5_shortcut = nn.Sequential()
		self.layers_6_conv1 = nn.Conv2d(4, 126, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn1 = nn.BatchNorm2d(126, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv2 = nn.Conv2d(126, 126, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=126, bias=False)
		self.layers_6_bn2 = nn.BatchNorm2d(126, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_6_conv3 = nn.Conv2d(126, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_6_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv1 = nn.Conv2d(7, 99, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn1 = nn.BatchNorm2d(99, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv2 = nn.Conv2d(99, 99, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=99, bias=False)
		self.layers_7_bn2 = nn.BatchNorm2d(99, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_conv3 = nn.Conv2d(99, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_7_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_7_shortcut = nn.Sequential()
		self.layers_8_conv1 = nn.Conv2d(7, 92, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn1 = nn.BatchNorm2d(92, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv2 = nn.Conv2d(92, 92, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=92, bias=False)
		self.layers_8_bn2 = nn.BatchNorm2d(92, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_conv3 = nn.Conv2d(92, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_8_bn3 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_8_shortcut = nn.Sequential()
		self.layers_9_conv1 = nn.Conv2d(7, 68, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_9_bn1 = nn.BatchNorm2d(68, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv2 = nn.Conv2d(68, 68, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=68, bias=False)
		self.layers_9_bn2 = nn.BatchNorm2d(68, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_9_conv3 = nn.Conv2d(68, 7, kernel_size=(1, 1), stride=(1, 1), bias=False)
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
		self.layers_11_conv1 = nn.Conv2d(10, 131, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn1 = nn.BatchNorm2d(131, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv2 = nn.Conv2d(131, 131, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=131, bias=False)
		self.layers_11_bn2 = nn.BatchNorm2d(131, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_conv3 = nn.Conv2d(131, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_11_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_11_shortcut = nn.Sequential()
		self.layers_12_conv1 = nn.Conv2d(10, 145, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn1 = nn.BatchNorm2d(145, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv2 = nn.Conv2d(145, 145, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=145, bias=False)
		self.layers_12_bn2 = nn.BatchNorm2d(145, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_conv3 = nn.Conv2d(145, 10, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_12_bn3 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_12_shortcut = nn.Sequential()
		self.layers_13_conv1 = nn.Conv2d(10, 212, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn1 = nn.BatchNorm2d(212, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv2 = nn.Conv2d(212, 212, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=212, bias=False)
		self.layers_13_bn2 = nn.BatchNorm2d(212, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_13_conv3 = nn.Conv2d(212, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_13_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv1 = nn.Conv2d(16, 186, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn1 = nn.BatchNorm2d(186, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv2 = nn.Conv2d(186, 186, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=186, bias=False)
		self.layers_14_bn2 = nn.BatchNorm2d(186, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_conv3 = nn.Conv2d(186, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_14_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_14_shortcut = nn.Sequential()
		self.layers_15_conv1 = nn.Conv2d(16, 219, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn1 = nn.BatchNorm2d(219, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv2 = nn.Conv2d(219, 219, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=219, bias=False)
		self.layers_15_bn2 = nn.BatchNorm2d(219, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_conv3 = nn.Conv2d(219, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_15_bn3 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_15_shortcut = nn.Sequential()
		self.layers_16_conv1 = nn.Conv2d(16, 242, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn1 = nn.BatchNorm2d(242, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv2 = nn.Conv2d(242, 242, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=242, bias=False)
		self.layers_16_bn2 = nn.BatchNorm2d(242, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_conv3 = nn.Conv2d(242, 108, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_bn3 = nn.BatchNorm2d(108, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layers_16_shortcut_0 = nn.Conv2d(16, 108, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.layers_16_shortcut_1 = nn.BatchNorm2d(108, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.conv2 = nn.Conv2d(108, 514, kernel_size=(1, 1), stride=(1, 1), bias=False)
		self.bn2 = nn.BatchNorm2d(514, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.linear = nn.Linear(in_features=514, out_features=100, bias=True)

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
