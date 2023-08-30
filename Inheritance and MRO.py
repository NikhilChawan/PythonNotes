'''class student:
    def student_info(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    def show(self):
        print('name::',self.name)
        print('id::',self.id)
        print('age::',self.age)
class update_student(student):
    def update_student_info(self,insta_id):
        self.insta_id=insta_id
    def shows(self):
        print('insta_id::',self.insta_id)
obj=update_student()
obj.student_info('om',6,26)
obj.show()
obj.update_student_info(1666)
obj.shows()'''
'''#1 single level inharitance
class A:
    def m1(self):
        print("in m1")
class B(A):
    def m2(self):
        print("in m2")
obj=B()
obj.m1();obj.m2()'''
'''#2 multi level inharitance
class A:
    def m1(self):
        print("in m1")
class B(A):
    def m2(self):
        print("in m2")
class C(B):
    def m3(self):
        print("in m3")
obj=C()
obj.m1();obj.m2();obj.m3()'''
'''#3 multiple inharitance
class A:
    def m1(self):
        print("in m1")
class B:
    def m2(self):
        print("in m2")
class C(A,B):
    def m3(self):
        print("in m3")
obj=C()
obj.m1();obj.m2();obj.m3()'''
'''#4-hybrid inharitance-combination of multi level inharitance and multiple inharotance
class A:
    def m1(self):
        print("in m1")
class B(A):
    def m2(self):
        print("in m2")
class C(B):
    def m3(self):
        print("in m3")
class D:
    def m4(self):
        print("in m4")
class E(B,D):
    def m5(self):
        print("in m5")
obj=E()
obj.m1();obj.m2();obj.m4();obj.m5()'''
'''#5-Hrichical inheritance
class A:
    def m1(self):
        print("in m1")
class B(A):
    def m2(self):
        print("in m2")
class C(A):
    def m3(self):
        print("in m3")
class D(B,A):
    def m4(self):
        print("in m4")
class E(B,A):
    def m5(self):
        print("in m5")
class F(C,A):
    def m6(self):
        print("in m6")
class G(C,A):
    def m7(self):
        print("in m7")
obj=G()
obj.m1();obj.m3();obj.m7()
obj2=D()
obj2.m1();obj2.m2();obj2.m4()'''
'''#how to call local veriable
class A:
    def m1(self):
        print("in m1")
    k=600
class B(A):
    def m2(self):
        print("in m2")
        print(A.k)
obj=B()
obj.m1();obj.m2()
#HomeWork Example Solution'''
class A:
    def m1(self):
        print("in m1")
class B(A):
    def m2(self):
        print("in m2")
class Z:
    def m3(self):
        print("in m3")
class Y:
    def m4(self):
        print("in m4")
class X:
    def m5(self):
        print("in m5")
class C(X,Z,Y,B,A):
    def m6(self):
        print("in m6")
class P(C,X,Z,Y,B,A):
    def m7(self):
        print("in m7")
class Q(C,X,Z,Y,B,A):
    def m8(self):
        print("in m8")
class E(B,A):
    def m9(self):
        print("in m9")
class G(E,B,A):
    def m10(self):
        print("in m10")
class F(E,B,A):
    def m11(self):
        print("in m11")
obj=C()
obj.m1();obj.m2();obj.m3();obj.m4();obj.m5();obj.m6()



