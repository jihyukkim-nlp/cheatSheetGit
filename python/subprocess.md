``` #system_call #sys #subprocess ```
~~~
import subprocess
# move command
bashCommand = "mv a.out aa.out"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
~~~
