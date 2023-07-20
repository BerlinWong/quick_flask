def demo(*args, **kwargs):
    for k, v in kwargs.items():
        print("Testing: %s=%s " % (k, v))


demo(name='alex')
