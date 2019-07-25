---
layout: post
title:  "About Free Energy"
date:   2019-07-18 12:10:37 +0100
excerpt: "Free energy minimization and the Boltzmann distribution from a mathematical perspective."
visible: 0
comments: true
---

## Introduction

Free energy is a concept which seems to be central in statistical physics, thermodynamics, chemistry and physical biology. For instance, practical results such that [the law of mass action](https://en.wikipedia.org/wiki/Law_of_mass_action) can be derived from the principle of free energy minimization. 

However, how can we develop an intuition about the following textbook definition of free energy:

$$ G = E - T S $$

Where:
- $E$ is the energy (sometimes enthalpy $H$ is used instead of $E$)
- $T$ the temperature    
- $S$ the entropy

To begin with, this expression of $G$ seems to be ill-typed because "energy" and "entropy" are not properties of the same kind of objects. Said differently, $E$ is the energy of what ? $S$ is the entropy of what ? Indeed, as presented in our [article on entropy]({% post_url 2017-07-24-shannon-entropy %}), entropy is a property of a **probability distribution** (or a random variable) while the energy $E$ seems to be the property of a **state** of a physical system. So how can we make sense of the expression of $G$ when $E$ and $S$ seem to be about very different things?

In this article, we answer that question by presenting a formalism of free energy with random variables. We'll rewrite $G$ as being the property of a system **state random variable** $X$ together with an **energetic valuation function** $v$. We will write:

$$ G(X,v) = \mathbb{E}[v(X)] - \tau H(X)$$

Where: 
- $X$ is the random variable indicating in which state (microstate) our system is currently in
- $v:\Omega \to \mathbb{R}$ is a function indicating what is the energy of a given state $s\in\Omega$ ($\Omega$ is the set of all states)
- $\mathbb{E}[v(X)]$ is the expectation of $v(X)$, i.e. the average energy of the system with valuation $v$   
- $\tau$ is a non-negative parameter called the ''threshold''
- $H(X)$ is the [Shannon entropy]({% post_url 2017-07-24-shannon-entropy %}) of $X$ (not to be mistaken with some enthalpy $H$)

We consciently drop the term of "temperature" for "threshold" because, in this mathematical model we don't deal with units and physical scales. 

Thanks to this formulation we'll get some intuition on what minimizing $G(X)$ means: finding the best compromise between stability (being in a low energy state) and "chaos" which is the natural ability of a system to explore all its possible states. With the theory of optimization we will be able to show that the probability distribution of $X$ which minimizes $G$ corresponds exactly to the [Boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution). Hence, with this formalism, the principle of free energy minimization directly leads to the Boltzmann distribution and justifies why, in statistical physics, the probability for a system to be at a level of energy $E_i$ is given by:

$$ p_i = \frac{1}{Z}e^{-\frac{E_i}{k_B T}}$$

Finally, throughout the article, we'll illustrate this formalism on a concrete toy example of 1D hybridization of two particles.

## Toy Model of Hybridization

### 1D Two Particles World

<div class="imgcap" style="border: 0px">
<div>
<img src="/assets/free_energy/world.svg">
</div>
<div class="thecap">Figure 1. Three of the $N^2 + N$ states of the 1D two particles world of size $N=5$.<br/> The two particles can possibly bound if they are on the same cell.</div>
</div>
<br/>

Our toy model of hybridization is as follows: we take two identical particles living in a 1D, disrcete, world composed of $N$ cells. These two particles can freely move to any cell of the world, in particular they can both be on the same cell (Figure 1, first and second rows). When they are on the same cell these two particles can "hybridize", i.e. make a bound between themselves (Figure 1, third row).

### Micro and Macro States

As shown in Figure 2, this system can be in $N^2+N$ states which we call **microstates**:

<div class="imgcap" style="border: 0px">
<div>
<img src="/assets/free_energy/world2.svg" style="width:70%">
</div>
<div class="thecap">Figure 2. The $N^2 + N$ microstates of the system and its two macrostates: bonded or not bonded.</div>
</div>
<br/>

These $N^2 + N$ microstates can be grouped in two distincts **macrostates** according to whether or not there is a bond between the molecules or not. Macrostates are collections of microstates sharing a common property. Here we have two macrostates: **bonded** and **not bonded**.

### Our System as a Random Variable

Let $X$ be the random variable indicating in which microstate the system is. The set of all microstates, $\Omega = \\{ S_1, \ldots, S_{N^2 + N} \\}$, is given in Figure 2. Formally, $X$ is the identity on $\Omega \to \Omega$.

The question we ask is: **"What is the probability to be in a given microstate ?"**. Equivalently: what is the distribution $p_X$ of the state variable $X$?

In order to answer this question we introduce the concept of *energy of a state $S_i$*.

## Free Energy or the Fight Between Energy and Entropy
### Some States are more Steady than Others

We are going to look at each of our microstate $S_i$ and evaluate how *stable* or *favorable* this state is. Formally, we are going to construct an energetic valuation function $v:\Omega \to \mathbb{R}$ by defining $v(S_i)$ for $1 \leq i \leq N+N^2$. 

The intution about energy can be found in the following metaphore: it is more stable for a screw to be screwed tight than to be left loose on the table. By convention, the screwed state, which is more stable, will be considered as a **low energy state** while the un-screwed state will be considered as **high energy**. Energies are values in $\mathbb{R}$ so, maybe counterintuitively, they can be negative. The more negative the energy of a state, the more stable the stable.

In our 1D world, any microstate where the two particles are **bonded** will be considered as having a lower energy -- i.e, being more stable because the two particles are "screwed" together -- than any microstate where they are **not bonded**. Furthermore, in our model there is not reason to give a different energetic score to two microstates being in the same macrostate. Indeed, energetically speaking, nothing distinguishes microstates $1$ to $N^2$ (not bonded case) as well as nothing distinguishes microstates $N^2+1$ to $N^2+N$ (bonded case).

Hence we have:

$$ \begin{align*} v(S_1) &= v(S_2) = \dots v(S_N^2) = E_{\text{not bonded}} \\ v(S_{N+1}) &= v(S_{N+2}) = \dots v(S_{N^2+N}) = E_{\text{bonded}} \end{align*} $$

In the following we take $E_{\text{not bonded}} = 0$ as a reference energy. The value of $E_{\text{bonded}}$ (negative) will account for how intense is the bond between the two particles. For instance $E_{\text{bonded}} = -100$ will correspond to a situation where that bond is 10 time stronger than a scenario where $E_{\text{bonded}} = -10$.

### What is a Fair Distribution on Microstates?

Our goal is to have a way to construct $p_X = (p_1, \ldots, p_{N^2 + N})$ which is the probability distribution over microstates: $p_i$ is the probability that the system is in microstate $S_i$. In order to get there we must describe what is a *good* (or a fair) distribution over the microstates space.

For instance, is it fair if $p_X$ is uniform, i.e $p_i = \frac{1}{N^2 + N}$ ? No since, because of the **energetic** argument. Indeed, microstates corresponding to the **bonded** macrostate are more favorable. Hence, our distribution $p_X$ must be biased in favor of bonded microstates $S_{N^2 + 1} \dots S_{N^2 + N}$.

Inversely, is it fair if $p_X$ favors only one particular microstate? For instance if we set $p_{N^2+1} = 1$ ? No, because of the **entropic** argument. The entropic argument accounts for the chaotic nature of microscopic systems: molecular agitation drives the system to explore its different possible configurations. Molecular agitation limits our ability to predict in which microstate the system is. 

Gibbs free energy will provide an answer to achieving a good compromise between the energetic and the entorpic argument.

### Minimizing Gibbs Free Energy Gives the Fairest Distribution on Microstates

Gibbs (or Helmholtz) free energy is a mathematical formalisation of the intuitive idea of a fight between energy and entropy in microscopic systems. We define it as follows:

$$ G(X,v) = \mathbb{E}[v(X)] - \tau H(X)$$

With $\mathbb{E}[v(X)] = \sum_{i} v(S_i) p_i$, the weighted average energy, $\tau \geq 0$ a parameter called the *threshold* and $H(X)$ the [Shannon entropy]({% post_url 2017-07-24-shannon-entropy %}) of $X$. 

If we minimize $G(X,v)$, i.e. find the probability distribution $p_X$ which gives the smallest value of $G$, we achieve an interesting compromise. Indeed, we minimize the **weighted average energy** of the system while **maximizing** the corresponding entropy of the microstates distribution. Note that maximizing Shannon entropy matches the intuitive idea of the entropic argument since we maximize the **lack of predictability** of the random variable $X$ (see the [article]({% post_url 2017-07-24-shannon-entropy %})). On the other hand, minimizing the weighted average energy is a possible way to formalise the energetic argument.

The parameter $\tau$ allows us to linearly control the lack of predictability (or chaos) of the system. If $\tau = 0$, there is no chaos. Minimizing free energy will correspond to deterministically set the system to the most favorable states. If $\tau = +\infty$, the system is totally unpredictable: minimizing free energy will lead to the uniform distribution on microstates and the system is so unstable that the energetic argument does not hold anymore. In physics, the threshold $\tau$, up to the normalization constant $k_{B}$, corresponds to temperature. Temperature linearly controls the molecular agitation of the system which determines the ability of the system to explore its state space.

The free energy principle states that the probability distribution over the states of a microscopic system will be the one minimizing free energy. As we are going to see, this distribution is the **Boltzmann distribution**:

$$ p_i = \frac{1}{Z}e^{-\frac{v(S_i)}{\tau}} $$

With $Z= \sum_i{e^{-\frac{v(S_i)}{\tau}}}$ a normalization factor (sometimes called *partition function*).