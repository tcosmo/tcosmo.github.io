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
        """
            Construction of a zero-filled SOM.
            h,w,dim_feat: constructs a (h,w,dim_feat) SOM.
        """
        self.shape = (h,w,dim_feat)
        self.som = np.zeros((h,w,dim_feat))
```

<br/>

**Note on the code.** We construct the code iteratively, the blocks you see are the cells of this [notebook].
We use the [jdc][jdc] `%%add_to` (see [\[4\]](#ref)) magic command in order to construct the SOM class step by step. If you're not familiar with notebooks
just consider each of the blocks commencing by `%%add_to SOM` as updates we do on the class `SOM` methods.

The entire final code is to be found [HERE].

When a function appears on several blocks such as the `__init__` function like [here](#b1) or [here](#b2) it means it has been updated from one block to the other.
Otherwise function calls always refer to the most recent definition of it.



<br/>
### What are we going to do with SOMs ?

We are going to **train** them!! 

<a name="bef"></a>
The idea of a SOM is to feed it with **d** dimensional data and let it update 
it's feature vectors in order to match this data. Furthermore, we want it to group nearby on the lattice data which are 
originally nearby in the **d**-dimensional space. This will be done by spreading information in **neighbourhoods**.

<br/>
#### Finding the BMU
At each time step t of the training, we are going to present to the SOM a randomly chosen input vector of our data. Then,
we find the cell having the closest (norm L2 speaking) feature vector to that input vector. We call this cell the Best Matching Unit (**BMU**).

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

$$ V_{t+1} = V_{t} + L(t)*(D_{t}-V_{t})\label{eq:bmu}$$

$$L(t)$$ is called the *learning rate* and depends on time t. Remark that if $$L(t) = 1$$, we directly replace our feature vector by the 
input vector. It's the kind of behavior that we would like to see at the begining of the training but if we want the SOM to "stabilize" 
we'll need to decrease L(t) over time. That's exactly why we define:

$$ L(t) = L_0*e^{-\frac{t}{\lambda}} \label{eq:L}$$

With $$L_0$$ the initial learning rate and $$\lambda$$ a time scaling constant.

Let implements these new ideas:

<a name="b1"></a>
```python
%%add_to SOM
def __init__(self,h,w,dim_feat):
    """
        Construction of a zero-filled SOM.
        h,w,dim_feat: constructs a (h,w,dim_feat) SOM.
    """
    self.shape = (h,w,dim_feat)
    self.som = np.zeros((h,w,dim_feat))
    
    # Training parameters
    self.L0 = 0.0
    self.lam = 0.0
    
def train(self,data,L0,lam):
    """ 
        Training procedure for a SOM.
        data: a N*d matrix, N the number of examples, 
              d the same as dim_feat=self.shape[2].
        L0,lam: training parameters.
    """
    self.L0 = L0
    self.lam = lam
    
    for t in itertools.count():
        i_data =  np.random.choice(range(len(data)))
        
        bmu = self.find_bmu(data[i_data])
        self.update_bmu(bmu,data[i_data],t)
            
        
def update_bmu(self,bmu,input_vector,t):
    """
        Update rule for the BMU.
        bmu: (y,x) BMU's coordinates.
        input_vector: current data vector.
        t: current time.
    """
    self.som[bmu] += self.L(t)*(input_vector-self.som[bmu])

def L(self, t):
    """
        Learning rate formula.
        t: current time.
    """
    return self.L0*np.exp(-t/self.lam) 
```

<br/>
#### Updating the rest of the SOM

As suggested [before](#bef), we are going to communicate the BMU's update to its **neighbourhood**.
This will lead on having close feature vectors on close cells. That's why we can see SOMs as a clustering method: 
it groups together similar information.

Let's have $W_t$ the feature vector of a cell $\boldsymbol c = (x,y)$, different than the BMU $\boldsymbol c_{0} = (x_0,y_0)$. 
We are going to update it as below:

$$ W_{t+1} = W_{t} + N(\delta,t)*L(t)*(D_{t}-W_{t})\label{eq:non_bmu}$$

With $N(\delta,t)$ the *neighbouring penalty* depending on $\delta = \|\| \boldsymbol c - \boldsymbol c_{0}\|\|_{2}$, the distance
between that cell and the BMU, and $t$ the current time.

Indeed, we would like farest cells ($\delta$ high) to be less affected by the BMU's update. Also, we would like this update to be 
more and more localized near the BMU over time. As for the learning rate, we want the SOM to "stabilize" over time.

It leads to the following formulation for $N(\delta,t)$:

$$ N(\delta,t) = e^{-\frac{\delta^2}{2\sigma(t)^2}}$$

Which is a spatial *Gaussian decay* scaled by radius factor $\sigma(t)$.
For the reasons we just mentionned, we want $\sigma(t)$ to get smaller over time so that the "influence area" of the BMU shrinks.
We'll do that in the exact same way as equation $\ref{eq:L}$. It gives:

$$ \sigma(t) = \sigma_0 * e^{-\frac{t}{\lambda}}$$

We use the same time scaling $\lambda$ parameter for both $L$ and $\sigma$.

By looking at the update equations $\ref{eq:bmu}$ and $\ref{eq:non_bmu}$ for the BMU cell and non-BMU cells we can notice that the only thing 
that differs is the $N(\delta,t)$ term. Furthermore, from the BMU to itself $\delta=0$ and gives $N(\delta,t)=1$ which exactly give equation $\ref{eq:bmu}$.
Thus we can use equation $\ref{eq:non_bmu}$ as a unique update rule for all cells, BMU and non-BMUs.

Let implements all that:

<a name="b2"></a>
```python
%%add_to SOM
def __init__(self,h,w,dim_feat):
    """
        Construction of a zero-filled SOM.
        h,w,dim_feat: constructs a (h,w,dim_feat) SOM.
    """
    self.shape = (h,w,dim_feat)
    self.som = np.zeros((h,w,dim_feat))
    
    # Training parameters
    self.L0 = 0.0
    self.lam = 0.0
    self.sigma0 = 0.0
    
def train(self,data,L0,lam,sigma0):
    """ 
        Training procedure for a SOM.
        data: a N*d matrix, N the number of examples, 
              d the same as dim_feat=self.shape[2].
        L0,lam,sigma0: training parameters.
    """
    self.L0 = L0
    self.lam = lam
    self.sigma0 = sigma0
    
    for t in itertools.count():
        i_data =  np.random.choice(range(len(data)))
        
        bmu = self.find_bmu(data[i_data])
        self.update_som(bmu,data[i_data],t)

            
def update_som(self,bmu,input_vector,t):
    """ 
        Calls the update rule on each cell.
        bmu: (y,x) BMU's coordinates.
        input_vector: current data vector.
        t: current time.
    """
    for y in range(self.shape[0]):
        for x in range(self.shape[1]):
            dist_to_bmu = np.linalg.norm((np.array(bmu)-np.array((y,x))))
            self.update_cell((y,x),dist_to_bmu,input_vector,t)

def update_cell(self,cell,dist_to_bmu,input_vector,t):
    """ 
        Computes the update rule on a cell.
        cell: (y,x) cell's coordinates.
        dist_to_bmu: L2 distance from cell to bmu.
        input_vector: current data vector.
        t: current time.
    """
    self.som[cell] += self.N(dist_to_bmu,t)*self.L(t)*(input_vector-self.som[cell])

def N(self,dist_to_bmu,t):
    """ 
        Computes the neighbouring penalty.
        dist_to_bmu: L2 distance to bmu.
        t: current time.
    """
    curr_sigma = self.sigma(t)
    return np.exp(-(dist_to_bmu**2)/(2*curr_sigma**2))

def sigma(self, t):
    """
        Neighbouring radius formula.
        t: current time.
    """
    return self.sigma0*np.exp(-t/self.lam) 
```


<br/>
#### How to initialize, how to stop ?

Two things we have left behind are the begining and the ending of the training procedure. 
For the moment we start with a full zero SOM and our `train` method is an infinite loop.

TODOTODO :)z)oz)àz)à

<a name="ref"></a>
## References
[kohonen]:http://www.scholarpedia.org/article/Kohonen_network
[bibl]:http://cis.legacy.ics.tkk.fi/research/som-bibl/vol1_4.pdf
[aijunkie]: http://www.ai-junkie.com/ann/som/som1.html

[jdc]: https://github.com/alexhagen/jdc

\[1\]: http://www.scholarpedia.org/article/Kohonen_network      
\[2\]: http://cis.legacy.ics.tkk.fi/research/som-bibl/vol1_4.pdf      
\[3\]: http://www.ai-junkie.com/ann/som/som1.html   
\[4\]: https://github.com/alexhagen/jdc   