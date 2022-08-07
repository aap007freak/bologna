## About function parameters

Python has five different parameter types, all of which can be injected into, but only is guaranteed to be runtime-safe: The keyword-only parameter type.

This section of the documentation focuses on function parameters, and common pitfalls one may fall into when trying to inject variables.


| PARAMETER TYPE        | INJECTABILITY         |
|-----------------------|-----------------------|
| POSITIONAL_ONLY       | Usable, with caveats  |
| POSITIONAL_OR_KEYWORD | Ussable, with caveats |
| VAR_POSITIONAL        | Usable, with caveats  |
| KEYWORD_ONLY          | **Fully** useable     |   
| VAR_KEYWORD           | Usable, with caveats  |

An example function which highlights the syntax of all five variable types:
````python
def my_function(pos_only_argument,
                / ,
                pos_key_argument,
                *varpos_arguments,
                keyword_only_argument,
                **varkey_arguments):
    pass

# example of how you'd call such a function
my_function("pos_only", 
            "pos_key_argument", 
            1, 2, 3, 
            keyword_only_argument=True, 
            extra_keyword_argument=1)
````

### Positional only parameters
You'd use this when the result of your function has depends on the order of the parameters, such as multiplying matrices.

