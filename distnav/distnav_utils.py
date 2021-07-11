import numpy as np
from numba import jit, prange


@jit(nopython=True, cache=False)
def init_config(num_agents):
    sub_table = np.zeros((num_agents, num_agents - 1), dtype=np.int32)
    for i in range(num_agents):
        for j in range(num_agents):
            if i < j:
                sub_table[i][j - 1] = j
            elif i > j:
                sub_table[i][j] = j
            else:
                continue
    return sub_table

@jit(nopython=True, parallel=True, cache=False)
def generate_expect_table(samples_x, samples_y, num_pts, num_agents,
                          pred_len, collision_likelihood):
    table = np.zeros((num_agents * num_pts, num_agents * num_pts))

    for i in prange(num_agents * num_pts):
        for j in prange(num_agents * num_pts):
            f1_x = samples_x[i]
            f1_y = samples_y[i]
            f2_x = samples_x[j]
            f2_y = samples_y[j]
            table[i][j] = collision_likelihood(f1_x, f1_y, f2_x, f2_y, pred_len)

    return table

@jit(nopython=True, cache=False, parallel=True)
def one_iteration(weights, table, sub_table, host_id, num_pts, num_agents):
    new_weights = weights.copy()

    for i in prange(num_pts):
        ev = 0.
        for j in prange(num_pts):
            for k in prange(num_agents - 1):
                client_id = sub_table[host_id][k]
                ev += table[host_id * num_pts + i][client_id * num_pts + j] * \
                      new_weights[client_id][j]
        ev /= num_pts
        new_weights[host_id][i] *= np.exp(-ev)

    new_weights[host_id] /= np.sum(new_weights[host_id]) / num_pts
    return new_weights.copy()

@jit(nopython=True, cache=False, parallel=True)
def objective(table, weights, num_agents, num_pts):
    val = 0.
    for i in prange(num_agents):
        for j in prange(i + 1, num_agents):
            for k in prange(num_pts):
                val += table[i * num_pts + k][j * num_pts + k] * weights[i][k] * weights[j][k]
    val /= num_pts ** 2
    return val
