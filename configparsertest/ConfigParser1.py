import configparser

config = configparser.ConfigParser()

config.read('n1.cfg')

secs = config.sections()

print(secs)


options2 = config.options('abc2')

print('---------------------')
print(options2)

# sec = config.remove_section('abc1')
# config.write(open('n1.cfg','w'))

sec = config.add_section('abc1')
sec = config.add
config.write(open('n1.cfg','w'))