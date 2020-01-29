import os
import configparser as cp
import subprocess
import sys

nets = ['resnet', 'mobilenetv2', 'alexnet', 'squeezenet']
pruningPercs = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]
subset = ['subset1', 'aquatic']
sub_classes = ["large_man-made_outdoor_things large_natural_outdoor_scenes vehicles_1 vehicles_2 trees small_mammals people", "aquatic_mammals fish"]
batchSize = []
ftBudget = []
lrSchedule = []
config = cp.ConfigParser()

configPath = '/home/ar4414/pytorch_training/src/ar4414/pruning/configs/l1_prune'
runFileBase = '/home/ar4414/pytorch_training/src/ar4414/pruning/scripts_conf_logs/'
cpRoot = "/home/ar4414/pytorch_training/src/ar4414/pruning/logs/{}/cifar100/{}/v1_l1_prune"

cmd = 'mkdir -p ' + configPath
subprocess.check_call(cmd, shell=True)

for netCount, net in enumerate(nets):
    testCount = 0
    configFile = '/home/ar4414/pytorch_training/src/ar4414/pruning/configs/' + str(net) + '.ini'
    config.read(configFile)
            
    repeats = 5
    gpu = "0" if (net == 'mobilenetv2' or net == 'resnet') else "1"
    runFile = os.path.join(runFileBase, 'run_{}.sh'.format(gpu))
    
    config['training_hyperparameters']['print_only'] = "False"
    
    config['pytorch_parameters']['gpu_id'] = gpu
    config['pytorch_parameters']['resume'] = "False"
    config['pytorch_parameters']['branch'] = "False"
    config['pytorch_parameters']['evaluate'] = "False"
    
    config['pruning_hyperparameters']['get_gops'] = "False"
    config['pruning_hyperparameters']['inference_gops'] = "False"
    config['pruning_hyperparameters']['change_in_rank'] = "False"
    
    config['pruning_hyperparameters']['prune_filters'] = "True"
    config['pruning_hyperparameters']['finetune'] = "True"
    config['pruning_hyperparameters']['static'] = "True"
    config['pruning_hyperparameters']['retrain'] = "False"
    config['pruning_hyperparameters']['finetune_budget'] = "30"
    config['pruning_hyperparameters']['prune_after'] = "5"

    for ssCount, ss in enumerate(subset):
        config['pruning_hyperparameters']['sub_name'] = ss
        config['pruning_hyperparameters']['sub_classes'] = sub_classes[ssCount]
        config['pytorch_parameters']['checkpoint_path'] = cpRoot.format(net, ss) 

        for ppCount, pp in enumerate(pruningPercs):
            config['pruning_hyperparameters']['pruning_perc'] = str(pp)
            config['pytorch_parameters']['test_name'] = 'pp_{}'.format(pp)

            testConfig = os.path.join(configPath, str(net) + '_' + str(testCount) + '.ini')
            with open(testConfig, 'w+') as tcFile:
                config.write(tcFile)
            
            with open(runFile, 'a+') as rFile:
                for i in range(repeats):
                    rFile.write('python main.py --config-file ' + testConfig + '\n')
            
            testCount += 1





