# -*- encoding: utf-8 -*-

"""
A List of Useful Decorators/Wrappers for `pandas` Modules

The decorators can be used for profiling/understanding the a function
which are developed to handle a `DataFrame` object.
"""

import time
import functools
import collections
import pandas as pd

def recordCounter(func : callable) -> callable:
    """
    Verbose the Shape of the DataFrame Pre- & Post- Function Execution

    On execution of a function (typically, if the function uses the
    :attr:`.drop()` or :attr:`.merge()` or etc.) the decorator prints
    the number of records before and after the execution.

    .. code-block:: python

        import pandas as pd
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

    LIMITATION: The decorator works IFF the dataframe is either the
    first arguments or is passed as an keyword argument with the
    argument name as either `data` or `frame` which is the general
    convention that is followed throughout the module. If the code has
    arguments, then it has preference over the keyword arguments and
    the `dataframe` must be the first argument.

    USE Cases: Often on function execution, joining/dropping records
    users need to execute `df.shape` before and after to check the
    record count. This is simplified and gives the result, and thus
    reducing code during such operations.
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
        retval = func(*args, **kwargs) # ? execute the func as is

        # ! retval:: can either be a dataframe, or iterable where
        # the first returned value is always a dataframe, then we can
        __retframe = retval[0] if isinstance(retval, (list, tuple)) \
            else retval if isinstance(retval, pd.DataFrame) else None

        try:
            final_record_count_ = __retframe.shape[0]
        except Exception as err:
            errors, final_record_count_ = True, 0
            print(f"  >> Function does not Return a DF. ERROR: {err}")

        if not errors:
            print(f"  >> Original Record Count = {start_record_count_:,}")
            print(f"  >> Final Record Count    = {final_record_count_:,}")

            n_change = final_record_count_ - start_record_count_
            p_change = (abs(n_change) / start_record_count_) * 100 if not errors else 0
            print(f"  >> Dropped/Added Records = {n_change:,} (= {p_change:.3f}%)")

        return retval

    return _wrapper


def timeit(func : callable) -> callable:
    """
    A Mimic of the iPython Magic :attr:`%timeit` for Dataframes

    The built-in iPython magic function :attr:`%timeit` displays the
    executed time of a function, or like the one from command line:

    .. code-block:: shell

        python -m timeit "function()"

    The function is built specifically to handle functions which
    returns a :attr:`pd.DataFrame` object, thus it prints more
    information like the number of records fetched, shape and other
    information w/o explictly needing to call additional pandas
    function by the end-user.
    """

    @functools.wraps(func)
    def _wrapper(*args, **kwargs) -> pd.DataFrame:
        print(f"Executed with @timeit[`{func.__name__}`]")

        start = time.process_time() # capture start time
        frame = func(*args, **kwargs) # execute function

        # verbose information(s) to the output
        process_time = time.process_time() - start
        dtypes_count = collections.Counter(frame.dtypes.values)
        print(f"  >> Function Executed in {process_time:,.3f} secs.")
        print(f"  >> Fetched {frame.shape[0]:,} Record(s).")
        print(f"  >> No. of Feature(s)/Column(s) = {frame.shape[1]:,}.")
        print(f"  >> Observed Data Type(s) : {dtypes_count}")

        return frame
    return _wrapper
