#
#
 
T
a
b
l
e
:
 
a
c
c
o
u
n
t
_
w
i
n
_
t
m
p


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
e
m
a
i
l
*
*
:
 
v
a
r
c
h
a
r
(
1
0
0
)




#
#
 
T
a
b
l
e
:
 
a
p
p
_
m
a
p
_
f
a
c
t
o
r
y


-
 
*
*
f
a
c
t
o
r
y
_
i
d
*
*
:
 
i
n
t


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
a
p
p
_
m
a
p
p
c


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
a
t
e
g
o
r
y
_
i
d
*
*
:
 
i
n
t




#
#
 
T
a
b
l
e
:
 
a
p
p
_
u
s
e
r


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
c
a
t
e
g
o
r
y
_
p
r
o
d
u
c
t
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
a
t
e
g
o
r
y
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
c
a
t
e
g
o
r
y
(
i
d
)


-
 
*
*
p
r
o
d
u
c
t
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
p
r
o
d
u
c
t
(
i
d
)


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
i
n
t


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
u
p
d
a
t
e
d
_
b
y
*
*
:
 
i
n
t


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
C
a
t
e
g
o
r
y
P
r
o
d
u
c
t
`
 
o
n
 
(
c
a
t
e
g
o
r
y
_
i
d
,
 
p
r
o
d
u
c
t
_
i
d
)




#
#
 
T
a
b
l
e
:
 
p
r
o
d
u
c
t
_
b
r
a
n
d


-
 
*
*
p
r
o
d
u
c
t
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
b
r
a
n
d
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y




#
#
 
T
a
b
l
e
:
 
p
r
o
d
u
c
t
_
b
r
a
n
d
_
t
m
p


-
 
*
*
c
o
l
u
m
n
1
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
o
l
u
m
n
2
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
r
o
l
e
_
p
e
r
m
i
s
i
o
n


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
r
o
l
e
_
i
d
*
*
:
 
i
n
t


-
 
*
*
p
e
r
m
i
s
i
o
n
_
i
d
*
*
:
 
i
n
t




#
#
 
T
a
b
l
e
:
 
s
y
s
d
i
a
g
r
a
m
s


-
 
*
*
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
2
8
)


-
 
*
*
p
r
i
n
c
i
p
a
l
_
i
d
*
*
:
 
i
n
t


-
 
*
*
d
i
a
g
r
a
m
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
v
e
r
s
i
o
n
*
*
:
 
i
n
t


-
 
*
*
d
e
f
i
n
i
t
i
o
n
*
*
:
 
v
a
r
b
i
n
a
r
y
(
-
1
)


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
K
_
p
r
i
n
c
i
p
a
l
_
n
a
m
e
`
 
o
n
 
(
p
r
i
n
c
i
p
a
l
_
i
d
,
 
n
a
m
e
)




#
#
 
T
a
b
l
e
:
 
t
b
_
a
d
m
i
n
_
f
a
c
t
o
r
y


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
u
s
e
r
_
i
d
*
*
:
 
i
n
t


-
 
*
*
f
a
c
t
o
r
y
_
i
d
*
*
:
 
i
n
t


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
_
t
b
_
a
d
m
i
n
_
_
B
9
B
E
3
7
0
E
A
4
E
1
E
3
2
C
`
 
o
n
 
(
u
s
e
r
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
a
p
i
_
k
e
y
s


-
 
*
*
i
d
*
*
:
 
u
n
i
q
u
e
i
d
e
n
t
i
f
i
e
r
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
k
e
y
_
h
a
s
h
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
5
)


-
 
*
*
l
a
b
e
l
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
0
)


-
 
*
*
s
c
o
p
e
*
*
:
 
n
v
a
r
c
h
a
r
(
-
1
)


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e
2


-
 
*
*
e
x
p
i
r
e
s
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e
2


-
 
*
*
r
e
v
o
k
e
d
*
*
:
 
b
i
t


-
 
*
*
d
a
i
l
y
_
q
u
o
t
a
*
*
:
 
i
n
t


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
_
t
b
_
a
p
i
_
k
_
_
1
4
E
2
2
E
8
6
E
0
7
4
1
1
0
8
`
 
o
n
 
(
k
e
y
_
h
a
s
h
)




#
#
 
T
a
b
l
e
:
 
t
b
_
b
l
a
c
k
l
i
s
t
e
d
_
t
o
k
e
n
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
t
o
k
e
n
*
*
:
 
v
a
r
c
h
a
r
(
5
0
0
)


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
B
l
a
c
k
l
i
s
t
e
d
T
o
k
e
n
s
_
T
o
k
e
n
`
 
o
n
 
(
t
o
k
e
n
)


 
 
-
 
`
I
X
_
B
l
a
c
k
l
i
s
t
e
d
T
o
k
e
n
s
_
T
o
k
e
n
`
 
o
n
 
(
t
o
k
e
n
)




#
#
 
T
a
b
l
e
:
 
t
b
_
b
r
a
n
d


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
b
r
a
n
d
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
b
u
s
i
n
e
s
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
b
u
s
i
n
e
s
s
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
0
)


-
 
*
*
s
e
c
r
e
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
c
a
t
e
g
o
r
y


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
a
t
e
g
o
r
y
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
a
t
e
g
o
r
y
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
5
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)


-
 
*
*
p
a
r
e
n
t
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
c
a
t
e
g
o
r
y
(
i
d
)


-
 
*
*
o
r
d
e
r
_
n
u
m
b
e
r
*
*
:
 
i
n
t


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
C
a
t
e
g
o
r
y
_
C
o
d
e
_
B
u
s
i
n
e
s
s
`
 
o
n
 
(
c
a
t
e
g
o
r
y
_
c
o
d
e
,
 
b
u
s
i
n
e
s
s
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
c
h
a
n
n
e
l


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
h
a
n
n
e
l
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
h
a
n
n
e
l
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
5
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
C
h
a
n
n
e
l
_
C
o
d
e
_
B
u
s
i
n
e
s
s
`
 
o
n
 
(
c
h
a
n
n
e
l
_
c
o
d
e
,
 
b
u
s
i
n
e
s
s
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
c
u
s
t
o
m
e
r


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
u
s
t
o
m
e
r
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
3
5
0
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
C
u
s
t
o
m
e
r
_
C
o
d
e
`
 
o
n
 
(
c
u
s
t
o
m
e
r
_
c
o
d
e
)




#
#
 
T
a
b
l
e
:
 
t
b
_
f
a
c
t
o
r
y


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
f
a
c
t
o
r
y
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
5
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
l
a
n
g


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
l
a
n
g
u
a
g
e
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
k
e
y
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
t
r
a
n
s
l
a
t
i
o
n
*
*
:
 
n
v
a
r
c
h
a
r
(
1
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
n
a
v
i
g
a
t
i
o
n
_
m
e
n
u


-
 
*
*
m
e
n
u
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
t
i
t
l
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)


-
 
*
*
u
r
l
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
5
)


-
 
*
*
i
c
o
n
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
p
a
r
e
n
t
_
i
d
*
*
:
 
i
n
t


-
 
*
*
d
i
s
p
l
a
y
_
o
r
d
e
r
*
*
:
 
i
n
t


-
 
*
*
i
s
_
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e




#
#
 
T
a
b
l
e
:
 
t
b
_
o
r
d
e
r


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
o
_
d
o
c
_
n
o
*
*
:
 
i
n
t


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
u
s
e
r
s
(
i
d
)


-
 
*
*
o
r
d
e
r
_
d
a
t
e
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
a
d
d
r
e
s
s
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
0
)


-
 
*
*
c
a
r
_
n
u
m
b
e
r
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
d
e
l
i
v
e
r
y
_
d
a
t
e
*
*
:
 
d
a
t
e


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
s
t
a
t
u
s
*
*
:
 
v
a
r
c
h
a
r
(
2
0
)


-
 
*
*
i
s
_
s
y
n
c
*
*
:
 
b
i
t


-
 
*
*
o
r
d
_
d
o
c
_
n
o
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
i
s
_
c
h
e
c
k
*
*
:
 
b
i
t


-
 
*
*
i
s
_
r
e
s
t
o
r
e
*
*
:
 
b
i
t


-
 
*
*
i
s
_
s
p
e
c
i
a
l
*
*
:
 
c
h
a
r
(
1
)




#
#
 
T
a
b
l
e
:
 
t
b
_
o
r
d
e
r
d
e
t
a
i
l


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
o
r
d
e
r
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
o
r
d
e
r
(
i
d
)


-
 
*
*
p
r
o
d
u
c
t
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
p
r
o
d
u
c
t
(
i
d
)


-
 
*
*
p
r
i
c
e
*
*
:
 
d
e
c
i
m
a
l


-
 
*
*
q
u
a
n
t
i
t
y
*
*
:
 
i
n
t


-
 
*
*
i
t
e
m
_
w
e
i
g
h
t
*
*
:
 
i
n
t


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
r
e
m
a
r
k
*
*
:
 
n
v
a
r
c
h
a
r
(
-
1
)


-
 
*
*
p
r
o
d
u
c
t
_
b
r
a
n
d
c
o
d
e
*
*
:
 
n
c
h
a
r
(
1
0
)


-
 
*
*
p
a
c
k
s
i
z
e
_
c
o
d
e
*
*
:
 
i
n
t


-
 
*
*
o
u
t
_
o
f
_
s
t
o
c
k
*
*
:
 
n
c
h
a
r
(
1
0
)


-
 
*
*
a
t
t
r
i
b
u
t
e
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
p
e
r
m
i
s
i
o
n
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
0
)


-
 
*
*
r
e
s
o
u
r
c
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
a
c
t
i
o
n
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
m
e
t
h
o
d
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e




#
#
 
T
a
b
l
e
:
 
t
b
_
p
r
i
c
e


-
 
*
*
i
d
*
*
:
 
i
n
t


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
l
a
s
s
_
p
r
i
c
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
i
c
e
*
*
:
 
f
l
o
a
t




#
#
 
T
a
b
l
e
:
 
t
b
_
p
r
o
d
u
c
t


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
p
r
o
d
u
c
t
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
5
0
)


-
 
*
*
n
a
m
e
_
e
n
g
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
u
n
i
t
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
p
a
c
k
a
g
e
_
s
i
z
e
*
*
:
 
i
n
t


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
i
m
a
g
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)


-
 
*
*
b
r
a
n
d
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
i
t
e
m
_
w
e
i
g
h
t
*
*
:
 
f
l
o
a
t


-
 
*
*
p
r
o
d
u
c
t
_
b
r
a
n
d
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
I
n
d
e
x
_
t
b
_
p
r
o
d
u
c
t
_
1
`
 
o
n
 
(
p
r
o
d
u
c
t
_
c
o
d
e
)




#
#
 
T
a
b
l
e
:
 
t
b
_
p
r
o
d
u
c
t
_
c
a
t
e
g
o
r
y


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
c
a
t
e
g
o
r
y
_
i
d
*
*
:
 
i
n
t


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
i
n
t


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
I
X
_
t
b
_
p
r
o
d
u
c
t
_
c
a
t
e
g
o
r
y
`
 
o
n
 
(
p
r
o
d
u
c
t
_
c
o
d
e
,
 
c
a
t
e
g
o
r
y
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
p
r
o
d
u
c
t
_
p
l
a
n


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
l
a
n
_
d
a
t
e
*
*
:
 
d
a
t
e


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
p
l
a
n
_
q
u
a
n
t
i
t
y
*
*
:
 
i
n
t


-
 
*
*
c
r
e
a
t
e
d
_
d
a
t
e
*
*
:
 
d
a
t
e


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
i
n
t


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
p
l
a
n
_
w
e
i
g
h
t
*
*
:
 
i
n
t


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
I
n
d
e
x
_
t
b
_
p
r
o
d
u
c
t
_
p
l
a
n
_
1
`
 
o
n
 
(
p
l
a
n
_
d
a
t
e
,
 
o
r
g
_
c
o
d
e
,
 
p
r
o
d
u
c
t
_
c
o
d
e
)




#
#
 
T
a
b
l
e
:
 
t
b
_
p
r
o
d
u
c
t
_
t
y
p
e


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
t
y
p
e
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
t
y
p
e
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
5
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)


-
 
*
*
o
r
d
e
r
_
n
u
m
b
e
r
*
*
:
 
i
n
t


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
P
r
o
d
u
c
t
T
y
p
e
_
C
o
d
e
_
B
u
s
i
n
e
s
s
`
 
o
n
 
(
t
y
p
e
_
c
o
d
e
,
 
b
u
s
i
n
e
s
s
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
p
r
o
d
u
c
t
_
t
y
p
e
_
m
a
p
p
i
n
g


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
t
y
p
e
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
p
r
o
d
u
c
t
_
t
y
p
e
(
i
d
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
U
Q
_
P
r
o
d
u
c
t
_
T
y
p
e
_
B
u
s
i
n
e
s
s
`
 
o
n
 
(
p
r
o
d
u
c
t
_
c
o
d
e
,
 
t
y
p
e
_
i
d
,
 
b
u
s
i
n
e
s
s
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
r
o
l
e
_
m
e
n
u


-
 
*
*
r
o
l
e
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
r
o
l
e
s
(
i
d
)


-
 
*
*
m
e
n
u
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
n
a
v
i
g
a
t
i
o
n
_
m
e
n
u
(
m
e
n
u
_
i
d
)


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
b
u
s
i
n
e
s
s
(
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
r
o
l
e
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
d
e
s
c
r
i
p
t
i
o
n
*
*
:
 
n
v
a
r
c
h
a
r
(
2
5
0
)


-
 
*
*
p
a
r
e
n
t
*
*
:
 
i
n
t


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e




#
#
 
T
a
b
l
e
:
 
t
b
_
s
t
o
c
k


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
o
d
u
c
t
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
s
t
o
c
k
_
q
u
a
n
t
i
t
y
*
*
:
 
i
n
t


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
I
X
_
t
b
_
s
t
o
c
k
`
 
o
n
 
(
o
r
g
_
c
o
d
e
,
 
p
r
o
d
u
c
t
_
c
o
d
e
)




#
#
 
T
a
b
l
e
:
 
t
b
_
t
e
s
t


-
 
*
*
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
d
e
s
c
r
i
p
t
i
o
n
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
t
e
s
t
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
t
m
p


-
 
*
*
u
s
e
r
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)


-
 
*
*
b
r
a
n
d
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)




#
#
 
T
a
b
l
e
:
 
t
b
_
u
s
e
r
_
b
u
s
i
n
e
s
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
u
s
e
r
_
i
d
*
*
:
 
i
n
t


-
 
*
*
b
u
s
i
n
e
s
s
_
i
d
*
*
:
 
i
n
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
i
n
t


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
I
n
d
e
x
_
t
b
_
u
s
e
r
_
b
u
s
i
n
e
s
s
_
1
`
 
o
n
 
(
b
u
s
i
n
e
s
s
_
i
d
,
 
u
s
e
r
_
i
d
)




#
#
 
T
a
b
l
e
:
 
t
b
_
u
s
e
r
_
c
l
a
s
s
p
r
i
c
e


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
o
r
g
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
l
a
s
s
_
p
r
i
c
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
i
d
*
*
:
 
i
n
t




#
#
 
T
a
b
l
e
:
 
t
b
_
u
s
e
r
_
f
a
c
t
o
r
y


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
u
s
e
r
_
i
d
*
*
:
 
i
n
t


-
 
*
*
f
a
c
t
o
r
y
_
i
d
*
*
:
 
i
n
t


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e




#
#
 
T
a
b
l
e
:
 
t
b
_
u
s
e
r
_
m
e
n
u


-
 
*
*
u
s
e
r
_
m
e
n
u
_
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
u
s
e
r
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
u
s
e
r
s
(
i
d
)


-
 
*
*
m
e
n
u
_
i
d
*
*
:
 
i
n
t
,
 
f
o
r
e
i
g
n
 
k
e
y
 
→
 
t
b
_
n
a
v
i
g
a
t
i
o
n
_
m
e
n
u
(
m
e
n
u
_
i
d
)


-
 
*
*
c
a
n
_
a
c
c
e
s
s
*
*
:
 
b
i
t


-
 
*
*
a
r
r
a
n
g
e
*
*
:
 
i
n
t




#
#
 
T
a
b
l
e
:
 
t
b
_
u
s
e
r
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
c
u
s
t
o
m
e
r
_
c
o
d
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
f
u
l
l
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)


-
 
*
*
u
s
e
r
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)


-
 
*
*
p
a
s
s
w
o
r
d
*
*
:
 
n
v
a
r
c
h
a
r
(
3
5
0
)


-
 
*
*
p
h
o
n
e
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
a
c
t
i
v
e
*
*
:
 
b
i
t


-
 
*
*
c
r
e
a
t
e
d
_
b
y
*
*
:
 
i
n
t


-
 
*
*
c
r
e
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
i
s
_
d
e
l
e
t
e
*
*
:
 
b
i
t


-
 
*
*
a
d
d
r
e
s
s
*
*
:
 
n
v
a
r
c
h
a
r
(
1
5
0
)


-
 
*
*
u
p
d
a
t
e
d
_
a
t
*
*
:
 
d
a
t
e
t
i
m
e


-
 
*
*
b
r
a
n
d
*
*
:
 
n
v
a
r
c
h
a
r
(
5
0
)


-
 
*
*
I
n
d
e
x
e
s
*
*
:


 
 
-
 
`
I
X
_
t
b
_
u
s
e
r
s
`
 
o
n
 
(
u
s
e
r
n
a
m
e
,
 
c
u
s
t
o
m
e
r
_
c
o
d
e
,
 
i
s
_
d
e
l
e
t
e
)




#
#
 
T
a
b
l
e
:
 
t
b
_
v
a
r
i
a
n
t
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
p
r
o
d
u
c
t
_
i
d
*
*
:
 
i
n
t


-
 
*
*
a
t
t
r
i
b
u
t
e
_
n
a
m
e
*
*
:
 
n
v
a
r
c
h
a
r
(
1
0
0
)




#
#
 
T
a
b
l
e
:
 
u
s
e
r
_
r
o
l
e
s


-
 
*
*
i
d
*
*
:
 
i
n
t
,
 
p
r
i
m
a
r
y
 
k
e
y


-
 
*
*
u
s
e
r
_
i
d
*
*
:
 
i
n
t


-
 
*
*
r
o
l
e
_
i
d
*
*
:
 
i
n
t




#
#
 
T
a
b
l
e
:
 
v
o
.
h
i
e
u


-
 
*
*
i
d
*
*
:
 
n
c
h
a
r
(
1
0
)




#
#
 
S
t
o
r
e
d
 
P
r
o
c
e
d
u
r
e
s


-
 
g
e
t
_
u
s
e
r


-
 
p
s
_
t
e
s
t


-
 
g
e
t
_
t
e
s
t


-
 
p
s
_
c
a
c
u
l
a
t
o
r


-
 
s
p
_
u
p
g
r
a
d
d
i
a
g
r
a
m
s


-
 
s
p
_
h
e
l
p
d
i
a
g
r
a
m
s


-
 
s
p
_
h
e
l
p
d
i
a
g
r
a
m
d
e
f
i
n
i
t
i
o
n


-
 
s
p
_
c
r
e
a
t
e
d
i
a
g
r
a
m


-
 
s
p
_
r
e
n
a
m
e
d
i
a
g
r
a
m


-
 
s
p
_
a
l
t
e
r
d
i
a
g
r
a
m


-
 
s
p
_
d
r
o
p
d
i
a
g
r
a
m

