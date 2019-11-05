import torch
import torch.nn as nn
import torch.nn.functional as F

class ResNet20(nn.Module):
	def __init__(self, num_classes=10):
		super().__init__()

		self.conv1 = nn.Conv2d(3, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.bn1 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_0_conv1 = nn.Conv2d(4, 8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_0_bn1 = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_0_conv2 = nn.Conv2d(8, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_0_bn2 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_1_conv1 = nn.Conv2d(4, 7, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_1_bn1 = nn.BatchNorm2d(7, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_1_conv2 = nn.Conv2d(7, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_1_bn2 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_2_conv1 = nn.Conv2d(4, 11, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_2_bn1 = nn.BatchNorm2d(11, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer1_2_conv2 = nn.Conv2d(11, 4, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer1_2_bn2 = nn.BatchNorm2d(4, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_0_conv1 = nn.Conv2d(4, 20, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
		self.layer2_0_bn1 = nn.BatchNorm2d(20, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_0_conv2 = nn.Conv2d(20, 8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_0_bn2 = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_0_downsample_0 = nn.Conv2d(4, 8, kernel_size=(1, 1), stride=(2, 2), bias=False)
		self.layer2_0_downsample_1 = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_1_conv1 = nn.Conv2d(8, 12, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_1_bn1 = nn.BatchNorm2d(12, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_1_conv2 = nn.Conv2d(12, 8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_1_bn2 = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_2_conv1 = nn.Conv2d(8, 18, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_2_bn1 = nn.BatchNorm2d(18, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer2_2_conv2 = nn.Conv2d(18, 8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer2_2_bn2 = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_0_conv1 = nn.Conv2d(8, 28, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
		self.layer3_0_bn1 = nn.BatchNorm2d(28, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_0_conv2 = nn.Conv2d(28, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_0_bn2 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_0_downsample_0 = nn.Conv2d(8, 16, kernel_size=(1, 1), stride=(2, 2), bias=False)
		self.layer3_0_downsample_1 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_1_conv1 = nn.Conv2d(16, 31, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_1_bn1 = nn.BatchNorm2d(31, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_1_conv2 = nn.Conv2d(31, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_1_bn2 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_2_conv1 = nn.Conv2d(16, 34, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_2_bn1 = nn.BatchNorm2d(34, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.layer3_2_conv2 = nn.Conv2d(34, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
		self.layer3_2_bn2 = nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
		self.avgpool = nn.AvgPool2d(kernel_size=8, stride=8, padding=0)
		self.fc = nn.Linear(in_features=16, out_features=100, bias=True)

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