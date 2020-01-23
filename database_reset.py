from mod import *


def main():
    try:
        for i in range(5, 0, -1):
            print('Deleting in {0}'.format(str(i))+' sec')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
