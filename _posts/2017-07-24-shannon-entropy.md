---
layout: post
title:  "Shannon's Entropy: A Matter of Surprise"
date:   2017-07-26 00:35:37 +0200
excerpt: "Some intuition about Shannon's Entropy."
visible: 0
comments: true
---

# Introduction

The word and the concept of **entropy** might be familiar to you. It originally came from physics and is usually associated to 
disorder, chaos, randomness, unpredictability. It was introduced in 1865 with the theory of thermodynamics but was revisited in 1948 by [Claude Shannon][shannon]. 
{: .text-justify}


Entropy is at the **root** of Shannon's [Information Theory][it]. You might never have heard of Information Theory but you use it every day!! Indeed, among others: 

- It provides the mathematical tools for [Data Compression][DC] such as, in practice: *zip*, *jpeg*, *mp3*, *mp4* methods. Huge internet infrastructures such as YouTube or 
Facebook use them extensively to store data.
- It's as the source of [Error Correcting Codes][ECC] that make possible the communication of data with possible loss on the way. Internet's efficiency deeply depends on it as its communication channels are highly unreliable.
{: .text-justify}

The goal of this post is principally to give you an **intuition** about what entropy is in Shannon's theory. The first part is purely informal and requires no particular background. Then we present a minimal formalization that leads to the construction of Shannon's entropy. This second part uses notions in analysis and probability theory.
{: .text-justify}

[shannon]: https://en.wikipedia.org/wiki/Claude_Shannon
[it]: https://en.wikipedia.org/wiki/Information_theory
[DC]: https://en.wikipedia.org/wiki/Data_compression
[ECC]: https://en.wikipedia.org/wiki/Error_detection_and_correction

# Weather Forecasting : An Intuitive Approach to Entropy

**The notion of surprisal.**  Let's say you give me the following forecast for tomorrow's weather:

<div class="imgcap">
<div>
<img src="/assets/H/forecast.png" style=" height:200px;">
</div>
<div class="thecap">Weather forecast for tomorrow : it's very likely to be sunny</div>
</div>
<br/>
That is, it's 99% likely to be sunny and only 1% likely to be rainy.   
Tomorrow when I wake up, there're two possible outcomes:

- It's *sunny*: well I'm not that **surprised**, you told me so.
- It's *rainy*: I'm very **surprised**!!! You told me it was only 1% likely :(

If we want to generalize this concept of **surprisal** we have that:

- An event which occurs with *high* probability should have a *low* surprisal, in our example it's the *sunny* outcome.
- An event which occurs with *low* probability should have a *high* surprisal, in our example it's the *rainy* outcome.    

<br/>
**Information and entropy.** What has it to do with **information** ? Surprise is a way to quantify information. If the outcome of a situation surprises me, I say 
it gives me more information than if it went as I predicted.    

What has it to do with **entropy** ? As it is definied in Shannon's theory, entropy is the average surprisal among the possible outcomes of 
a phenomenon. It measures my **lack of information** about the phenomenon or said differently, it's **uncertainty**. 

A subtlety is that this average is weighted by the probabilty of each outome. In our example, the *rainy* outcome would give me high surprisal, but weighted by the 
fact that is has 1% chance to occurs it becomes smaller. The other outcome, *sunny*, would give me a very low surprisal and I enforce it by the 
fact it happens 99% of the time. Overall, given your forecast, my average surprisal which is the **entropy** of the *weather* phenomenon, is very low. There's not a lot of uncertainty about tomorrow's weather.

So which weather forecast would lead to a higher entropy ?  As intuition might whisper it to our ears, the **equiprobable** forecast :
<div class="imgcap">
<div>
<img src="/assets/H/forecast_equi.png" style=" height:200px;">
</div>
<div class="thecap">An equiprobable weather forecast : it has high entropy</div>
</div>
<br/>

In that setting, the *weather* phenomenon becomes a lot more **uncertain**! With this forecast I would be really less inclined to plan an activity which entirely depends 
on having a *sunny* weather. It matches with our informal definition of entropy, each outcome's surprisal is medium but enforced by 
a relatively high probability to happen, it leads to a higher entropy than the previous situation.

It turns out that, in Shannon's formalism, it has **maximal entropy**!

**Formalization.**
