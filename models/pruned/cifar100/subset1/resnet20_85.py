import torch
import torch.nn as nn
import torch.nn.functional as F

class ResNet20(nn.Module):
	def __init__(self, num_classes=10):
		super().__init__()

		self.conv1 = nn.Conv2d(3, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.bn1 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_0_conv1 = nn.Conv2d(4, 9, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_0_bn1 = nn.BatchNorm2d(9, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_0_conv2 = nn.Conv2d(9, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_0_bn2 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_1_conv1 = nn.Conv2d(4, 11, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_1_bn1 = nn.BatchNorm2d(11, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_1_conv2 = nn.Conv2d(11, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_1_bn2 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_2_conv1 = nn.Conv2d(4, 14, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_2_bn1 = nn.BatchNorm2d(14, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_2_conv2 = nn.Conv2d(14, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_2_bn2 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_0_conv1 = nn.Conv2d(4, 31, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
		self.layer2_0_bn1 = nn.BatchNorm2d(31, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_0_conv2 = nn.Conv2d(31, 10, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_0_bn2 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_0_downsample_0 = nn.Conv2d(4, 10, kernel_size=(1, 1), stride=(2, 2), bias=False)
		self.layer2_0_downsample_1 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_1_conv1 = nn.Conv2d(10, 22, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_1_bn1 = nn.BatchNorm2d(22, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_1_conv2 = nn.Conv2d(22, 10, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_1_bn2 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_2_conv1 = nn.Conv2d(10, 25, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_2_bn1 = nn.BatchNorm2d(25, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_2_conv2 = nn.Conv2d(25, 10, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_2_bn2 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_0_conv1 = nn.Conv2d(10, 43, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
		self.layer3_0_bn1 = nn.BatchNorm2d(43, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_0_conv2 = nn.Conv2d(43, 10, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_0_bn2 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_0_downsample_0 = nn.Conv2d(10, 10, kernel_size=(1, 1), stride=(2, 2), bias=False)
		self.layer3_0_downsample_1 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_1_conv1 = nn.Conv2d(10, 46, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_1_bn1 = nn.BatchNorm2d(46, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_1_conv2 = nn.Conv2d(46, 10, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_1_bn2 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_2_conv1 = nn.Conv2d(10, 30, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_2_bn1 = nn.BatchNorm2d(30, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_2_conv2 = nn.Conv2d(30, 10, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_2_bn2 = nn.BatchNorm2d(10, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.avgpool = nn.AvgPool2d(kernel_size=8, stride=8, padding=0)
		self.fc = nn.Linear(in_features=10, out_features=100, bias=True)

	def forward(self, x):
		x = F.relu(self.bn1(self.conv1(x)))
		out = F.relu(self.layer1_0_bn1(self.layer1_0_conv1(x)))
		out = self.layer1_0_bn2(self.layer1_0_conv2(out))
		x = F.relu(out + x)
		out = F.relu(self.layer1_1_bn1(self.layer1_1_conv1(x)))
		out = self.layer1_1_bn2(self.layer1_1_conv2(out))
		x = F.relu(out + x)
		out = F.relu(self.layer1_2_bn1(self.layer1_2_conv1(x)))
		out = self.layer1_2_bn2(self.layer1_2_conv2(out))
		x = F.relu(out + x)
		out = F.relu(self.layer2_0_bn1(self.layer2_0_conv1(x)))
		out = self.layer2_0_bn2(self.layer2_0_conv2(out))
		x = F.relu(out + self.layer2_0_downsample_1(self.layer2_0_downsample_0(x)))
		x = F.relu(out + x)
		out = F.relu(self.layer2_1_bn1(self.layer2_1_conv1(x)))
		out = self.layer2_1_bn2(self.layer2_1_conv2(out))
		x = F.relu(out + x)
		out = F.relu(self.layer2_2_bn1(self.layer2_2_conv1(x)))
		out = self.layer2_2_bn2(self.layer2_2_conv2(out))
		x = F.relu(out + x)
		out = F.relu(self.layer3_0_bn1(self.layer3_0_conv1(x)))
		out = self.layer3_0_bn2(self.layer3_0_conv2(out))
		x = F.relu(out + self.layer3_0_downsample_1(self.layer3_0_downsample_0(x)))
		x = F.relu(out + x)
		out = F.relu(self.layer3_1_bn1(self.layer3_1_conv1(x)))
		out = self.layer3_1_bn2(self.layer3_1_conv2(out))
		x = F.relu(out + x)
		out = F.relu(self.layer3_2_bn1(self.layer3_2_conv1(x)))
		out = self.layer3_2_bn2(self.layer3_2_conv2(out))
		x = F.relu(out + x)
		x = self.avgpool(x)
		x = x.view(x.size(0), -1)
		x = self.fc(x)
		return x

def resnet(**kwargs):
	return ResNet(**kwargs)
