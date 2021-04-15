'''
# Matrix-module that supports following methods:

 __ add__(self, other_matrix) method should add current instance to matrix instanse that pass as argument <br>
 __ sub__(self, other_matrix) method should subtract from current instance a matrix instanse that pass as argument <br>
 __ mul__(self, other_matrix) method should multiply current instance with matrix instanse that pass as argument <br>
 __ str__(self, other_matrix) method shuld return string of matrix as follows: <br>
 determinant() calculates determinant of matrix
 inverse() calculate inverse of matrix
 same_dimention_with(other_matrix) makes sure other matrix has the same dimension as instance matrix
 is_square() check if matrix is square
 random_matrix() static method returns instance of Matrix

'''

import random

class Matrix:
    def __init__(self, mat: list, row: int ,col: int):
        self.mat = mat
        self.validation()
        self.length = len(mat)
        self.rowl = len(mat[0])
        self.row = row
        self.col = col

    def validation(self):
        for x in self.mat:
            k = all(1 if (''.join(str( str(i).strip('-') ).split('.', 1))).isdecimal() else 0 for i in x)
            if (not k):
                raise Exception('Input matrix contains non-numeric character')
            elif( len(x)!=len(self.mat[0]) ):
                raise Exception('Input matrix\'s rows are not equal' )


    def __add__(self, other_matrix):
        if not self.check_dimention(other_matrix):
            raise ValueError('matrixes do not have same dimension')
        matrix_addition = []
        for el in range(len(self.mat)):
            new_row = list(map(lambda n1, n2: n1+n2, self.mat[el], other_matrix.mat[el]))
            matrix_addition.append(new_row)
        return Matrix(matrix_addition)


    def __sub__(self, other_matrix):
        if not self.check_dimention(other_matrix):
            raise ValueError('matrixes do not have same dimension')
        matrix_addition = []
        for el in range(len(self.mat)):
            new_row = list(map(lambda n1, n2: n1-n2, self.mat[el], other_matrix.mat[el]))
            matrix_addition.append(new_row)
        return Matrix(matrix_addition)


    def __mul__(self, other_matrix):
        matrix_mul = []
        for el in range(len(self.mat)):
            new_row = []
            for j in range(len(other_matrix.mat[0])):
                new_el =0
                for i in range(len(other_matrix.mat)):
                    new_el +=self.mat[el][i] * other_matrix.mat[i][j]
                new_row.append(new_el)
            matrix_mul.append(new_row)
        return Matrix(matrix_mul)


    def __str__(self):
        new_str = '[ {} ]'.format(' '.join(map(str, self.mat[0])))
        for i in range (1, len(self.mat) -1):
            new_str = '{} \n| {} |'.format(new_str, ' '.join(map(str, self.mat[i])))
        new_str = '{} \n[ {} ]'.format(new_str, ' '.join(map(str, self.mat[len(self.mat) -1])))
        return new_str


    def is_square(self):
        return all(1 if self.length == len(self.mat[el]) else 0 for el in range(self.length))


    def check_dimention(self,other_matrix):
        return (self.length==other_matrix.length & self.rowl==other_matrix.rowl)


    def determinant(self):
        if not self.is_square():
            raise ValueError ('Cannot calculate for this matrix')
        if self.length == 1:
            return self.mat[0][0]
        elif self.length == 2:
            return (self.mat[0][0]*self.mat[1][1]-self.mat[0][1]*self.mat[1][0])
        else:
            det = 0
            for i in range(self.length):
                mat_copy = self.mat[1:]
                for j in range(len(mat_copy)):
                    mat_copy[j]=mat_copy[j][0:i] + mat_copy[j][i + 1:]
                fact = (-1) ** (i%2)
                a = Matrix(mat_copy)
                det_rec = a.determinant()
                det += fact * self.mat[0][i] * det_rec
        return det


    def inverse(self):
        if not self.is_square():
            raise ValueError ("Cannot calculate for this matrix")
        if self.length == 2:
            if (self.mat[0][0] * self.mat[1][1] == self.mat[0][1] * self.mat[1][0]):
                raise ValueError("ad = bc. This matrix does not have an inverse ad=bc")
            else:
                det = 1/(self.determinant())
                return([[det*self.mat[1][1],det*-self.mat[0][1]],[det*-self.mat[1][0],det*self.mat[0][0]]])
        elif (self.length == 1) :
            return (1/self.mat[0][0])
        else:
            inverse_mat = []
            for i in range(len(self.mat)):
                new_row = []
                for j in range(len(self.mat)):
                    minor = Matrix( [row[:j] + row[j+1:] for row in (self.mat[:i]+self.mat[i+1:])])
                    new_row.append(((-1)**(i+j)) * minor.determinant())
                inverse_mat.append(new_row)
            inverse_mat = list(map(list,zip(*inverse_mat)))
            for r in range(len(inverse_mat)):
                for c in range(len(inverse_mat)):
                    inverse_mat[r][c] = inverse_mat[r][c]/self.determinant()

            return inverse_mat

    def printg(self):
        print(self.mat)

    @staticmethod
    def get(row,col):
        return( [[random.random() for c in range(col)] for e in range(row)])

if __name__ == '__main__':
#    print(Matrix([[1,1] ,[2,3]]))
    a = Matrix([[4,7] ,[2,6]] ,None,None)
    a.printg()
    print(a.inverse())
#
#    c = Matrix([1,2])
#    print(c.inverse())
    print(a.is_square())
#    print(Matrix.printg(a))
#    b = Matrix([[6, 1, 1], [4, -2, 5], [2,8,7]])
#    print(b.inverse())
#    b.printg()
#    c = a.__add__(b)
#    c.printg()
#    print(a.check_dimention(b))
#    print(a.determinant())
#    print(b.determinant())
#    print(c.mat)
#    print(Matrix.__add__())
#    descr = repr(Matrix([[1,1] ,[2,7]]))
#    print ("dddd", descr)

    a_1 = Matrix.get(row =3, col=2)
    print(a_1)












