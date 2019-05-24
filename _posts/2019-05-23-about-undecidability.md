---
layout: post
title:  "About Undecidability in Logic"
date:   2019-05-23 18:49:37 +0100
excerpt: "Demystifying the concept of undecidability through monoïds and groups."
visible: 1
comments: true
---

The concept of undecidability in logic is often seen as something mysterious or even mystical: a statement (on natural numbers for instance) could be true, false or... undecidable. The goals of this post is to ground the notion of undecidability on earth and to show that it is in fact a very natural concept. We will illustrate the concept of undecidability on a very rudimentary system of axioms: [Monoïds](https://en.wikipedia.org/wiki/Monoid).

We hope that after reading this post, the reader will be convinced that undecidability is not an alternative to truth (a statement is either true or false in a given model) but that undecidability is just a mirror of the weakness of a system of axioms.

A big part of the mystery surrounding undecidability maybe comes from the fact that it plays a major role in Gödel incompletness theorems and that these theorems are often seen as mystical, infinitely deep results. Gödel incompletness theorems are not our subject today but we will, at the end of this post, give a brief description of how they relate to the concept of undecidability.

The take-home message of this blog post is:

<p style="text-align: center;">
Undecidability is a property of a logical statement with respect to a set of axioms. 
</p>

# Monoïds

Monoïds are objects containing elements which can interact with each others thanks to a composition law. Take two elements $x,y$ of a monoïd $\mathcal{M}$, you can construct $z=x\cdot y$, an other element of $\mathcal{M}$, which is called the *composition* of $x$ and $y$. A monoïd also has a special element denoted by $e$ called "neutral". 

To be a monoïd, $\mathcal{M}$ must verify the two following axioms:

1. $ \forall x,y,z \quad x\cdot(y\cdot z) = (x\cdot y )\cdot z $
2. $ \forall x \quad x\cdot e = e\cdot x = x $

The first axiom specifies that parenthesis don't matter when you are composing elements with each others, $x\cdot(y\cdot z) = (x\cdot y )\cdot z = x\cdot y \cdot z$ while the second one justifies why $e$ is called "neutral": composing an element $x$ with $e$ wont affect $x$.

The definition of monoïds is very abstract. As a consequence, loads of different objects are monoïds. For instance, the set of natural numbers is a monoïd! Take $\mathbb{N}=\{0,1\dots,\}$ and use addition as the composition law and 0 to be the neutral element. Then you will satisfy both axiom 1 and 2:

1. $\forall x,y,z \in \mathbb{N} \quad x+(y+z) = (x+y)+z = x + y + z$
2. $\forall x \in \mathbb{N} \quad x + 0 = 0 + x = x$

Weirder objects are monoïds. Consider $\mathcal{A}$, the set of words you can make with the letters "a" and "b". You can make:

1. The empty word $\epsilon$ (you write nothing)
2. The word "a"
3. The word "ab"
4. The word "aba"
5. etc...

The composition operation becomes string concatenation : $\text{abba}\cdot \text{aab} = \text{abbaaab}$.

This object $\mathcal{A}$ together with the law $\cdot$ meets all the requirement to be a monoïd, indeed, the neutral element is the empty word, for instance: $\text{aaab}\cdot \epsilon = \text{aaab}$ (concatenating with nothing does not change the string) and parenthesis don't matter while concatenating. However this object looks different from the first monoïd we saw, the set of natural numbers $\mathbb{N}$!

In other words, the very minimal set of axioms that monoïds satisfy allow to construct a wide variety of different looking objects. This set of axiom has an important expressive power because it can shape such different objects.

Undecidability will arise from the fact that some of these objects will have properties that the others don't have.

# Groups

Let's consider the following statement, called the "inverse property":

$$ \forall x\, \exists y\,\,\,\, x\cdot y = y\cdot x = e$$

The element $y$ is called the "inverse" of $x$.

The question that arises is: "is this statement verified by all monoïds" ?

The answer is NO! Indeed, the two examples of monoïds we gave don't have that property:

1. Take any strictly positive $x\in\mathbb{N}$, there is no element of $y\in\mathbb{N}$ such that $x+y=0$
2. Take a non empty string like "aabaa", there is no string you can concatenate to it in order to get back to the empty string "\epsilon".

However, some monoïds do have the "inverse property"! For instance, in the set of negative and positive integers $\mathbb{Z}$ we have:

$$ \forall x \in \mathbb{Z} \quad x + (-x) = 0 $$

Monoïds which have the "inverse property" are called [Groups](https://en.wikipedia.org/wiki/Group_(mathematics)).

What we just saw is that any group is a monoïd but not all monoïds are groups!

For that reason, the sentence $ \forall x\, \exists y\,\, x\cdot y = y\cdot x = e$ is **undecidable** under the axioms of monoïds. The axioms of monoïds are not *strong enough* to enforce this property in all the objects that satisfy the monoïds axioms.

Finally, keep in mind that in a given model of the axioms of monoïds (a model is an object satisfying the axioms), the "inverse property", as any property, is either true or false.

# Wrapping Up

From the Monoïd VS Groups example, we understand that undecidability is a very natural concept. A sentence is undecidable with respect to a system of axioms if not all models of these axioms verify it. Said otherwise, a property is undecidable with respect to a system of axioms when this system of axioms is **too weak** to logically imply this property. From the axioms of monoïds you cannot logically deduce the inverse property!

Undecidability outlines the degrees of freedom that a system of axioms gives you. An undecidable property can live in harmony (i.e. without causing any logical contradiction) with the system of axioms as well as the negation of that property: we are free to have either.

Undecidability is not at all an alternative to being true or false, it is a property of a logical sentence with respect to a given system of axioms. In a specific model of these axioms, a property is always either true or false. However, if the property is undecidable, we will find models of the axioms where the property is true and models where the property is false.

On a side remark, note that characterizing all the objects that satisfy a system of axioms is not an easy task. Consider the axioms of groups (axioms of monoïds + the inverse property). It has been a major task of 20th century mathematics to only describe the finite models of groups axioms (called finite groups). This description resulted in a theorem called the [Monster Theorem](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups) of which proof is ten thousands of pages long.

# Link With Gödel ?

Gödel theorems deal with a specific set of axioms: the axioms of arithmetic, called [Peano Axioms](https://en.wikipedia.org/wiki/Peano_axioms). These axioms formalize the concept of numbers and the operations that we are used to do on them: addition and multiplication.

These theorems construct an undecidable property in the axioms of arithmetic. It was easy for us to outline an undecidable property when looking at monoïds but it is much more tricky when looking at arithmetic. More powerfully, Gödel incompletness theorems show that you will always be able to construct undecidable properties in systems of axioms which "embeds" arithmetic.

In other word, if you have a system of axioms which allows you to do something as elementary as counting, you will be able to construct undecidable properties with respect to this system of axioms. 