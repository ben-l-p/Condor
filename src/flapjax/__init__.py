import jax

# use 64-bit floats everywhere in the code by default
jax.config.update("jax_enable_x64", True)
