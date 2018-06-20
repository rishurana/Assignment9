''Ques 1 .Create a circle class and initialize it with radius.
 Make two methods getArea and getCircumference inside this class.'''
class Circle:
    radius=10
    def getArea(self):
        c = 3.14 * self.radius * self.radius
        print("Area of Circle is: ",c)
    def getCircumference(self):
        c = self.radius * 2 * 3.14
        print("Circumference of circle is :",c)
c1=Circle()
c1.getArea()
c1.getCircumference()
'''Ques 2. Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.'''
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def show(self):
        print(self.name,self.roll)
s1=Student("Bikram",6316506)
s1.show()
'''Ques 3. Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''
class temperature:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit
    def convertfahrenheit(self):
        fahrenheit = (celsius * 1.8) + 32
        print(fahrenheit)
    def convertcelcius(self):
        celsius = (fahrenheit - 32) / 1.8
        print(celsius)
celsius = int(input("enter temp in celcius: "))
fahrenheit = int(input("enter temp in fahrenheit: "))
s1 = temperature(celsius, fahrenheit)
s1.convertfahrenheit()
s1.convertcelcius()
'''Ques 4. Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
Make methods to
1. Display-Display the details.
2. Update- Update the movie details.'''
class MovieDetails:
    def __init__(self, moviename, artistname, year_of_release, ratings):
        self.moviename = moviename
        self.artistname = artistname
        self.year_of_release = year_of_release
        self.ratings = ratings
    print("")
    def display(self):
        print("Movie: ", self.moviename)
        print("artist name: ", self.artistname)
        print("release year:", self.year_of_release)
        print("ratings out of 5: ", self.ratings)
    print("")
    def update(self):
        self.moviename = input("enter the new updated movie:")
        self.artistname = input("enter the artist name:")
        self.year_of_release = (input("enter its release year:"))
        self.ratings = (input("enter the rating out of 5:"))
    print("")
moviename = input(" Movie: ")
artistname = input("Artist name")
year_of_release = input("Release year:")
ratings = input("Rating out of 5:")
s1 = MovieDetails(moviename, artistname, year_of_release, ratings)
s1.display()
s1.update()
s1.display()
'''Ques 5. Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
1. Display expenditure and savings
2. Calculate total salary
3. Display salary'''
class Expenditure:
	def __init__(self,expenditure,savings):
		self.expenditure=expenditure
		self.savings=savings
	def display(self):
		print("Enter Expenditure:",self.expenditure)
		print("Enter Savings: ",self.savings)
	def totalsalary(self):
		salary=self.expenditure+self.savings
		print("Total Salary  =",salary)
expenditure=int(input("Enter  Expenditure:"))
savings=int(input("Enter Savings:"))
s1=Expenditure(expenditure,savings)
s1.display()
s1.totalsalary()