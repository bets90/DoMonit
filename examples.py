#!/usr/bin/env python
from __future__ import division

from domonit.containers import Containers
from domonit.ids import Ids
from domonit.inspect import Inspect
from domonit.logs import Logs
from domonit.process import Process
from domonit.changes import Changes
from domonit.stats import Stats

c = Containers()
i = Ids()

print ("Number of containers is : %s " % (sum(1 for i in i.ids())))

if __name__ == "__main__":

    for c_id in i.ids():

        ins = Inspect(c_id)
        sta = Stats(c_id)
        proc = Process(c_id, ps_args = "aux")

        # Container name
        print ("\n#Container name")
        #print ins.name()
        print c.names(c_id)

        # Container id
        print ("\n#Container id")
        print ins.id()

        # Memory usage
        mem_u = sta.memory_stats_usage()

        # Memory limit
        mem_l = sta.memory_stats_limit()

        # Memory usage %
        print ("\n#Memory usage %")
        print  int(mem_u)*100/int(mem_l)

        # CPU stats

        # CPU Delta
        cpu_delta = int(sta.cpu_stats_total_usage()) - int(sta.precpu_total_usage())

        # systemDelta
        system_delta = int(sta.cpu_stats_system_cpu_usage()) - int(sta.precpu_system_cpu_usage())

        # number of cores
        usage_per_core = sta.cpu_stats_percpu_usage().strip('[]')
        number_of_cores = len(usage_per_core.split(','))

        print ("\n#CPU percentage")
        print number_of_cores * ((cpu_delta/system_delta)*100)

        # The number of times that a process of the cgroup triggered a "major fault"
        print ("\n#The number of times that a process of the cgroup triggered a major fault")
        print sta.memory_stats_stats_fault()


        # Same output as ps aux in *nix
        print("\n#Same output as ps aux in *nix")
        print proc.ps()



