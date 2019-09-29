## Lab Exercise 9.19.2017 Demo Program 2
## Author: nmessa
## This program will print a table of decimal equivalents of fractions

#Generate all combinations of numerators and denominators
for num in range(1, 11):
    for den in range(1, 11):
        decimal = round(num / den, 4)

        #two alternative methods of printing result
        print(str(num) + '/' + str(den) + " = " + str(decimal))
        #print(num, '/', den, "=", decimal)

##Output
##1/1 = 1.0
##1/2 = 0.5
##1/3 = 0.3333
##1/4 = 0.25
##1/5 = 0.2
##1/6 = 0.1667
##1/7 = 0.1429
##1/8 = 0.125
##1/9 = 0.1111
##1/10 = 0.1
##2/1 = 2.0
##2/2 = 1.0
##2/3 = 0.6667
##2/4 = 0.5
##2/5 = 0.4
##2/6 = 0.3333
##2/7 = 0.2857
##2/8 = 0.25
##2/9 = 0.2222
##2/10 = 0.2
##3/1 = 3.0
##3/2 = 1.5
##3/3 = 1.0
##3/4 = 0.75
##3/5 = 0.6
##3/6 = 0.5
##3/7 = 0.4286
##3/8 = 0.375
##3/9 = 0.3333
##3/10 = 0.3
##4/1 = 4.0
##4/2 = 2.0
##4/3 = 1.3333
##4/4 = 1.0
##4/5 = 0.8
##4/6 = 0.6667
##4/7 = 0.5714
##4/8 = 0.5
##4/9 = 0.4444
##4/10 = 0.4
##5/1 = 5.0
##5/2 = 2.5
##5/3 = 1.6667
##5/4 = 1.25
##5/5 = 1.0
##5/6 = 0.8333
##5/7 = 0.7143
##5/8 = 0.625
##5/9 = 0.5556
##5/10 = 0.5
##6/1 = 6.0
##6/2 = 3.0
##6/3 = 2.0
##6/4 = 1.5
##6/5 = 1.2
##6/6 = 1.0
##6/7 = 0.8571
##6/8 = 0.75
##6/9 = 0.6667
##6/10 = 0.6
##7/1 = 7.0
##7/2 = 3.5
##7/3 = 2.3333
##7/4 = 1.75
##7/5 = 1.4
##7/6 = 1.1667
##7/7 = 1.0
##7/8 = 0.875
##7/9 = 0.7778
##7/10 = 0.7
##8/1 = 8.0
##8/2 = 4.0
##8/3 = 2.6667
##8/4 = 2.0
##8/5 = 1.6
##8/6 = 1.3333
##8/7 = 1.1429
##8/8 = 1.0
##8/9 = 0.8889
##8/10 = 0.8
##9/1 = 9.0
##9/2 = 4.5
##9/3 = 3.0
##9/4 = 2.25
##9/5 = 1.8
##9/6 = 1.5
##9/7 = 1.2857
##9/8 = 1.125
##9/9 = 1.0
##9/10 = 0.9
##10/1 = 10.0
##10/2 = 5.0
##10/3 = 3.3333
##10/4 = 2.5
##10/5 = 2.0
##10/6 = 1.6667
##10/7 = 1.4286
##10/8 = 1.25
##10/9 = 1.1111
##10/10 = 1.0