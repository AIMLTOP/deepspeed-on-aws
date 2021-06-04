



work1 ssh 172.31.90.89
work2 ssh 172.31.88.251


cat > /opt/ml/input/config/hostfile <<EOF
ip-172-31-90-89.ec2.internal slots=1
ip-172-31-88-251.ec2.internal slots=1
EOF

cat /opt/ml/input/config/hostfile

/opt/conda/bin/deepspeed --hostfile=/opt/ml/input/config/hostfile --launcher=openmpi --launcher_args='--allow-run-as-root --display-map --tag-output' --master_addr=ip-172-31-90-89.ec2.internal --master_port=55555 /opt/ml/code/train_cifar10.py --deepspeed-flag --config-file=/opt/ml/code/cifar_ds_config.json

/opt/conda/bin/deepspeed --hostfile=/opt/ml/input/config/hostfile --launcher=openmpi --launcher_args='--allow-run-as-root --display-map --tag-output' --master_addr=ip-172-31-88-251.ec2.internal --master_port=55555 /opt/ml/code/train_cifar10.py --deepspeed-flag --config-file=/opt/ml/code/cifar_ds_config.json
