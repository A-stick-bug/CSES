These problems will be grouped by category, sorted by the order that 
they appear in https://cses.fi/problemset/

Usually, I try to analyze the time complexity. I only analyze space complexity 
if it is relevant due to tight memory limits (since SC <= TC).

About SortedList:

- We treat it as a **Python built-in** rather than a data structure template
  - This is because languages like C++ have *multiset* while Python doesn't
  - In terms of features, SortedList is actually closer to C++'s PBDS
- The template I use should be pretty similar to https://grantjenks.com/docs/sortedcontainers/sortedlist.html
  - Most the time, you can just replace the import with the template
- The actual underlying structure is very complex, but I place its usage at 10p difficulty
  as it is a reasonable place to be aware of it

The difficulty estimate is based on the DMOJ point system and my own 
experience (which is obviously biased).

- in this system, the point is based off the difficulty of the concept required, in 
addition to the problem itself 
  - so a template segment tree problem would have a 
  higher point value than a difficult binary search problem since 
  the concept itself is harder
  - "Ad hoc" refers to uncategorized observation/thinking based problems 
   (more thinking than coding) and tend to require mathematical intuition.
    - "Constructive", usually has ad hoc aspects and requires you to make a 
      structure (array,tree,etc.) satisfying some property
  - "Implementation" either means the problem is implementation heavy or there is
    not really an algorithm and you just have to code it.
