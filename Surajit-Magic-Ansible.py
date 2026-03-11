#Code to redirect ansible console o/p from stdout

#!/usr/bin/python

import sys
from prettytable import PrettyTable
import json
import os
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager as Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from collections import namedtuple

from io import BytesIO as StringIO
from contextlib import contextmanager
@contextmanager
def stdout_redirector(stream,streame):
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = stream
    sys.stderr = streame
    try:
        yield
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

myOutputStream = StringIO()
myErrorStream = StringIO()

def create_vnf(inventory_path,playbook_path,logger,conf_file=None,status_script=None,status_output=None,slot_id=None,local_path=None,local_db_file_name=None,update_blade_config_script=None,local_am_build_name=None,local_rm_build_name=None,upgrade_script=None):
    loader = DataLoader()
    inventory = Inventory(loader=loader, sources=inventory_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    playbook_path = playbook_path
    Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check', 'diff'])


    options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='root', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method='sudo', become_user='root', verbosity=3, check=False, diff=False)
    
        variable_manager.extra_vars = {'config_file': conf_file,'show_status_script': status_script,'output_file_name': status_output,'slot_id':slot_id,'local_path':local_path,'local_db_file_name':local_db_file_name,'local_am_build_name': local_am_build_name,'update_blade_config_script':update_blade_config_script,'local_rm_build_name':local_rm_build_name,'upgrade_script':upgrade_script}
    passwords = {}

    pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory,options=options, variable_manager=variable_manager, loader=loader, passwords=passwords)
    results=""
    with stdout_redirector(myOutputStream,myErrorStream):
        results = pbex.run()
    run_success = True
    stats = pbex._tqm._stats
    value = sorted(stats.processed.keys())
    for h in value:
        t = stats.summarize(h)
        if t['unreachable'] > 0 or t['failures'] > 0:
            run_success = False
    return run_success
