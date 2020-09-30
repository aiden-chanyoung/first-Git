
import tensorflow as tf
sess = tf.Session()

YEHS = tf.constant('YEHS')
print(sess.run(YEHS).decode())

# Add your name and print it :)
CYPARK = tf.constant('Chan Young Park')
print(sess.run(CYPARK).decode())
AIDEN = tf.constant('Aiden')
print(sess.run(AIDEN).decode())
