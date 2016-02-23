import demo
from demo import sub1, sub2

assert demo.hello() == "root"
assert sub1.hello() == "sub1"
assert sub2.hello() == "sub2"

print("test ok !")
