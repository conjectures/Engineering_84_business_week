# Introduction to Data Types and Operators

## Data Types
- Strings
- Numbers (Integers, Floats)
- Boolean (True or False)

## Arithmetic Operators

```python
# Arithmetic
+, -, *, /

# Power
2 ** 2
# 4

# Modulus - gives remainder of division
4 % 3
# 1
```

## Comparison Operators

- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` greater than or equal
- `==` equal to 

## Bit wise operators
- `x << y`

Return x bit shifted to the left by y places, similar to mutliplying x with `2**y`
```
5 << 3
# 40
```

- `x >> y`
Return x bit shifted to the right by y places, similar to dividing x with `2**y`
```
256 >> 3
#32
```
- `x & y` : Bitwise AND
- `x | y` : Bitwise OR
- `~x` : Complement
- `x ^ y` : Bitwise XOR



# Strings and Casting

`greetings = "Hello World!"`

Indexing in Python starts from 0
```python
# H e l l o   W o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

```
Reverse indexing starts from `-1`
```python
print(greetings[:-6])
# Hello 
print(greetings[-6:])
# World!
```

# Let's have a look at some string methods

```python 
print(greetings.upper())
# HELLO WORLD!
print(greetings.lower())
# hello world!
print(greetings.capitalize())
# Hello World!
print(greetings.replace("World", "Cosmos"))
# Hello Cosmos!
```

