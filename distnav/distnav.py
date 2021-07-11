import numpy as np
np.seterr(divide='ignore', invalid='ignore')

from numba import jit
from .distnav_utils import *


class distnav:
    def __init__(self, collision_likelihood, samples_x, samples_y, origin_logpdf,
                 predict_len, num_agents, num_samples):
        self.collision_likelihood = collision_likelihood
        self.samples_x = samples_x.copy()
        self.samples_y = samples_y.copy()
        self.origin_logpdf = origin_logpdf.copy()
        self.predict_len = predict_len
        self.num_agents = num_agents
        self.num_samples = num_samples

        self.weights = np.ones((self.num_agents, self.num_samples), dtype=np.float32)

    def prepare(self):
        self.sub_table = init_config(self.num_agents)
        self.table = generate_expect_table(self.samples_x, self.samples_y,
                                      self.num_samples, self.num_agents,
                                      self.predict_len, self.collision_likelihood)
        print('preparation finished.')

    def reset_weights(self):
        self.weights = np.ones((self.num_agents, self.num_samples), dtype=np.float32)

    def optimize(self, thred, max_iter, return_log):
        obj = 0.
        it = 0
        while True:
            obj = objective(self.table, self.weights, self.num_agents, self.num_samples)
            if obj < thred or it >= max_iter:
                print('optimization terminated at iteration [{}] with objective: {}'.format(it, obj))
                break

            for pid in range(self.num_agents):
                new_weights = one_iteration(self.weights, self.table, self.sub_table, pid,
                                            self.num_samples, self.num_agents)
                self.weights = new_weights.copy()

            it += 1

        ret_weights = self.weights.copy()
        ret_weights_log = np.log(ret_weights)
        ret_weights_log = np.nan_to_num(ret_weights_log, neginf=-np.min(self.origin_logpdf))

        self.reset_weights()
        if return_log:
            return ret_weights, ret_weights_log
        else:
            return ret_weights

