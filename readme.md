<h1>Multithreading to Find Primes</h1>
<h2>Kyle Bejel</h2>
<br>
<h3>Execution & Instructions</h3>
<p>Python makes it very easy to run files, simply use the command:</p>
```
python primes.py
```
<p>the output will be located in /output/primes.txt</p>
<h3>Assinment Documentation & Reflection</h3>
<p>For my assignment, I have decided to use the python programming language and have implemented a sieve to make the finding of prime numbers possible within a realistic span of time. I have used 8 threads running synchronously to make this happen most efficiently, spawning a thread on the second loop within the seive (when it is using numbers in the array to "cross out" their multiples) so that multiple numebrs are occuring at once. On reflection, I do not think I will use python again because, even though it is my preferred language, its execution time is rather slow no matter what and, upon further research after the completion of this project, I have learned that, while python supports multithreading and uses locks to synchronize them, it does not use the CPU to the greatest efficiency and thus does not help your execution time by much (my time personally went down from 19 seconds to around 15);just because something is possible doesnt mean you should do it. In the future, I will be using Java.</p>
<h3>Documentation</h3>
<p>I used to primary sources for the development of this project: the documentation for the threading python library and a wikipedia discussing the sieve (links below)</p>
<a>https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes</a>
<a>https://docs.python.org/3/library/threading.html</a>
