class Add:
      def sum(self,a,b):
            self.c=a+b
            print("The Sum",self.c)
      def mul(self,a,b):
            self.c=a*b
            print("The Answer",self.c)
a=Add()
a.sum(12,13)
a.sum(11.66,15.77)
a.sum("Hello ","codders")
a.mul(5,6)
a.mul(5.5,7.8)
a.mul(8," Python ")