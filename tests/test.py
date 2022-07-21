import bologna
import threading


class Object:
    pass


def test_di():
    my_object = Object()
    bologna.provide("object", my_object)

    @bologna.inject
    def inject_here(object=None, trans=0):
        print(object)

    @bologna.inject
    async def inject_here(object=None, trans=0):
        print(object)

    inject_here()
    thr = threading.Thread(target=inject_here)
    thr.start()
    thr.join()


def test_readme():
    from datetime import date

    my_injectable_string = "Hello, DI. Today is"
    my_injectable_object = date.today()

    bologna.provide("greeting", my_injectable_string)
    bologna.provide("thedate", my_injectable_object)

    @bologna.inject
    def print_date(greeting=None, thedate=None):
        print(f"{greeting}; {thedate}")

    print(print_date())
