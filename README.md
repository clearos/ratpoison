# ratpoison

Forked version of ratpoison with ClearOS changes applied

## Update usage
  Add __#kojibuild__ to commit message to automatically build

* git clone git+ssh://git@github.com/clearos/ratpoison.git
* cd ratpoison
* git checkout f12
* git remote add upstream git://pkgs.fedoraproject.org/ratpoison.git
* git pull upstream f12
* git checkout clear7
* git merge --no-commit f12
* git commit
