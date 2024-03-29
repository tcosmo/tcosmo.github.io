---
layout: post
title:  "Differentiating Primes"
excerpt: "What happens if you iterate the discrete differenciation operator on the sequence of primes numbers ?"
visible: 1
date: jeu. janv. 18 16:13:46 CET 2018
comments: true
---

* TOC
{:toc}

## Warning

Note that all the the experimental results shown in this post might be biased by numerical errors. They all need to be checkproofed. You can find the base python code that generated them here: [Code](/assets/primes/diff_primes.py).

## Introduction
<p>
We play the following game. You are given a finite sequence of numbers and the goal is to predict which is the next one.     
For instance let's say we take:

<center>
0, 1, 4, 9, 16, 25, ?
</center>
<br/>
If you are familiar with maths you would certainly come up with 36.   <br/>  
If not here's a way we could proceed: through iterated differentiations.    
The idea is the following, we substract each term to the following one and do it again on the new sequence. Here we get:  <br/>   
<center>
<br/>
0, 1, 4, 9, 16, 25<br/>
1, 3, 5, 7, 9<br/>
2, 2, 2, 2<br/>      
0, 0, 0<br/>
0, 0<br/>
0     
</center> <br/>
From this pyramidal construction we can make the probable hypothesis that the third line will always be constant, equal to 2 and propagate 
from there in order to decide the next term in the first line:   
<center>
<br/>
0, 1, 4, 9, 16, 25, <span style="color:red">36</span><br/>
1, 3, 5, 7, 9, <span style="color:red">11</span><br/>
2, 2, 2, 2, <span style="color:red">2</span><br/>         
</center> <br/>

Which is consistent with the first mathematical guess that was based on the recognition of the sequence of squares:   
<center>
<br/>
$ U_n = n^2 $
</center>
<br/>
Formally, our method through differentiation was to repeatedly construct $V_n = U_{n+1}-U_n$ and setting $U=V$ at each stage. Even more formally have constructed a sequence of sequence $W$ such that:    

<center>
<br/>
$W^0 = U$ <br/>
and <br/>
$W^{k+1}_{n} = W^{k}_{n+1}-W^{k}_{n} = D(W^k)$
<br/>
</center>      


With $D$ the differentiation operator on sequences.       <br/><br/>
Since we have only a finite number of elements of $U$ -- the sequence from which we want to guess the next element -- note that we "loose" one term at each iteration of the differentitation and thus have a pyramidal structure in the end. <br/>
</p>
<br/>
<p>
In this example we were lucky because we could guess the next number even without using this method of differentiation. This is because the sequence of squares is well known. To enforce the idea that this method can be generalized let's apply it on the following $U$:
<center>
13, 10, 5, 4, 13, 38, ?
</center>
<br/>

We get:
<center>
<br/>
$W^0:$ 13, 10, 5, 4, 13, 38<br/>
$W^1:$ -3, -5, -1, 9, 25<br/>
$W^2:$ -2, 4, 10, 16<br/>      
$W^3:$ 6, 6, 6<br/>
$W^4:$ 0, 0<br/>
$W^5:$ 0     
</center> <br/>

By progration we guess the next number:
<center>
<br/>
$W^0:$ 13, 10, 5, 4, 13, 38, <span style="color:red">85</span><br/>
$W^1:$ -3, -5, -1, 9, 25, <span style="color:red">47</span><br/>
$W^2:$ -2, 4, 10, 16, <span style="color:red">22</span><br/>
$W^3:$ 6, 6, 6, <span style="color:red">6</span>    
</center> <br/>


Which is consistent with the fact that the underlying formula we chose to generate this sequence was:     
<center>
    <br/>
$ U_n = n^3 - 4n^2 + 13$
</center>
<br/>
Which would have been way harder to recognize than $U_n=n^2$!
</p>

<br/><br/>
Ok so this method of differentation gave us a tool in order to predict the underlying structure of our example sequences.       
When thinking of interger sequences there is one of which structure is very mysterious, **primes numbers**:
<center>
$(p_n):$ 2, 3, 5, 7, 11, ...
<br/>
<br/>
</center>  
Why not doing the same, that is taking $W^0 = (p_n)$ and see what happens ? However, we're not going to do it by hand but program it. Here's what we obtain:



<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/primes.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of the primes below $10^4$</div>
</div>
<br/>
</center>
 
This video was made by successively plotting for each $k$, $n \mapsto W^{k}_{n}$.       <br/><br/>
Isn't it **super strange** ?    <br/><br/>
This blog post aims at compiling experiments around this iterated differentitation idea and at making a formal link with cellular automata, we do not proove nor conjecture anything.    
We found very little literature on the subject, please **feel free to add some in the comment sections if these plots ring you a bell**.
<br/><br/>
# Experiments
## Pertubing primes
The first question that came to our mind after seeing the video shown in introduction was: is this phenomenon characteristic of prime numbers ?    
Without any experiments we can already say: **no**. Because translating primes by a constant, for instance $p'_n=p_n+53$, won't perturbate the differentations. However, this pertubation is quite straightforward and not very harmful on the structure of primes. Let's pertubate them quite a lot.
We add to each prime below $10^4$ a different random number between $-1000$ and $1000$ and sort the obtained sequence. We take this as our $W^0$. Here's what we obtain:
<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/primes2.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of sorted primes below $10^4$ with random pertubations</div>
</div>
<br/>
</center>
Which is a quite similar behavior!    
<br/>
Ok so, this fancy shapes are certainly not specific to primes.
<br/>
In this pertubation spirit let's try something even harder: we similarly add random numbers to each primes but **do not sort** the sequence after this operation. That is that $W^0$ is not increasing at all and has random fluctuations. Here's what we get:
<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/primes3.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of unsorted primes below $10^4$ with random pertubations</div>
</div>
<br/>
</center>
Again, these shapes.<br/>
Ok so for which other sequence should we have these shapes ?
## Taking $nln(n)$
The theorem of primes number claims that $(p_n) \sim nln(n)$ so it would be natural to see this kind of behaviors with $W^0_n = nln(n)$.   
It gives:
<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/nln.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of $W^0_n = nln(n)$</div>
</div>
<br/>
</center>
To stay with integers only, what happens with $W^0_n = \text{int}(nln(n))$ ? The following:
<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/nlnent.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of $W^0_n = \text{int}(nln(n))$</div>
</div>
<br/>
</center>
The behavior seems really more geometric at least for earlier derivatives (low $k$).
## Taking $ntan(n)$
We thought of $nln(n)$ because it was somehow related to primes. What if we take something that does not look especially related ?
For instance $W^0_n = ntan(n)$.
<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/ntan.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of $W^0_n = ntan(n)$</div>
</div>
<br/>
</center>
<!-- back to polynomes -->
<!-- disclaimer order of magnitudes float error ? -->
<!-- cellular automata, symmetrized rule -->
## Back to primes: from order to chaos ?
Let's try something weird on our primes. Let's take: $$ W^0_n = p_{p_n} $$, the sequence of primes indexed by primes. 
In order to have enough data, we extend $p_n$ to be all the primes below $10^5$. It gives:
<center>
<div class="imgcap">
    <video width="70%" controls>
      <source type="video/mp4" src="/assets/primes/videos/chaos.mp4">
      Your browser does not support the video tag.
    </video>
    <div class="thecap">Iterated differentiations of $W^0_n = p_{p_n}$</div>
</div>
<br/>
</center>

At the begining everything seems "as usual". But suddenly it breaks and it looks very chaotic...