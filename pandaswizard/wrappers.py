# -*- encoding: utf-8 -*-

"""
A List of Useful Decorators/Wrappers for `pandas` Modules

The decorators can be used for profiling/understanding the a function
which are developed to handle a `DataFrame` object.
"""

import functools
import pandas as pd

def recordCounter(func : callable) -> callable:
    """
    Verbose the Shape of the DataFrame Pre- & Post- Function Execution

    On execution of a function (typically, if the function uses the
    `.drop()` or `.merge()` or etc.) the decorator prints the number
    of records before and after the execution of the function.

    ```python
    import pandaswizard as pdw # attempt to create an ubiquitous naming

    frame = pd.DataFrame(data = {
        "LABEL" : ["A", "A", "B"],
        "VALUES" : [1, 2, 3]
    })

    @pdw.wrappers.recordCounter
    def dropvals(frame):
        return frame[frame["LABEL"] != "B"]

    filtered = dropvals(frame = frame.copy())
    >> Executed with @recordCounter[`dropvals`]
    >>   >> Original Record Count = 3
    >>   >> Final Record Count    = 2
    >>   >> Dropped/Added Records = -1 (= 33.333%)
    ```

    LIMITATION: The decorator works IFF the dataframe is either the
    first arguments or is passed as an keyword argument with the
    argument name as either `data` or `frame` which is the general
    convention that is followed throughout my code. If the code has
    arguments, then it has preference over the keyword arguments and
    the `dataframe` must be the first argument.
    """

    @functools.wraps(func)
    def _wrapper(*args, **kwargs) -> pd.DataFrame:
        print(f"Executed with @recordCounter[`{func.__name__}`]")

        errors = False # lets initialize the decorator w/o error
        try:
            __frame = args[0] if args else \
                kwargs.get("data", None) or kwargs["frame"]
        except KeyError:
            errors = True
            print("  >> Failed to Execute. Check Decorator Limitation.")

        if not errors and not isinstance(__frame, pd.DataFrame):
            errors = True
            print("  >> Failed to Execute. DF Object is Not Found.")

        start_record_count_ = __frame.shape[0] if not errors else 0
        retval = func(*args, **kwargs)

        try:
            final_record_count_ = retval.shape[0]
        except Exception as err:
            final_record_count_ = 0
            print(f"  >> Function does not Return a DF. ERROR: {err}")

        print(f"  >> Original Record Count = {start_record_count_:,}")
        print(f"  >> Final Record Count    = {final_record_count_:,}")

        n_change = final_record_count_ - start_record_count_
        p_change = (abs(n_change) / start_record_count_) * 100 if not errors else 0
        print(f"  >> Dropped/Added Records = {n_change:,} (= {p_change:.3f}%)")
        return retval

    return _wrapper
