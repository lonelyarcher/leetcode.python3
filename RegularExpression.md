^ start, $ end
* + ? {m, n} non-greedy *? +? ?? {m, n}?
() captured group
(?:) non-captured group
(?#) comment, ignorable
(?=XXX) lookahead match, match the prev only followed by XXX, (?!=XXX) not followed by XXX
(?<=XXX) lookbehind match, match the following only it is following XXX
\d match digits \D non digits
\w = [a-zA-Z0-9_] \W no w, can be used to split
re.split(r'\W+', "i am , a person.") = ('i', 'am', 'a', 'person', '') flags=re.I
re.findall(pattern, string, flags=0), re.finditer()