In [1]: import panda as pd
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-1-cb2e74f3cfa3> in <module>()
----> 1 import panda as pd

ImportError: No module named panda

In [2]: import panda as pd
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-2-cb2e74f3cfa3> in <module>()
----> 1 import panda as pd

ImportError: No module named panda

In [3]: import panda as pd
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-3-cb2e74f3cfa3> in <module>()
----> 1 import panda as pd

ImportError: No module named panda

In [4]: import pandas as pd

In [5]: s1 = pd.Series([1,2,3,4,5], index=list('abcde')
   ...: )

In [6]: s
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-f4d5d0c0671b> in <module>()
----> 1 s

NameError: name 's' is not defined

In [7]: s1
Out[7]: 
a    1
b    2
c    3
d    4
e    5
dtype: int64

In [8]: data = {'one'::s1*s*1, 'two':s1+1}
  File "<ipython-input-8-b7abd0c6bb33>", line 1
    data = {'one'::s1*s*1, 'two':s1+1}
                  ^
SyntaxError: invalid syntax


In [9]: data = {'one':s1*s*1, 'two':s1+1}
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-c4e382e2ce7c> in <module>()
----> 1 data = {'one':s1*s*1, 'two':s1+1}

NameError: name 's' is not defined

In [10]: data = {'one':s1**s1, 'two':s1+1}

In [11]: type(data)
Out[11]: dict

In [12]: df
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-7ed0097d7e9e> in <module>()
----> 1 df

NameError: name 'df' is not defined

In [13]: df= pd.DataFrame(data)

In [14]: df
Out[14]: 
    one  two
a     1    2
b     4    3
c    27    4
d   256    5
e  3125    6

In [15]: s2=s1

In [16]: s2
Out[16]: 
a    1
b    2
c    3
d    4
e    5
dtype: int64

In [17]: s2.index=[1,2,3,4,5]

In [18]: s2.index
Out[18]: Int64Index([1, 2, 3, 4, 5], dtype='int64')

In [19]: df['tremila']=s2

In [20]: df
Out[20]: 
    one  two  tremila
a     1    2      NaN
b     4    3      NaN
c    27    4      NaN
d   256    5      NaN
e  3125    6      NaN

In [21]: s12
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-21-06c6f839e57f> in <module>()
----> 1 s12

NameError: name 's12' is not defined

In [22]: s2
Out[22]: 
1    1
2    2
3    3
4    4
5    5
dtype: int64

In [23]: df.columns=['a','b','c']

In [24]: df
Out[24]: 
      a  b   c
a     1  2 NaN
b     4  3 NaN
c    27  4 NaN
d   256  5 NaN
e  3125  6 NaN

In [25]: df.indexes = [1,2,3,4,5]

In [26]: df
Out[26]: 
      a  b   c
a     1  2 NaN
b     4  3 NaN
c    27  4 NaN
d   256  5 NaN
e  3125  6 NaN

In [27]: df['c']=s2

In [28]: df
Out[28]: 
      a  b   c
a     1  2 NaN
b     4  3 NaN
c    27  4 NaN
d   256  5 NaN
e  3125  6 NaN

In [29]: df.indexe=[1,2,3,4,5]

In [30]: df
Out[30]: 
      a  b   c
a     1  2 NaN
b     4  3 NaN
c    27  4 NaN
d   256  5 NaN
e  3125  6 NaN

In [31]: df.index=[1,2,3,4,5]

In [32]: df
Out[32]: 
      a  b   c
1     1  2 NaN
2     4  3 NaN
3    27  4 NaN
4   256  5 NaN
5  3125  6 NaN

In [33]: df['c']=s2

In [34]: df
Out[34]: 
      a  b  c
1     1  2  1
2     4  3  2
3    27  4  3
4   256  5  4
5  3125  6  5

In [35]: s2= pd.Series([1,2,3,4,5], index=list('abcde')
   ....: )

In [36]: s2
Out[36]: 
a    1
b    2
c    3
d    4
e    5
dtype: int64

In [37]: df.index=list('ecbdf')

In [38]: df
Out[38]: 
      a  b  c
e     1  2  1
c     4  3  2
b    27  4  3
d   256  5  4
f  3125  6  5

In [39]: df['c']=s2

In [40]: df
Out[40]: 
      a  b   c
e     1  2   5
c     4  3   3
b    27  4   2
d   256  5   4
f  3125  6 NaN

In [41]: data=np.random.randn(5,2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-41-a8912a8dc6af> in <module>()
----> 1 data=np.random.randn(5,2)

NameError: name 'np' is not defined

In [42]: import numpy as np

In [43]: data=np.random.randn(5,2)

In [44]: data
Out[44]: 
array([[  1.55576973e+00,  -4.71761873e-01],
       [ -1.30470864e-01,  -1.67076903e+00],
       [ -2.28718035e-01,  -6.83276170e-01],
       [  7.76923065e-01,   7.67115791e-01],
       [  1.67031609e-03,  -7.17894809e-01]])

In [45]: df=pd.DataFrame(data,index = list('abcde'), coloumns=['one','two']
   ....: )
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-45-313fe8eb4fb4> in <module>()
----> 1 df=pd.DataFrame(data,index = list('abcde'), coloumns=['one','two']
      2 )

TypeError: __init__() got an unexpected keyword argument 'coloumns'

In [46]: df=pd.DataFrame(data,index = list('abcde'), columns=['one','two'])

In [47]: df
Out[47]: 
        one       two
a  1.555770 -0.471762
b -0.130471 -1.670769
c -0.228718 -0.683276
d  0.776923  0.767116
e  0.001670 -0.717895

In [48]: col=df.one

In [49]: col
Out[49]: 
a    1.555770
b   -0.130471
c   -0.228718
d    0.776923
e    0.001670
Name: one, dtype: float64

In [50]: type(col)
Out[50]: pandas.core.series.Series

In [51]: row=df.xs('b')

In [52]: b
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-52-3b5d5c371295> in <module>()
----> 1 b

NameError: name 'b' is not defined

In [53]: row
Out[53]: 
one   -0.130471
two   -1.670769
Name: b, dtype: float64

In [54]: type(row)
Out[54]: pandas.core.series.Series

In [55]: df=pd.DataFrame(data,index = list('abbbe'), columns=['one','two'])

In [56]: df
Out[56]: 
        one       two
a  1.555770 -0.471762
b -0.130471 -1.670769
b -0.228718 -0.683276
b  0.776923  0.767116
e  0.001670 -0.717895

In [57]: df=pd.DataFrame(data,index = list('abbbe'), columns=['one','one'])

In [58]: df
Out[58]: 
        one       one
a  1.555770 -0.471762
b -0.130471 -1.670769
b -0.228718 -0.683276
b  0.776923  0.767116
e  0.001670 -0.717895

In [59]: col=df.one

In [60]: col
Out[60]: 
        one       one
a  1.555770 -0.471762
b -0.130471 -1.670769
b -0.228718 -0.683276
b  0.776923  0.767116
e  0.001670 -0.717895

In [61]: type(col)
Out[61]: pandas.core.frame.DataFrame

In [62]: row=df.xs('b')

In [63]: type(row)
Out[63]: pandas.core.frame.DataFrame

In [64]: row
Out[64]: 
        one       one
b -0.130471 -1.670769
b -0.228718 -0.683276
b  0.776923  0.767116

In [65]: df=pd.DataFrame(data,index = list('abcde'), columns=['one','two'])

In [66]: df
Out[66]: 
        one       two
a  1.555770 -0.471762
b -0.130471 -1.670769
c -0.228718 -0.683276
d  0.776923  0.767116
e  0.001670 -0.717895

In [67]: df.ix['a']
Out[67]: 
one    1.555770
two   -0.471762
Name: a, dtype: float64

In [68]: type(df.ix['a'])
Out[68]: pandas.core.series.Series

In [69]: df.iloc[1,1]
Out[69]: -1.6707690337090699

In [70]: df.mean()
Out[70]: 
one    0.395035
two   -0.555317
dtype: float64

In [71]: df.mean(axis=1)
Out[71]: 
a    0.542004
b   -0.900620
c   -0.455997
d    0.772019
e   -0.358112
dtype: float64

In [72]: df.ix['a'].mean(axis=1)
Out[72]: 0.54200392681869469

In [73]: df.ix['a'].mean(axis=0)
Out[73]: 0.54200392681869469

In [74]: df.ix['a']
Out[74]: 
one    1.555770
two   -0.471762
Name: a, dtype: float64

In [75]: df.ix['a'].mean(axis=0)
Out[75]: 0.54200392681869469

In [76]: df1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-76-e51f5dd68a05> in <module>()
----> 1 df1

NameError: name 'df1' is not defined

In [77]: df1=pd.DataFrame(np.random.rand
np.random.rand             np.random.random
np.random.randint          np.random.random_integers
np.random.randn            np.random.random_sample

In [77]: df1=pd.DataFrame(np.random.randn(6, 3), columns=['A','B','C'])

In [78]: df2=pd.DataFrame(np.random.randn(6, 3), columns=['A','B','C'])

In [79]: df3=df1.copy()

In [80]: df1
Out[80]: 
          A         B         C
0  0.046430 -2.162765 -0.852180
1  1.924129 -0.610644  1.206051
2 -0.223661 -1.087791 -1.836772
3  0.798298 -0.375727  0.377745
4  0.667173 -1.194150 -0.088722
5 -1.900235  0.908775 -0.267576

In [81]: df2
Out[81]: 
          A         B         C
0 -0.387266 -0.417813  1.269620
1  1.029947 -0.586089 -0.470838
2 -1.586241 -0.930255 -0.473067
3 -1.403153  0.790704 -0.186402
4  1.208448  0.854779 -0.705194
5  0.566307  1.060011 -0.890049

In [82]: df3
Out[82]: 
          A         B         C
0  0.046430 -2.162765 -0.852180
1  1.924129 -0.610644  1.206051
2 -0.223661 -1.087791 -1.836772
3  0.798298 -0.375727  0.377745
4  0.667173 -1.194150 -0.088722
5 -1.900235  0.908775 -0.267576

In [83]: df=pd.concat([df1,df2])

In [84]: type([df1,df2])
Out[84]: list

In [85]: df=pd.concat([df1,df2])

In [86]: df
Out[86]: 
          A         B         C
0  0.046430 -2.162765 -0.852180
1  1.924129 -0.610644  1.206051
2 -0.223661 -1.087791 -1.836772
3  0.798298 -0.375727  0.377745
4  0.667173 -1.194150 -0.088722
5 -1.900235  0.908775 -0.267576
0 -0.387266 -0.417813  1.269620
1  1.029947 -0.586089 -0.470838
2 -1.586241 -0.930255 -0.473067
3 -1.403153  0.790704 -0.186402
4  1.208448  0.854779 -0.705194
5  0.566307  1.060011 -0.890049

In [87]: help(pd.concat)


In [88]: df=pd.concat([df1,df2],join_axes=1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-88-85693b9dd4a5> in <module>()
----> 1 df=pd.concat([df1,df2],join_axes=1)

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in concat(objs, axis, join, join_axes, ignore_index, keys, levels, names, verify_integrity, copy)
    720                        keys=keys, levels=levels, names=names,
    721                        verify_integrity=verify_integrity,
--> 722                        copy=copy)
    723     return op.get_result()
    724 

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in __init__(self, objs, axis, join, join_axes, keys, levels, names, ignore_index, verify_integrity, copy)
    852         self.copy = copy
    853 
--> 854         self.new_axes = self._get_new_axes()
    855 
    856     def get_result(self):

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in _get_new_axes(self)
    906                 new_axes[i] = self._get_comb_axis(i)
    907         else:
--> 908             if len(self.join_axes) != ndim - 1:
    909                 raise AssertionError("length of join_axes must not be "
    910                                      "equal to {0}".format(ndim - 1))

TypeError: object of type 'int' has no len()

In [89]: help(pd.concat)


In [90]: df=pd.concat([df1,df2],join_axes=[0,1,2,3,4])
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-90-1f93879ff725> in <module>()
----> 1 df=pd.concat([df1,df2],join_axes=[0,1,2,3,4])

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in concat(objs, axis, join, join_axes, ignore_index, keys, levels, names, verify_integrity, copy)
    720                        keys=keys, levels=levels, names=names,
    721                        verify_integrity=verify_integrity,
--> 722                        copy=copy)
    723     return op.get_result()
    724 

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in __init__(self, objs, axis, join, join_axes, keys, levels, names, ignore_index, verify_integrity, copy)
    852         self.copy = copy
    853 
--> 854         self.new_axes = self._get_new_axes()
    855 
    856     def get_result(self):

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in _get_new_axes(self)
    908             if len(self.join_axes) != ndim - 1:
    909                 raise AssertionError("length of join_axes must not be "
--> 910                                      "equal to {0}".format(ndim - 1))
    911 
    912             # ufff...

AssertionError: length of join_axes must not be equal to 1

In [91]: 

In [91]: 

In [91]: 

In [91]: 

In [91]: 

In [91]: 

In [91]: 

In [91]: 

In [91]: 

In [91]: help(pd.concat)


In [92]: df=pd.concat([df1,df2],join_axes : [0,1,2,3,4])
  File "<ipython-input-92-30ca619a0e35>", line 1
    df=pd.concat([df1,df2],join_axes : [0,1,2,3,4])
                                     ^
SyntaxError: invalid syntax


In [93]: df=pd.concat([df1,df2],join_axes = [0,1,2,3,4])
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-93-a4d8085a7509> in <module>()
----> 1 df=pd.concat([df1,df2],join_axes = [0,1,2,3,4])

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in concat(objs, axis, join, join_axes, ignore_index, keys, levels, names, verify_integrity, copy)
    720                        keys=keys, levels=levels, names=names,
    721                        verify_integrity=verify_integrity,
--> 722                        copy=copy)
    723     return op.get_result()
    724 

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in __init__(self, objs, axis, join, join_axes, keys, levels, names, ignore_index, verify_integrity, copy)
    852         self.copy = copy
    853 
--> 854         self.new_axes = self._get_new_axes()
    855 
    856     def get_result(self):

/usr/lib/python2.7/dist-packages/pandas/tools/merge.pyc in _get_new_axes(self)
    908             if len(self.join_axes) != ndim - 1:
    909                 raise AssertionError("length of join_axes must not be "
--> 910                                      "equal to {0}".format(ndim - 1))
    911 
    912             # ufff...

AssertionError: length of join_axes must not be equal to 1

In [94]: df=pd.concat([df1,df2],axes = a)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-94-79e160cca55c> in <module>()
----> 1 df=pd.concat([df1,df2],axes = a)

NameError: name 'a' is not defined

In [95]: df=pd.concat([df1,df2],axes = 1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-95-71aea2f4f353> in <module>()
----> 1 df=pd.concat([df1,df2],axes = 1)

TypeError: concat() got an unexpected keyword argument 'axes'

In [96]: df=pd.concat([df1,df2],axes = 1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-96-71aea2f4f353> in <module>()
----> 1 df=pd.concat([df1,df2],axes = 1)

TypeError: concat() got an unexpected keyword argument 'axes'

In [97]: df=pd.concat([df1,df2],axis = 1)

In [98]: df
Out[98]: 
          A         B         C         A         B         C
0  0.046430 -2.162765 -0.852180 -0.387266 -0.417813  1.269620
1  1.924129 -0.610644  1.206051  1.029947 -0.586089 -0.470838
2 -0.223661 -1.087791 -1.836772 -1.586241 -0.930255 -0.473067
3  0.798298 -0.375727  0.377745 -1.403153  0.790704 -0.186402
4  0.667173 -1.194150 -0.088722  1.208448  0.854779 -0.705194
5 -1.900235  0.908775 -0.267576  0.566307  1.060011 -0.890049

In [99]: help(pd.concat)


In [100]: save Test_panda.py
'' was not found in history, as a file, url, nor in the user namespace.

In [101]: save '~/Test_panda.py'
'' was not found in history, as a file, url, nor in the user namespace.

In [102]: save '~/test.py'
'' was not found in history, as a file, url, nor in the user namespace.

In [103]: save "~/test.py"
'' was not found in history, as a file, url, nor in the user namespace.

In [104]: 

In [104]: ipython.notebook
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-104-b15799545e07> in <module>()
----> 1 ipython.notebook

NameError: name 'ipython' is not defined

In [105]: 

