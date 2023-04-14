# version beta

```shell
git checkout -b nqtr-tool
git checkout nqtr-tool
git config pull.rebase false
git pull https://github.com/DRincs-Productions/DS-toolkit.git tool-only --allow-unrelated-histories

```

## Migrations

Use search and replace of vscode with regex functionality enabled

![image](https://user-images.githubusercontent.com/67595890/224504331-1f546922-5673-4fa9-8cc7-e3fc4e671305.png)

### updateFlags

* `updateFlags\((.*)\)`
* `update_flags($1)`

### getFlags

* `getFlags\((.*)\)`
* `get_flags($1)`

### setFlags

* `setFlags\((.*)\)`
* `set_flags($1)`

### notifyEx

* `notifyEx\((.*)\)`
* `notify_add($1)`

### notifyExPreventsLoops

* `notifyExPreventsLoops\((.*)\)`
* `notify_prevents_loops($1)`

### notifyExClean

* `notifyExClean\((.*)\)`
* `notify_remove($1)`


### GENDER_TYPE

* `GENDER_TYPE`
* `GenderEnum`
