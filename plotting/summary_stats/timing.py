import os
import sys
import glob
import json
import math

import configparser as cp

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def get_raw_times(prof_logs):
#{{{
    breakpoint()
#}}}

def plot_inf_gops_vs_acc(summaryData, subsetAgnosticSummaryData, saveLoc=None):
#{{{
    xAxis = 'InferenceGops'
    yAxis = 'AvgTestAcc'

    subsets = set(list(summaryData['Dataset']))
    networks = set(list(summaryData['Network']))
    #plt.subplots returns fig,ax
    axes = {net:{subset:plt.subplots(1,1) for subset in subsets} for net in networks} 

    for (dataset, net), data in summaryData.groupby(['Dataset', 'Network']):
        title = 'Top1 Test Accuracy (%) for {} on {}'.format(net.capitalize(), dataset.capitalize()) 
        label = 'Subset Aware Pruning'
        
        ax = data.plot.scatter(x=xAxis, y=yAxis, ax=axes[net][dataset][1], label=label, title=title)
        
        ax.set_xlabel('Inference GOps')
        ax.set_ylabel('Test Accuracy (%)')
    
    for (subset, net), data in subsetAgnosticSummaryData.groupby(['Subset', 'Network']):
        for count, (pp, points) in enumerate(data.groupby(['PrunePerc'])):
            labels = ['Subset Agnostic Unpruned', 'Subset Agnostic Pruning', '']
            labelIdx = 0 if pp == "0" else 1 if count == 1 else 2
            marker = 'x' if pp == "0" else '+'
            
            axes[net][subset][1].plot([float(points['InferenceGops'])], [float(points['TestAcc'])], label=labels[labelIdx], marker=marker, markersize=4, color='red', linestyle="None")
            axes[net][subset][1].legend()

    if saveLoc is not None:
        for net,plots in axes.items(): 
            for subset,plot in plots.items(): 
                plt.tight_layout()
                figFile = os.path.join(saveLoc, '{}_{}.png'.format(net, subset))
                plot[0].savefig(figFile)
#}}}

def plot_ft_gops_vs_acc(summaryData):
#{{{
    axAccs = [plt.subplots(1,1)[1] for i in range(3)] #subplots returns fig,ax tuple
    xAxis = 'FinetuneGops'
    yAxis = 'AvgTestAcc'

    for (dataset, net), data in summaryData.groupby(['Dataset', 'Network']):
        colour = 'red' if 'mobilenetv2' in net else 'blue'
        title = 'Top1 Test Accuracy (%) for {} on Subset-{}'.format(net, dataset.capitalize()) 
        
        if 'entire_dataset' in dataset:
            ax = data.plot.scatter(x=xAxis, y=yAxis, ax=axAccs[0], c=colour, label=net, title=title)
        elif 'subset1' in dataset:
            ax = data.plot.scatter(x=xAxis, y=yAxis, ax=axAccs[1], c=colour, label=net, title=title)
        elif 'aquatic' in dataset:
            ax = data.plot.scatter(x=xAxis, y=yAxis, ax=axAccs[2], c=colour, label=net, title=title)
        
        ax.set_xlabel('Finetune GOps')
        ax.set_ylabel('Test Accuracy (%)')
#}}}

def plot_ft_gops_by_epoch(data, plotAsLine=None, _accMetric='Test_Top1'):
#{{{
    nets = list(data.keys())
    subsets = list(data[nets[0]].keys()) 
    prunePercs = list(data[nets[0]][subsets[0]].keys())

    colours = cm.rainbow(np.linspace(0,1,len(prunePercs))) 
    accMetric = _accMetric
    xAxis = 'Ft_Gops'
    lab = '{}-%'

    linePlots = ['25', '50', '75', '95'] if plotAsLine is None else plotAsLine

    for net in nets: 
        for subset in subsets:
            for i,pp in enumerate(prunePercs): 
                df = data[net][subset][pp]
                colour = [colours[i]]*len(df)
                
                if i == 0:
                    ax = df.plot(x=xAxis, y=accMetric, color=colour, label=lab.format(pp), title='{} vs Finetune Gops \n Network-{} on Subset-{}'.format(accMetric, net.capitalize(), subset.capitalize()))
                    ax.set_xlabel('Finetune Gops')
                    ax.set_ylabel(accMetric)
                else:
                    if pp in linePlots:
                        df.plot(x=xAxis, y=accMetric, ax=ax, color=colour, label=lab.format(pp))
                    
                    ax.plot([df[xAxis][len(df)-1]], [df[accMetric][len(df)-1]], marker="o", markersize=4, color='red')
                    ax.set_xlabel('Finetune Gops')
                    ax.set_ylabel(accMetric)
#}}}

