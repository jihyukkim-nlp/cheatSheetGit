``` #system_call #sys #subprocess #bash #command #shell ```
~~~
import subprocess
# move command
bashCommand = "mv a.out aa.out"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
~~~
