Unanswered:

* Is there really a difference?

```

x = set(arr1)
[i for i in arr2 if not in x]
# and 
[i for i in arr2 if not in set(arr1)]

```

Stage 1: 

 * Data structure and algorithm 
    courses: 
    * [course 1](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)
    * [course 2](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/video_galleries/lecture-videos/) - until the random walk
    * [course 3  ](https://www.youtube.com/watch?v=8hly31xKli0)- freeCodeCamp.org

Helpful vids: 
* [link](https://www.youtube.com/c/eniolaa)
* clamp function: when you want to create a function that puts inputs in a range of min and max


Q : in doubly linked list when wanting to print curr. why does it blow up?

Q: How to make merge sort on linked lists efficient?

REVIEW: items in need of future attention!

--------------------------------
Subject: Prime number finding: 

It depends on whether we're looking at many big numbers or a few.

A few: looking into a list seems to be a good option.
Many: Maybe better to forget about the lists! cause not too many are available.

--------------------------------

Subject: comparing letters and words based on their order.

Use ord(letter) -> starts from ord('a') = 97

Example: find the maximum sum when comparing words with each other.

max(x.lower().split(), key = lambda word: sum(ord(l) - 96 for l in word))

--------------------------------

create an expression that can be interpreted into equation:

example: given three numbers try to come up with an expression that can output the max

max(max(eval(f'{a}{op1}({b}{op2}{c})'), eval(f'({a}{op1}{b}){op2}{c}')) for op1 in '+*' for op2 in '+*')



--------------------------------

To see if a number is '06':

two ways: str(int(num)) == num
or regex re.match(r'^0\d+', num) == None

--------------------------------

When you want to know whether an argument is a function: (RuplesJS #3: String EachChar)

x(a) if callable(x) else ...

--------------------------------

Keep in mind: \w is alphanumberic characters! all letters + all numbers so:

to find something like 5f and 6g you must say: re.match('\d[a-ZA-Z]+') not re.match('\d\w')

--------------------------------

Take a look at this later, this is a question you thought you had to solve when seeing the longest path in binary tree question ![link](https://leetcode.com/problems/diameter-of-binary-tree/discuss/480877/543.-Diameter-of-Binary-Tree-and-124.-Binary-Tree-Maximum-Path-Sum), but it was different: ![link](https://www.geeksforgeeks.org/length-of-longest-straight-path-from-a-given-binary-tree/) -> look at the p29 file!!!