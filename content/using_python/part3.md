---
title: Part 3 - An In-Memory, Append-Only, Single-Table Database
weight: 3
---

We're going to start small by putting a lot of limitations on our database. For now, it will:

- support two operations: inserting a row and printing all rows
- reside only in memory (no persistence to disk)
- support a single, hard-coded table

Our hard-coded table is going to store users and look like this:

| column   | type         |
|----------|--------------|
| id       | integer      |
| username | varchar(32)  |
| email    | varchar(255) |

This is a simple schema, but it gets us to support multiple data types and multiple sizes of text data types.

`insert` statements are now going to look like this:

```
insert 1 cstack foo@bar.com
```
`./part3.py` 
also accepts CLI `python ./part3.py` 

 With those changes we can actually save data in our database!
```command-line
~ ./db
db >
$insert 1 cstack foo@bar.com
Executed.
db >
$insert 2 bob bob@example.com
Executed.
db > select
$(1, cstack, foo@bar.com)
$(2, bob, bob@example.com)
Executed.
db > 
$insert foo bar 1
Syntax error. Could not parse statement.
db > .exit
~
```

{{< code title="part3.py" file="/content/using_python/code/part3.py" language="python" >}}






