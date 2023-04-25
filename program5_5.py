def hello(name = 'world',age = 99):
    print('Hello!' + name)
    print(' 年齢は、{} 才ですね。'.format(age))
hello()
hello(age = 30)
hello(age = 30, name = 'kosei')
