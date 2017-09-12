#--coding: utf-8--

# close —— 关闭文件
# read —— 读取文件内容
# readline —— 读取文本文件中的一行
# truncate —— 清空文件
# write(stuff) —— 将stuff写入文件

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncate the file. Goodbye!"

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()