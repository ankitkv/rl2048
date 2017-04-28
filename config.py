import argparse
import random
import numpy as np


parser = argparse.ArgumentParser()

parser.add_argument('--pretraining_steps', type=int, default=10**5)
parser.add_argument('--exp_buffer_size', type=int, default=10**6)
parser.add_argument('--seed', type=int, default=None)
parser.add_argument('--hidden_units', type=int, default=512)
parser.add_argument('--cuda', type=bool, default=False)
parser.add_argument('--batch_size', type=int, default=32)
parser.add_argument('--max_steps', type=int, default=10**6)
parser.add_argument('--start_random', type=float, default=1.0)
parser.add_argument('--end_random', type=float, default=0.1)
parser.add_argument('--random_anneal_steps', type=int, default=10**6)
parser.add_argument('--gamma', type=float, default=0.99)
parser.add_argument('--update_every', type=int, default=1000)


def get_config():
    conf = parser.parse_args()

    conf.action_map = {
        0: 'left',
        1: 'right',
        2: 'up',
        3: 'down',
    }

    random.seed(conf.seed)
    np.random.seed(conf.seed)

    return conf
