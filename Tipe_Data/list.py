x = [1, 'Dicoding', True, 1.0]

print(type(x))  # <class 'list'>

print(x[3])  # 1.0


# Mengubah nilai elemen list
x = [1, 2.2, 'Dicoding']

x[0] = 'Indonesia'

print(x) # ['Indonesia', 2.2, 'Dicoding']


# Berbagai cara indexing pada list
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0]) # laptop
print(x[2]) # mouse
print(x[-1]) # microphone
print(x[-3]) # webcam


# Slcing pada list
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2]) # ['laptop', 'mouse', 'keyboard']
print(x[1:]) # ['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
print(x[:3]) # ['laptop', 'monitor', 'mouse']