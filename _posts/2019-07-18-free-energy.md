---
layout: post
title:  "About Free Energy"
date:   2019-07-18 12:10:37 +0100
excerpt: "Free energy minimization and the Boltzmann distribution from a mathematical perspective."
visible: 0
comments: true
---

## Introduction

Free energy is a concept which seem to be central in statistical physics, thermodynamics, chemistry and physical biology. For instance, practical results such that [the law of mass action](https://en.wikipedia.org/wiki/Law_of_mass_action) can be derived from the principle of free energy minimization. 

However, how to develop an intuition about the following textbook definition of free energy:

$$ G = E - T S $$

Where:
- $E$ is the energy (sometimes enthalpy $H$ is used instead of $E$)
- $T$ the temperature    
- $S$ the entropy

To begin with, this expression of $G$ seems to be ill-typed because "energy" and "entropy" are not properties of the same kind of objects. Said differently, $E$ is the energy of what ? $S$ is the entropy of what ? Indeed, as presented in our [article on entropy]({% post_url 2017-07-24-shannon-entropy %}), entropy is a property of a **probability distribution** (or a random variable) while the energy $E$ seems to be the property of a **state** of a physical system. So how can we make sense of the expression of $G$ when $E$ and $S$ seem to be about very different things?

In this article, we answer that question by presenting a formalism of free energy with random variables. We'll rewrite $G$ as being the property of an **energetic random variable** $X$. We will write:

$$ G(X) = \mathbb{E}[X] - \tau H(X)$$

Where: 
- $\mathbb{E}[X]$ is the expectation of $X$   
- $\tau$ is a non-negative parameter called the ''threshold''
- $H(X)$ is the [Shannon entropy]({% post_url 2017-07-24-shannon-entropy %}) of $X$ (not to be mistaken with some enthalpy $H$)

We consciently drop the term of "temperature" for "threshold" because, in this mathematical model we don't deal with units and physical scales. 

Thanks to this formulation we'll get some intuition on what minimizing $G(X)$ means: finding the best compromise between stability (being in a low energy state) and "chaos" which is the natural ability of a system to explore all its possible states. With the theory of optimization we will be able to show that the probability distribution of $X$ which minimizes $G$ corresponds exactly to the [Boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution). Hence, with this formalism, the principle of free energy minimization directly leads to the Boltzmann distribution and justifies why, in statistical physics, the probability for a system to be at a level of energy $E_i$ is given by:

$$ p_i = \frac{1}{Z}e^{-\frac{E_i}{k_B T}}$$

Finally, throughout the article, we'll use  and illustrate this formalism on a concrete toy example of 1D hybridization of two particles.