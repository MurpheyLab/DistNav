# Introduction

This repository contains related code for the RSS 2021 [paper](http://www.roboticsproceedings.org/rss17/p053.pdf) "Move Beyond Trajectories: Distribution Space Coupling for Crowd Navigation" by Muchen Sun, Francesca Baldini, Pete Trautman and Todd Murphey.

If you use this toolbox, please cite it as below.

```
@INPROCEEDINGS{SunM-RSS-21, 
    AUTHOR    = {Muchen Sun AND Francesca Baldini AND Peter Trautman AND Todd Murphey}, 
    TITLE     = {{Move Beyond Trajectories: Distribution Space Coupling for Crowd Navigation}}, 
    BOOKTITLE = {Proceedings of Robotics: Science and Systems}, 
    YEAR      = {2021}, 
    ADDRESS   = {Virtual}, 
    MONTH     = {July}, 
    DOI       = {10.15607/RSS.2021.XVII.053} 
}
```

## `DistNav` Toolbox

You can install the crowd navigaton toolbox via `pip install distnav`. The second tutorial below contains examples for how to use this toolbox.

## Tutorials

We provide a Jupyter notebook tutorials for our algorithm. You can find them under the "notebooks" directory.
 - [Tutorial 1: distribution space coupling in one-dimensional space](./notebooks/distnav_1d_tutorial.ipynb): In the first tutorial, we will build from scratch on a one-dimensional two-agents toy example to show how DistNav optimization works. We will show both the analytical solution with numerical integration and approximated solution with sampling and Monte-Carlo integration, and how they can match with
   each other. You can find a copy of the notebook in Google Colaboratory [**here**](https://colab.research.google.com/github/MurpheyLab/DistNav/blob/master/notebooks/distnav_1d_tutorial.ipynb).
 - [Tutorial 2: distribution space coupling in high-dimensional space using `distnav` toolbox](./notebooks/distnav_traj_tutorial.ipynb): In the second tutorial, we will do distribution space coupling in high-dimensional spaces, to predict the preference distributions over long trajectories for four pedestrians (or robots) walk across each other. We show how to specify initial preference distributions using Gaussian processes regression and how to use our `distnav` toolbox to find optimal
   preferences via samples. You can find a copy of the notebook in Google Colaboratory [**here**](https://colab.research.google.com/github/MurpheyLab/DistNav/blob/master/notebooks/distnav_traj_tutorial.ipynb).

## Questions?

Feel free to contact Muchen Sun via `muchen@u.northwestern.edu` for any question :)

