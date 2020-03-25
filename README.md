[![HitCount](http://hits.dwyl.io/oke-aditya/Neurex.svg)](http://hits.dwyl.io/oke-aditya/Neurex)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/oke-aditya/Neurex/master)

# Neurex

# How it works

- Uses fast auto-encoders that can encrypt the text.
- We create multiple hashmaps of varying bit length using HashMapGenerator.py.
- Hashmap creation is random. Could be tied to some markov chain as well.
- We learn that hashmap through our autoencoders.
- These autoencoders work simultaneously to provide an encryption. (encrpyter_multiple_loading_running.py file)
- Note multiple autoencders can be generated from hashmaps with different bit length settings. All can be combined.
- Takes < 2mins to create a new network.
- Little slower than normal encryption algos.

### Version Supports
- Network V1.01 works for 6 bits for lowercase
- Network V1.11 works for for 8 bits lowercase
- Network V1.2.0 works for 8 bists all characters
- Network V1.2.1 works for 32 bits all characters
- Network V1.2.3 works for 56 bits all characters


## Major Update

- Parallel multiple neural network encryption algorithm aded.
- Not chained to processors / GPU yet.




