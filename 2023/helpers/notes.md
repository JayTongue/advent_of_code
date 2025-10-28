delist regex: [\[\], ']

What is the minimum amount of information you need to solve this problem?

Can you hash it?
Can you Cache it?
	functools cache is superfast when you have expensive operations that are executed only once per unique set of arguments

using frozenset() is more performant than set()

comprehensions are super fast. They only produce values on demand and doesn't store them in memory.
	are comprehensions... generators?

to add something to a set, use .add()
to add its elements to a set, use .update()
to find overlaps between two sets, use an intersection: (set1 & set2)

Doing things one by one is the worse. See if you can go chunk by chunk.

reduce({function}, {iterable}, {starting_value})

Recursion is super fast, but can be inefficient. 
	i.e. It's easy to make a lot of work for yourself that you don't need to do or can't complete

# Walrus :=
python walrus := 
	evaluates and assigns at once. 
	e.g. if (n := len([1, 2, 3])) > 2:
	    print(f"List has {n} elements")
	this can be used to avoid recomputation


# Reduce, Map, Filter
reduce, map, and filter- from functional programming
	Map applies the same function to a list of values
		map(func, iterable)
	reduce applies a particular function passed in its argument to all of the iterable elements
		def add(x, y):
    		return x + y
		a = [1, 2, 3, 4, 5]
		res = reduce(add, a)
	filter applies a map, but looks to see if the result is True
		filter(func, iterable) == (item for item in iterable if func(item))