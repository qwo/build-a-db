---
title: How Does a Database Work? In [C]
weight: 20
---

-- *Based on the material from [CStack's write a SQlit3 clone scratch](https://cstack.github.io/db_tutorial/)

Makefile in `content/code/Makefile`


` make all arg1=content/using_c/code/part1.c ` for example to run part 1

`make all arg1=content/using_c/code/db.c` for finished example

- What format is data saved in? (in memory and on disk)
- When does it move from memory to disk?
- Why can there only be one primary key per table?
- How does rolling back a transaction work?
- How are indexes formatted?
- When and how does a full table scan happen?
- What format is a prepared statement saved in?

In short, how does a database **work**?

I'm building a clone of [sqlite](https://www.sqlite.org/arch.html) from scratch in C in order to understand, and I'm going to document my process as I go.


> "What I cannot create, I do not understand." -- [Richard Feynman](https://en.m.wikiquote.org/wiki/Richard_Feynman)

<img src="/assets/images/arch2.gif" description="sqlite architecture (https://www.sqlite.org/arch.html)" />