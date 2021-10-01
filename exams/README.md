# Written examinations (with keys)

In this page it is possible to find the link to the various written examination of the course Computational Thinking and Programming, academic year 2020/2021.


## 20 September 2021 written examination

**Text of the exam:** [PDF](./written-examination-2021-09-20.pdf)

**Solutions:**
* Section 1 (theory):
  1. greedy
     
     backtracking
     
  2. `if position == value_to_search` should be `if item == value_to_search`, and `return item` should be `return position`
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-22) available online.
  
  4. We can distinguish three macro-sets of programming languages:
     * machine language is a set of instructions that can be executed directly by the central processing unit (CPU) of an electronic computer;
     * low-level programming languages are languages that provide one abstraction level on top of the machine language and allow one to write programs in a way that is more intelligible to humans;
     * high-level programming languages are languages which are characterised by a strong abstraction from the specifiability of the machine language, and they may use natural language words for specific constructs, to be easy to use and to understand by humans.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-25) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-25) available online.


## 7 July 2021 written examination

**Text of the exam:** [PDF](./written-examination-2021-07-07.pdf)

**Solutions:**
* Section 1 (theory):
  1. A queue is a countable sequence of ordered and repeatable elements.
     
     A dictionary is a countable collection of unordered key-value pairs, where the key is non- repeatable in the dictionary.
     
  2. The second `return 0` should be `return 1`, and `fib_dc(n-3)` should be `fib_dc(n-2)`
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-21) available online.
  
  4. Backtracking in an algorithic technique that tries to find a solution to a particular computational problem by identifying possible candidate solutions incrementally. It abandons partial candidates once it is clear that they will not be able to provide a solution to the problem. At each step of the execution, a backtracking algorithm considers a particular node of the tree of choices as input, that is addressed according to one of the following steps:
     * [leaf-win] if the current node is a leaf, and it represents a solution to the problem, then return the sequence of all the moves that have generated the successful situation; otherwise,
     * [leaf-lose] if the current node is a leaf, but it is not a solution to the problem, then return no solution to the parent node; otherwise,
     * [recursive-step] apply the whole approach recursively for each child of the current node, until one of these recursive executions returns a solution. If none of them provides a solution, return no solution to the parent node of the current one.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-24) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-24) available online.


## 14 June 2021 written examination

**Text of the exam:** [PDF](./written-examination-2021-06-14.pdf)

**Solutions:**
* Section 1 (theory):
  1. The three main kinds of programming languages are machine language, low-level programming languages, and high-level programming languages
  
     The Turing machine can simulate any algorithm
     
  2. [Solution](https://comp-think.github.io/exercises/understanding/beginner/exercise-12) available online.
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-20) available online.
  
  4. A recursive function is a function defined in terms of itself (i.e. it calls itself in its body). It is used as an alternative to iteration when a solution to a particular computational problem depends on the partial solutions of smaller instances of the same problem. In particular, a recursive function has one or more basic cases and at least one recursive step. Each basic case describes a terminating scenario and does not use any recursion to produce the answer to a specific (sub-)problem. Instead, the recursion step is where the same algorithm is executed again with a different (and, usually, reduced) input.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-23) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-23) available online.


## 17 May 2021 written examination

**Text of the exam:** [PDF](./written-examination-2021-05-17.pdf)

**Solutions:**
* Section 1 (theory):
  1. In Python, a list is a mutable object, The recursive-step is one of the main step of backtracking
     
  2. [Solution](https://comp-think.github.io/exercises/understanding/beginner/exercise-11) available online.
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-19) available online.
  
  4. There are two characteristics that a computational problem should show to be sure that the application of a greedy approach will bring to an optimal solution to the problem:
     * greedy choice property – at a particular step, we can choose the best candidate for improving the set of candidates bringing to a solution;
     * optimal substructure – the optimal solution to a computational problem is built by considering the optimal solutions to its subproblems.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-22) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-22) available online.


## 15 March 2021 written examination

**Text of the exam:** [PDF](./written-examination-2021-03-15.pdf)

**Solutions:**
* Section 1 (theory):
  1. The Fibonacci number can be computed using a dynamic programming approach, The Fibonacci number can be computed using a non-recursive approach
     
  2. `input_list_len == 0` should be `input_list_len <= 1`, `left = merge_sort(input_list[input_list_len:mid])` should be `left = merge_sort(input_list[0:mid])`
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-18) available online.
  
  4. Charles Babbage developed two machines: the Difference Engine and the Analytical Engine. The Difference Engine was a mechanical calculator which aimed at addressing similar tasks that were run by human computers, but in a way that was automatic, faster, and error-free. The Difference Engine was not a programmable machine since it was able to compute only a fixed set of operations on the inputs specified physically by changing specific configurations of the machine. Instead, the Analytical Engine was a programmable machine since it enabled a user could create any possible procedural calculation.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-21) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-21) available online.


## 29 January 2021 written examination

**Text of the exam:** [PDF](./written-examination-2021-01-29.pdf)

**Solutions:**
* Section 1 (theory):
  1. divide and conquer, dynamic programming
     
  2. [Solution](https://comp-think.github.io/exercises/understanding/beginner/exercise-10) available online.
     
  3. [Solution](https://comp-think.github.io/exercises/development/beginner/exercise-17) available online.
  
  4. A Turing Machine is composed of an **infinite memory tape** containing cells. Each cell can contain a symbol (i.e. either 0 or 1, where 0 is the blank symbol, assigned to all the cells in advance) that can be read and written by the **head of the machine**. The **state of the machine at a specific time is recorded**. The machine specifies the possible actions to perform in a **finite table of instructions**. Each instruction in the table says what to do: write a new symbol, move the head either left or right, go to a new state. The machine selects a particular instruction to execute according to the current state and the symbol currently under the head. An **initial state and zero or more final states** are provided, to define where to start the process, and when to finish it.

* Section 2 (understanding): [Solution](https://comp-think.github.io/exercises/understanding/advanced/exercise-20) available online.

* Section 3 (development): [Solution](https://comp-think.github.io/exercises/development/advanced/exercise-20) available online.
