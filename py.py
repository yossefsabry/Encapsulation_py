#-----------------------------------------------
# object oriented programming => Encapsulation
#-----------------------------------------------


#   public attributes = variables = properties


class member:

    def __init__(self,name):

        self.name = name

one = member("ahmed")

print(one.name)

#########################################

# #              protected
# you cant use the attributes inside or outside the class there no thing deffirent
#  its better use in typing for specifc the type of attributes
class member:

    def __init__(self,name):

        self._name = name

one = member("ahmed")

print(one._name)

one._name = "yossef"

print(one._name)

#########################################

#              private

# you cant use the attributes outside the class you can only use in the class
# but its not work very well for this its only use in typing for specifc the type of attributes 


class member:

    def __init__(self,name):

        self.__name = name

    def name_1(self):

        print(f"hello {self.__name}")

one = member("ahmed")

print(one.name_1())


print(one._member__name)

