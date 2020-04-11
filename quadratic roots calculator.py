import matplotlib.pyplot as plt
import numpy as np
while True:
    try:
        print('-'*111) # for decoration purpose
        x = input('<< To continue press enter OR To kill the application press "0" >>   ')
        if x == '':
            print()
            print('<< THIS APPLICATION CALCULATES ROOTS FOR A GIVEN QUADRATIC EQUATION >>')
            print()
            print('>>> THE EQUATION WILL BE IN FORM OF << a.X^2 + b.X + c >>')
            print()
            a = int(input('enter value of a: '))
            b = int(input('enter value of b: '))
            c = int(input('enter value of c: '))
            d = ((b**2)-4*a*c)**(1/2)
            discriminant = ((b**2)-4*a*c)

            roots_1= ((-b)+d)/(2*a)
            roots_2 = ((-b)-d)/(2*a)
            root_declare = f'>>> The roots are  X = {roots_1}  and  X = {roots_2}.'
            print()
            print(f'>>> THE EQUATION IS ( {a}.X^2 + {b}.X + {c} ).')
            print()
            print(root_declare)
            print()
            print(f'>>> The value of discriminant is {discriminant}.')
            print()

            def root_indicator():                     # tell's root charateristic
                if discriminant > 0:
                    return('The roots of given equation are real.')
                elif discriminant < 0:
                    return('The roots of given equation are imaginary.')
                elif discriminant == 0:
                    return('There is one real root.')
            print(f'>>> {root_indicator()}')
            print()
            def plot_show():
                # 100 linearly spaced numbers
                x = np.linspace(-10**2,10**2,10**2)
                y = np.linspace(-10**2,10**2,10**2)

                # the function, which is y = x^2 here
                y = (a*(x**2))+(b*x)+c

                # setting the axes at the centre
                fig = plt.figure()
                ax = fig.add_subplot(1, 1, 1)
                ax.spines['left'].set_position('center')
                ax.spines['bottom'].set_position('zero')
                ax.spines['right'].set_color('none')
                ax.spines['top'].set_color('none')
                ax.xaxis.set_ticks_position('bottom')
                ax.yaxis.set_ticks_position('left')

                # plot the function
                plt.plot(x,y, 'r')

                # show the plot
                plt.show()
            plot_show()
        elif int(x) == 0:
            break
    except:
        if a == 0:
            print(f'>> a value must be larger than "zero" and enter numerals only.  <<')
        else:
            print()
            print(f'>> Please check the entered value, enter numerals only. <<')