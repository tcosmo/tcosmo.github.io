---
layout: post
title:  "Having Fun with Self-Organizing Maps"
excerpt: "Implementing SOMs in Python."
visible: 0
date: 2017-07-27 17:46:31 +0200
comments: false
---

## Introduction

Self-Organizing Maps (**SOM**), or [Kohonen Networks][kohonen] ([\[1\]](#ref)), is a method for unsupervised clustering and visualization introduced in the 80' by computer scientist Teuvo 
Kohonen.

In this post we are going to present the basics of SOM model and build a minimal python implementation based on `numpy`. It leads to visualizations such as:

<center>
<div class="imgcap">
    <video width="50%" controls>
      <source type="video/mp4" src="/assets/soms/square.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">A SOM trained on square data</div>
</div>
</center>
<br/>

There is a huge litterature on SOMs (see [\[2\]](#ref)), theoretical and applied, this post only aims at having fun with this model over a tiny implementation.
The approach is very much inspired by this [post][aijunkie] ([\[3\]](#ref)).

<br/>
## What's a SOM ?

For the sake of simplicity we'll describe SOMs as being supported by a **h**\***w** set of 2D points that we call cells, regularly spaced in the plan, also called a *point lattice*.
We refer to them by assigning them coordinates, here top down in the spirit of `numpy` matrices.


<div class="imgcap">
    <div>
        <img width="45%" src="/assets/soms/point_lattice.png" alt="point lattice"/>
    </div>
    <div class="thecap">A point lattice, support of a (5,6)-shaped SOM</div>
</div>
<br/>

To each of these cells is associated a **feature vector** of dimension **d** (d is the same for all cells). 
In that setting a SOM is entirely described by a **h**\***w** matrix containing **d** dimensional vectors, that is a 
**(h,w,d)** tensor. 


We thus can construct a zero-initialized SOM with the following code:


```python
# jdc for step by step class construction
import jdc.jdc as jdc

import numpy as np
import itertools 

class SOM(object):
    def __init__(self,h,w,dim_feat):
        self.shape = (h,w,dim_feat)
        self.som = np.zeros((h,w,dim_feat))
```

**Note on the code.** We construct the code iteratively, what you see are the cells of this [notebook].
We use the [jdc][jdc] `%%add_to` magic command in order to construct the SOM class step by step.
The whole code is to be found [HERE].


<br/>
### What are we going to do with SOMs ?

We are going to **train** them!! 

The idea of a SOM is to feed it with **d** dimensional data and let it update 
it's feature vectors in order to match this data. Furthermore, we want it to group nearby on the lattice data which are 
originally nearby in the **d**-dimensional space. This will be done by spreading information in neighbourhoods.

<br/>
#### Finding the BMU
At each time step t of the training, we are going to present to the SOM a randomly chosen input vector of our data. Then,
we find the cell having the closest feature vector to that input vector. We call this cell the Best Matching Unit (**BMU**).

```python
%%add_to SOM
def train(self,data):
    """ 
        Training procedure for a SOM.
        data: a N*d matrix, N the number of examples, 
              d the same as dim_feat=self.shape[2].
    """
    for t in itertools.count():
        i_data =  np.random.choice(range(len(data)))
        bmu = self.find_bmu(data[i_data])
        
def find_bmu(self, input_vec):
    """
        Find the BMU of a given input vector.
        input_vec: a d=dim_feat=self.shape[2] input vector.
    """
    list_bmu = []
    for y in range(self.shape[0]):
        for x in range(self.shape[1]):
            dist = np.linalg.norm((input_vec-self.som[y,x]))
            list_bmu.append(((y,x),dist))
    list_bmu.sort(key=lambda x: x[1])
    return list_bmu[0][0]
```

<br/>

#### Updating the BMU
Now that we found the BMU, we want it's current feature vector $$V_t$$ to be closer to the inputed data vector at time t,
$$D_t$$. Here the update rule we are going to use:

$$ V_{t+1} = V_{t} + L(t)*(D_{t}-V_{t})$$

$$L(t)$$ is called the *learning rate* and depends on time t. Remark that if $$L(t) = 1$$, we directly replace our feature vector by the 
input vector. It's the kind of behavior that we would like to see at the begining of the training but if we want the SOM to "stabilize" 
we'll need to decrease L(t) over time. That's exactly why we define:

$$ L(t) = L_0*e^(-\frac{t}{\lambda})$$

With $$L_0$$ the initial learning rate and $$\lambda$$ a time scaling constant.


<a name="ref"></a>
## References
[kohonen]:http://www.scholarpedia.org/article/Kohonen_network
[bibl]:http://cis.legacy.ics.tkk.fi/research/som-bibl/vol1_4.pdf
[aijunkie]: http://www.ai-junkie.com/ann/som/som1.html

[jdc]: https://github.com/alexhagen/jdc

\[1\]: http://www.scholarpedia.org/article/Kohonen_network      
\[2\]: http://cis.legacy.ics.tkk.fi/research/som-bibl/vol1_4.pdf      
\[3\]: http://www.ai-junkie.com/ann/som/som1.html     
