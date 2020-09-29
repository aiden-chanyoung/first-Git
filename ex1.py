
import tensorflow as tf
hello = tf.constant('Hello, YEHS :)')
sess = tf.Session()
print(sess.run(hello).decode())
