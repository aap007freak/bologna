import pytest

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


@pytest.fixture(autouse=True, scope="module")
def provide_some_variables():
    bologna.provide("a", "avalue")
    bologna.provide("b", "bvalue")
    bologna.provide("c", "cvalue")
    bologna.provide("d", ["d1", "d2", "d3"])
    bologna.provide("e", {"e1": "e1value", "e2": "e2value"})


def test_positional_only():
    @bologna.inject_new
    def f(x, b, /):
        return x, b

    assert f(1) == (1, "bvalue")


def test_positional_only_both_positions():
    @bologna.inject_new
    def f(a, b, /):
        return a, b

    assert f() == ("avalue", "bvalue")


def test_positional_only_not_enough_arguments():
    @bologna.inject_new
    def f(a, b, x, y):
        return a, b, x, y

    with pytest.raises(bologna.InjectionError):
        f(1)


def test_positional_or_keyword():
    @bologna.inject_new
    def f(a, x, b, y):
        return a, x, b, y

    assert f(1, 2) == ("avalue", 1, "bvalue", 2)
    assert f(y=1, x=2) == ("bvalue", 2, "avalue", 1)


def test_positional_or_keyword_not_enough_arguments():
    pass
