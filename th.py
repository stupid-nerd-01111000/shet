from threading import Thread


def say_dorood(halat):
    if halat == 'didar':
        print('hello')
    if halat == 'jodaii':
        print('goodby')

th1 = Thread(target=say_dorood, args=('didar',))
th2 = Thread(target=say_dorood, args=('jodaii',))



th1.start()
th2.start()
