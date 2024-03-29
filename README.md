# Build A DB 

Build a DB is an upgraded version of cstack's build-a-db in C project. Using the Hugo Theme for technical documentation.

https://cstack.github.io/db_tutorial/

Supported Languages
- C
- Python [In-progress]


## Features

* Modern, Simple layout
* Responsive web design
* Documentation menu (Select Menu style)

## Tests
* Uses RSPEC

Ubuntu 18.04+  - ` sudo apt install ruby-rspec-core` 

`rspec` 

## Tools
Use the below sed command to remove +/- diffs
`cat FILE1.c | sed -r "s/^([^-+ ]*)[-+ ]/\\1/" > FILE1_clean2.c `


## Deploy Site to public_html directory

```
hugo -t hugo-theme-techdoc -d public_html
```

## Development environment

```
hugo server --watch
```

## Contribution

### Patches and Bug Fixes

Small patches and bug reports can be submitted a issue tracker in Github. Forking on Github is another good way. You can send a pull request.

1. Fork 
2. Create a feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Create new Pull Request

## Changelog

Original Theme By

[thingsym](https://github.com/thingsym)

Copyright (c) 2017-2019 by thingsym


## Copyright
MIT 