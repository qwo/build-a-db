---
title: Part 4 - Our First Tests (and Bugs)
weight: 4
---

We've got the ability to insert rows into our database and to print out all rows. Let's take a moment to test what we've got so far.

I'm going to use [rspec](http://rspec.info/) to write my tests because I'm familiar with it, and the syntax is fairly readable.

I'll define a short helper to send a list of commands to our database program then make assertions about the output:

`rspec ../../../tests/part4.rb`

{{< code title="part4.rb" file="/../../../tests/part4.rb" language="python" >}}
{{< code title="part4.py" file="/content/using_python/code/part4.py" language="python" >}}






