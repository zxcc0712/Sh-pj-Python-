# import  sys ,pprint
#
# pprint.pprint(sys.path)
#
import  copy

print([n for n in dir(copy) if not n.startswith('_')])