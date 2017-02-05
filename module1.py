# def _private_1(name):
#     return "Hello %s" %name
#
# def _private_2(name):
#     return 'Hi %s' %name
#
# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)
#
# print(greeting("dis"))

def main():
    print("we are in %s"%__name__)

if __name__ == "__main__":
    main()

