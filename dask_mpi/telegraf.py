import subprocess
import os


def parse_rank(rank):
    if rank == 0:
        # This is the scheduler node
        return "scheduler"
    elif rank == 1:
        # This is the benchmarking node
        return "caller"
    else:
        # This is a worker node
        return "worker-{}".format(rank)


def exec_telegraf(rank):
    node_str = parse_rank(rank)
    # Set the environment variable of the Dask node name (for telegraf)
    os.environ['DASKNODE'] = node_str

    home_dir = os.environ['HOME']
    telegraf_path = os.path.join(home_dir, 'telegraf/bin/telegraf')

    # Run telegraf
    telegraf_proc = subprocess.Popen(telegraf_path, shell=True)

    return telegraf_proc
