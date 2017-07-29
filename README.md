# MedianHeap
Find the median of given numbers by implementing heap data structure on python.

Example below does:

Input: A list of numbers.

Output: 2 lines; first line tells the number that pushed into heap and second line tells the new median.

```python
hp = Heapy()
numbers =[12, 4, 5, 3, 8, 7, 6]
for x in numbers:
    hp.add_number(x)
    print("Add Number: ", x)
    hp.balance()
    print("New Median: ", hp.get_median())
```
```
Output:
Add Number:  12
New Median:  12.0
Add Number:  4
New Median:  8.0
Add Number:  5
New Median:  5.0
Add Number:  3
New Median:  4.5
Add Number:  8
New Median:  5.0
Add Number:  7
New Median:  6.0
Add Number:  6
New Median:  6.0
```
