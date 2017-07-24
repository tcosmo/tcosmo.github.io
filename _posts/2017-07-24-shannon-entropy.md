---
layout: post
title:  "Shannon's Entropy: A Matter of Surprisal"
excerpt: "Some intuition about Shannon's Entropy."
visible: 0
comments: true
---

# Introduction

[TODO: context]

# The Surprisal Function

**Weather Forecast.** Let's say you give me the following forecast for tomorrow's weather:

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
      
**Formalization.**
