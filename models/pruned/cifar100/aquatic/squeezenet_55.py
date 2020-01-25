import torch
import torch.nn as nn
import torch.nn.functional as F

class SqueezeNet(nn.Module):
	def __init__(self, num_classes=10):
		super().__init__()

		self.conv1 = nn.Conv2d(3, 76, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.bn1 = nn.BatchNorm2d(76, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.maxpool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
		self.fire2_conv1 = nn.Conv2d(76, 15, kernel_size=(1, 1), stride=(1, 1))
		self.fire2_bn1 = nn.BatchNorm2d(15, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire2_conv2 = nn.Conv2d(15, 64, kernel_size=(1, 1), stride=(1, 1))
		self.fire2_bn2 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire2_conv3 = nn.Conv2d(15, 41, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire2_bn3 = nn.BatchNorm2d(41, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire3_conv1 = nn.Conv2d(105, 16, kernel_size=(1, 1), stride=(1, 1))
		self.fire3_bn1 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire3_conv2 = nn.Conv2d(16, 64, kernel_size=(1, 1), stride=(1, 1))
		self.fire3_bn2 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire3_conv3 = nn.Conv2d(16, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire3_bn3 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire4_conv1 = nn.Conv2d(128, 32, kernel_size=(1, 1), stride=(1, 1))
		self.fire4_bn1 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire4_conv2 = nn.Conv2d(32, 85, kernel_size=(1, 1), stride=(1, 1))
		self.fire4_bn2 = nn.BatchNorm2d(85, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire4_conv3 = nn.Conv2d(32, 118, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire4_bn3 = nn.BatchNorm2d(118, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.maxpool2 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
		self.fire5_conv1 = nn.Conv2d(203, 32, kernel_size=(1, 1), stride=(1, 1))
		self.fire5_bn1 = nn.BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire5_conv2 = nn.Conv2d(32, 127, kernel_size=(1, 1), stride=(1, 1))
		self.fire5_bn2 = nn.BatchNorm2d(127, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire5_conv3 = nn.Conv2d(32, 91, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire5_bn3 = nn.BatchNorm2d(91, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire6_conv1 = nn.Conv2d(218, 48, kernel_size=(1, 1), stride=(1, 1))
		self.fire6_bn1 = nn.BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire6_conv2 = nn.Conv2d(48, 119, kernel_size=(1, 1), stride=(1, 1))
		self.fire6_bn2 = nn.BatchNorm2d(119, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire6_conv3 = nn.Conv2d(48, 33, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire6_bn3 = nn.BatchNorm2d(33, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire7_conv1 = nn.Conv2d(152, 48, kernel_size=(1, 1), stride=(1, 1))
		self.fire7_bn1 = nn.BatchNorm2d(48, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire7_conv2 = nn.Conv2d(48, 169, kernel_size=(1, 1), stride=(1, 1))
		self.fire7_bn2 = nn.BatchNorm2d(169, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire7_conv3 = nn.Conv2d(48, 131, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire7_bn3 = nn.BatchNorm2d(131, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire8_conv1 = nn.Conv2d(300, 64, kernel_size=(1, 1), stride=(1, 1))
		self.fire8_bn1 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire8_conv2 = nn.Conv2d(64, 239, kernel_size=(1, 1), stride=(1, 1))
		self.fire8_bn2 = nn.BatchNorm2d(239, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire8_conv3 = nn.Conv2d(64, 139, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire8_bn3 = nn.BatchNorm2d(139, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.maxpool3 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
		self.fire9_conv1 = nn.Conv2d(378, 64, kernel_size=(1, 1), stride=(1, 1))
		self.fire9_bn1 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire9_conv2 = nn.Conv2d(64, 2, kernel_size=(1, 1), stride=(1, 1))
		self.fire9_bn2 = nn.BatchNorm2d(2, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.fire9_conv3 = nn.Conv2d(64, 2, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
		self.fire9_bn3 = nn.BatchNorm2d(2, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.conv2 = nn.Conv2d(4, 100, kernel_size=(1, 1), stride=(1, 1))
		self.avg_pool = nn.AdaptiveAvgPool2d(output_size=1)
		self.softmax = nn.LogSoftmax(dim=1)

	def forward(self, x):
		x = F.relu(self.bn1(self.conv1(x)))
		x = self.maxpool1(x)
		x = F.relu(self.fire2_bn1(self.fire2_conv1(x)))
		out1x1 = self.fire2_bn2(self.fire2_conv2(x))
		out3x3 = self.fire2_bn3(self.fire2_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = F.relu(self.fire3_bn1(self.fire3_conv1(x)))
		out1x1 = self.fire3_bn2(self.fire3_conv2(x))
		out3x3 = self.fire3_bn3(self.fire3_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = F.relu(self.fire4_bn1(self.fire4_conv1(x)))
		out1x1 = self.fire4_bn2(self.fire4_conv2(x))
		out3x3 = self.fire4_bn3(self.fire4_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = self.maxpool2(x)
		x = F.relu(self.fire5_bn1(self.fire5_conv1(x)))
		out1x1 = self.fire5_bn2(self.fire5_conv2(x))
		out3x3 = self.fire5_bn3(self.fire5_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = F.relu(self.fire6_bn1(self.fire6_conv1(x)))
		out1x1 = self.fire6_bn2(self.fire6_conv2(x))
		out3x3 = self.fire6_bn3(self.fire6_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = F.relu(self.fire7_bn1(self.fire7_conv1(x)))
		out1x1 = self.fire7_bn2(self.fire7_conv2(x))
		out3x3 = self.fire7_bn3(self.fire7_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = F.relu(self.fire8_bn1(self.fire8_conv1(x)))
		out1x1 = self.fire8_bn2(self.fire8_conv2(x))
		out3x3 = self.fire8_bn3(self.fire8_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = self.maxpool3(x)
		x = F.relu(self.fire9_bn1(self.fire9_conv1(x)))
		out1x1 = self.fire9_bn2(self.fire9_conv2(x))
		out3x3 = self.fire9_bn3(self.fire9_conv3(x))
		x = F.relu(torch.cat([out1x1, out3x3], 1))
		x = self.conv2(x)
		x = self.avg_pool(x)
		x = self.softmax(x)
		return x.squeeze()

def squeezenet(**kwargs):
	return SqueezeNet(**kwargs)
