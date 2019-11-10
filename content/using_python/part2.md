---
title: Part 2 - World's Simplest SQL Compiler and Virtual Machine
weight: 2
---

We're making a clone of sqlite. The "front-end" of sqlite is a SQL compiler that parses a string and outputs an internal representation called bytecode.

See full explaination in C section.

`./part2.py` 
also accepts CLI `python ./part2.py` 

```
db > 
$ foo
Unrecognized command 'foo'.


db > 
$ select
This is where we would do a select.

Executed.

db > 
$ insert
This is  where we would do an insert.

Executed.

$ .exit
```

{{< code title="part2.py" file="/content/using_python/code/part2.py" language="python" >}}






