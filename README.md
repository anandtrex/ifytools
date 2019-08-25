# ifytools
Functional utils (for ML)

## INSTALL

`pip install https://github.com/anandtrex/ifytools/archive/master.zip`

## Use with tensorflow (graph mode)

```python
import numpy as np
import tensorflow as tf

from ifytools import multiprocify, generatorify, fify

def gen_sth(random_gen, mi, mx, ss):
    nn1 = random_gen.uniform(mi, mx, ss).astype(np.float32)
    nn2 = random_gen.uniform(mi, mx, ss).astype(np.float32)

    return dict(number1=nn1, number2=nn2)


ss = (1,)
seed = 1234
batch_size = 4
f_gen_sth = fify(gen_sth, mi=1, mx=10, ss=ss)

gen_fn = multiprocify(f_gen_sth, seed=seed)
tf_dataset = tf.data.Dataset.from_generator(
    gen_fn,
    {'number1': tf.float32, 'number2': tf.float32},
    {'number1': ss, 'number2': ss},
) \
    .batch(batch_size)
iterator = tf_dataset.make_one_shot_iterator()
values = iterator.get_next()
number1, number2 = values['number1'], values['number2']

n1 = tf.placeholder_with_default(number1, (batch_size, *ss), name='n1')
n2 = tf.placeholder_with_default(number2, (batch_size, *ss), name='n2')

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(10):
        summ = sess.run(tf.reduce_sum(n1 + n2))
        print(summ)
```
