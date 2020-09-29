
import tensorflow as tf
sess = tf.Session()

# Print Example
hello = tf.constant('Hello, YEHS :)')
print(sess.run(hello).decode())

# Calculate Example
a = tf.constant(40)
b = tf.constant(25)
print(sess.run(a+b))
