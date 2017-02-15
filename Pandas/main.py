from pandas import Series, DataFrame

s = Series([1, 2, 3.0, 'abc'])
print(s)

s = Series(index=['a', 'b', 'c', 'd'], data=[1, 3, 5, 7], )
print(s)
print(s.index)
print(s.values)

data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame(data)
print(df)
print(df.index)
print(df.year[2])

temp = df.drop(2)  # Delete row or column
print(temp)

temp = df[:2]  # Slice row
print(temp)

temp = df.ix[:2, :2]  # Slice row and column
print(temp)

temp = df.sort_values(by='pop')
print(temp)
