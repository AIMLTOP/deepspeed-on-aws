# Microsoft DeepSpeed on AWS

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 447341124968.dkr.ecr.us-east-1.amazonaws.com
docker build -t deepspeed-sm-base . -f Dockerfile-Base
docker tag deepspeed-sm-base:latest 447341124968.dkr.ecr.us-east-1.amazonaws.com/deepspeed-sm-base:latest
docker push 447341124968.dkr.ecr.us-east-1.amazonaws.com/deepspeed-sm-base:latest



# Issues
[2021-06-03 01:41:20,343] [INFO] [runner.py:358:main] cmd = mpirun -n 2 -hostfile /opt/ml/input/config/hostfile --mca btl ^openib --mca btl_tcp_if_include eth0 --allow-run-as-root --display-map --tag-output -x UCX_TLS=tcp -x PYTHONUNBUFFERED=1 -x PYTHONIOENCODING=UTF-8 -x PYTHON_VERSION=3 -x PYTHONDONTWRITEBYTECODE=1 -x NCCL_VERSION=2.8.3 -x NCCL_SOCKET_IFNAME=eth0 -x NCCL_IB_DISABLE=1 -x NCCL_DEBUG=DEBUG -x PYTHONPATH=/opt/ml/code:/opt/ml/code:/opt/conda/bin:/opt/conda/lib/python36.zip:/opt/conda/lib/python3.6:/opt/conda/lib/python3.6/lib-dynload:/opt/conda/lib/python3.6/site-packages /opt/conda/bin/python3.6 -u /opt/ml/code/train_cifar10.py --deepspeed-flag --config-file=/opt/ml/code/cifar_ds_config.json
ssh: connect to host algo-2 port 22: Connection refused
--------------------------------------------------------------------------
ORTE was unable to reliably start one or more daemons.
This usually is caused by:

* not finding the required libraries and/or binaries on
one or more nodes. Please check your PATH and LD_LIBRARY_PATH
settings, or configure OMPI with --enable-orterun-prefix-by-default

* lack of authority to execute on one or more specified nodes.
Please verify your allocation and authorities.

* the inability to write startup files into /tmp (--tmpdir/orte_tmpdir_base).
Please check with your sys admin to determine the correct location to use.

*  compilation of the orted with dynamic libraries when static are required
(e.g., on Cray). Please check your configure cmd line and consider using
one of the contrib/platform definitions for your system type.

* an inability to create a connection back to mpirun due to a
lack of common network interfaces and/or no route found between
them. Please check network connectivity (including firewalls
and network routing requirements).
  

