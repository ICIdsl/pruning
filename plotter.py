import sys
import matplotlib.pyplot as plt
import os
import json
import torch.nn as nn
import numpy as np
import subprocess
import itertools
from scipy.spatial import distance
import pandas as pd

class ChannelPlotter(object):
#{{{
    def __init__(self, params, model):
    #{{{
        self.params = params
        self.model = model
        
        # if 'resnet' in self.params.arch:
        #     self.net = str(self.params.arch) + str(self.params.depth)
        # else:
        #     self.net = str(self.params.arch)
        self.net = str(self.params.arch)
        
        self.subsets = ['entire_dataset', 'subset1', 'aquatic']
        
        # if 'mobilenet' in self.net:
        #     self.logDir = '/mnt/users/ar4414/pruning_logs/' + self.net +'/cifar100/{}/l1_prune'
        # else:
        #     self.logDir = '/home/ar4414/pytorch_training/src/ar4414/pruning/logs/' + self.net +'/cifar100/{}/l1_prune'
        self.logDir = '/home/ar4414/pytorch_training/src/ar4414/pruning/logs/' + self.net +'/cifar100/{}/l1_prune'
    #}}}

    def save_fig(self, plt, plotType=''):
    #{{{
        plt.tight_layout()

        # plt.show()
        
        folder = os.path.join('/home/ar4414/remote_copy/channels/', self.net, plotType)
        fig = os.path.join(folder, 'pp_{}.png'.format(int(self.prunePerc)))
        cmd = 'mkdir -p {}'.format(folder)
        subprocess.check_call(cmd, shell=True)
        print('Saving - {}'.format(fig))
        plt.savefig(fig, format='png') 
    #}}}
        
    def plot_channels(self):
    #{{{
        self.pivotDict = {}
        for i, logFile in enumerate(self.params.plotChannels):
            logDir = os.path.join(self.logDir.format(self.subsets[i%3]), logFile)
            
            try:
                with open(os.path.join(logDir, 'pruned_channels.json'), 'r') as cpFile:
                    channelsPruned = json.load(cpFile)
            except FileNotFoundError:
                print("File : {} does not exist.".format(os.path.join(logDir, 'pruned_channels.json')))
                print("Either the log directory is wrong or run finetuning without GetGops to generate file before running this command.")
                sys.exit()
            
            pruneEpoch = int(list(channelsPruned.keys())[0])
            channelsPruned = list(channelsPruned.values())[0]
            self.prunePerc = channelsPruned.pop('prunePerc')
            allChannelsByLayer = {l:np.zeros(m.out_channels,dtype=int) for l,m in self.model.named_modules() if isinstance(m, nn.Conv2d)}

            if self.prunePerc == 0.:
                continue
            
            for j,(l,c) in enumerate(allChannelsByLayer.items()):
                c[channelsPruned[l]] = 1                              

            self.layerNames = ['.'.join(x.split('.')[1:]) for x in list(allChannelsByLayer.keys())]
            self.numChannelsPerLayer = [len(v) for v in allChannelsByLayer.values()]

            self.pivotDict[self.subsets[i%3]] = {'grad':allChannelsByLayer, 'pp':self.prunePerc}
            
            if (i+1)%3 == 0:
                if self.params.plotType == 'number':
                    fig, ax = plt.subplots(figsize=(10,5))
                    self.plot_num_pruned(ax)
                
                elif self.params.plotType == 'hamming':
                    fig, ax = plt.subplots(figsize=(10,5))
                    self.plot_hamming(ax)
                
                else:
                    fig, axs = plt.subplots(2,1,figsize=(20,10))
                    self.plot_num_pruned(axs[0])
                    self.plot_hamming(axs[1])
                
                self.save_fig(plt, self.params.plotType)
                
                self.pivotDict = {}
    #}}}        

    def plot_channel_comparisons(self):
    #{{{
        fig, ax = plt.subplots()
        bar = ax.barh(self.layerNames, self.numChannelsPerLayer)
        
        ax = bar[0].axes
        lim = ax.get_xlim() + ax.get_ylim()
        
        for i, bar in enumerate(bar):
            layer = 'module.' + self.layerNames[i]
            
            grads = []
            for k,v in self.pivotDict.items():
                grads.append(v['grad'][layer])
                prunePerc = v['pp']
            
            if (np.array_equal(grads[0], grads[1])) and (np.array_equal(grads[1], grads[2])): 
                grad = np.array(grads[0])
                grad = np.expand_dims(grad, 1).T
                bar.set_zorder(1)
                bar.set_facecolor("none")
                x,y = bar.get_xy()
                w,h = bar.get_width(), bar.get_height()
                ax.imshow(grad, extent=[x,x+w,y,y+h], aspect="auto", zorder=0)
            else:
                inc = bar.get_height() / 3.
                cmaps = ['viridis', 'winter', 'rainbow']
                for i in range(3):
                    grad = np.array(grads[i])
                    grad = np.expand_dims(grad, 1).T
                    bar.set_zorder(1)
                    bar.set_facecolor("none")
                    x,y = bar.get_xy()
                    w,h = bar.get_width(), bar.get_height()
                    ax.imshow(grad, extent=[x,x+w,y+(i*inc),y+((i+1)*inc)], aspect="auto", cmap=cmaps[i], zorder=0)
        
        ax.axis(lim)
        ax.set_title('Channels Pruned By Layer for {:.2f}% pruning'.format(prunePerc))
        plt.tight_layout()
        
        folder = '/home/ar4414/remote_copy/channels/'
        fig = os.path.join(folder, 'p_{}.png'.format(int(prunePerc)))
        cmd = 'mkdir -p {}'.format(folder)
        subprocess.check_call(cmd, shell=True)
        print('Saving - {}'.format(fig))
        plt.savefig(fig, format='png') 
    #}}} 

    def plot_hamming(self, axes):
    #{{{
        channels = {}

        for layer in self.layerNames:
            channels[layer] = {ss : self.pivotDict[ss]['grad']['module.'+layer] for ss in self.subsets}
        
        hamming = {}
        for layer,v in channels.items():
            combs = list(itertools.combinations(range(len(v.keys())), 2)) 
            ss = list(v.keys())
            for pair in combs:
                comb = [ss[pair[0]], ss[pair[1]]] 
                key = '+'.join(comb)
                hamming[key] = {} if key not in list(hamming.keys()) else hamming[key]
                hamming[key][layer] = distance.hamming(v[comb[0]], v[comb[1]])
        
        width = 0.3
        starts = [-width,0,width]
        for i,(k,v) in enumerate(hamming.items()):
            layers = v.keys()
            ind = np.arange(len(layers))
            heights = v.values()
            axes.bar(ind + starts[i], heights, width=width, label=k)
        
        axes.set_title('Hamming Distance between channels pruned for {:.2f}% pruning'.format(int(self.prunePerc)))
        axes.set_xticks(ind)
        axes.set_xticklabels(layers, rotation=45, ha='right')
        axes.set_ylabel('Hamming')
        axes.legend()
    #}}}
    
    def plot_num_pruned(self, axes):
    #{{{
        channels = {}

        for layer in self.layerNames:
            channels[layer] = {ss : self.pivotDict[ss]['grad']['module.'+layer] for ss in self.subsets}
        
        numPruned = {}
        for layer,v in channels.items():
            combs = list(itertools.combinations(range(len(v.keys())), 2)) 
            ss = list(v.keys())
            for key in ss:
                numPruned[key] = {} if key not in list(numPruned.keys()) else numPruned[key]
                numPruned[key][layer] = np.count_nonzero(v[key]) 
        
        width = 0.3
        starts = [-width,0,width]
        for i,(k,v) in enumerate(numPruned.items()):
            layers = v.keys()
            ind = np.arange(len(layers))
            heights = v.values()
            axes.bar(ind + starts[i], heights, width=width, label=k)
        
        axes.set_title('Num channels pruned per layer for {:.2f}% pruning'.format(int(self.prunePerc)))
        axes.set_xticks(ind)
        axes.set_xticklabels(layers, rotation=45, ha='right')
        axes.set_ylabel('Number of Channels Pruned')
        axes.legend()
    #}}}
#}}}

class RetrainPlotter(object):
#{{{
    def __init__(self):
        self.accGopData = {
            'Inference GOps':[],
            'Finetune Train Accuracy':[],'Finetune Val Accuracy':[], 'Finetune Test Accuracy':[], 
            'Retrain Train Accuracy':[], 'Retrain Val Accuracy':[], 'Retrain Test Accuracy':[]
        }  
        self.fig, self.axis = plt.subplots(1,1,figsize=(10,5))

    @staticmethod
    def get_best_acc(logCsv, fromEpoch=0):
    #{{{
        log = pd.read_csv(logCsv, delimiter=',\t', engine='python')
        test = log['Test_Top1'].dropna()
        val = log['Val_Top1'].dropna()
        train = log['Train_Top1'].dropna()

        bestValIdx = val[fromEpoch:].idxmax()
        
        return (train[bestValIdx], val[bestValIdx], test[bestValIdx])
    #}}}

    # tfg : total forward gops
    # bestRand : best test accuracy for random initalisation
    # bestFt : best test accuracy for finetuning
    def update_stats(self, tfg, bestRand, bestFt):
    #{{{
        self.accGopData['Inference GOps'].append(tfg)
        self.accGopData['Finetune Train Accuracy'].append(bestFt[0])
        self.accGopData['Finetune Val Accuracy'].append(bestFt[1])
        self.accGopData['Finetune Test Accuracy'].append(bestFt[2])
        self.accGopData['Retrain Train Accuracy'].append(bestRand[0])
        self.accGopData['Retrain Val Accuracy'].append(bestRand[1])
        self.accGopData['Retrain Test Accuracy'].append(bestRand[2])
    #}}}

    def plot(self, title, logFile=None, save=False):
    #{{{
        accGopData = pd.DataFrame(self.accGopData)
        
        accGopData.plot(x='Inference GOps', y='Finetune Train Accuracy', ax=self.axis, kind='scatter', color='r', label='Finetune_Train', marker=".")
        accGopData.plot(x='Inference GOps', y='Retrain Train Accuracy', ax=self.axis, kind='scatter', color='b', label='Retrain_Train', marker=".")
        
        accGopData.plot(x='Inference GOps', y='Finetune Val Accuracy', ax=self.axis, kind='scatter', color='r', label='Finetune_Val', marker="+")
        accGopData.plot(x='Inference GOps', y='Retrain Val Accuracy', ax=self.axis, kind='scatter', color='b', label='Retrain_Val', marker="+")
        
        accGopData.plot(x='Inference GOps', y='Finetune Test Accuracy', ax=self.axis, kind='scatter', color='r', label='Finetune_Test', marker="x")
        accGopData.plot(x='Inference GOps', y='Retrain Test Accuracy', ax=self.axis, kind='scatter', color='b', label='Retrain_Test', marker="x")
        
        plt.title(title)
        plt.ylabel('Best Accuracy (%)')
        plt.legend()
        plt.tight_layout()
        
        if logFile is not None:
            split = logFile.lower().split('/')
            folder = '/'.join(split[:-1])
            figName = logFile.lower()
        else:
            folder = '/home/ar4414/remote_copy/tmp/'
            figName = os.path.join(folder, 'recent.png')
        
        if save:
            cmd = 'mkdir -p {}'.format(folder)
            subprocess.check_call(cmd, shell=True)
            print('Saving - {}'.format(figName))
            plt.savefig(figName, format='png') 
        else:
            plt.show()
    #}}}
#}}}
