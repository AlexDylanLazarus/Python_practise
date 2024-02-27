## Assignment for lookbehind in regex

[Article Used](https://www.geeksforgeeks.org/python-regex-lookbehind/)
- Lookbehind searches from right to left.
  - This means that it is used to determine if the pattern is behind the parsers current position
- It is known as a a zero-width assertion.

### The syntax is as follows:

#### Positive lookbehind
```
(?<=<lookbehind_regex>)
```

#### Negative lookbehind
```
(?<!<lookbehind_regex>) 
```

### Example:

```
import re

text = "Hello world, this is a sample text with some numbers 12345."

matches = re.findall( r'(?<=\b)\d+', text)

print(matches)  # Output: ['12345']
```

- \b assert position at a word boundary: (^\w|\w$|\W\w|\w\W)
- \d matches a digit (equivalent to [0-9])
- +matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)