#!/usr/bin/env bash


### Head: init #################################################################
#
THE_BASE_DIR_PATH=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
THE_BASE_DIR_PATH="$THE_BASE_DIR_PATH/../../../../ext"
source "$THE_BASE_DIR_PATH/init.sh"
#
### Tail: init #################################################################


### Head: main #################################################################
#
fcitx_chewing_conf_set_main () {
	util_run_sub_module_function 'fcitx_chewing' 'conf_set' 'fcitx_chewing_conf_set'
}


fcitx_chewing_conf_set_main
#
### Tail: main #################################################################
