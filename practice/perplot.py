import numpy as np
import perfplot

perfplot.show(
    setup=lambda n: np.random.rand(n),  # or setup=np.random.rand
    kernels=[
        lambda a: np.c_[a, a],
        lambda a: np.stack([a, a]).T,
        lambda a: np.vstack([a, a]).T,
        lambda a: np.column_stack([a, a]),
        lambda a: np.concatenate([a[:, None], a[:, None]], axis=1),
    ],
    labels=["c_", "stack", "vstack", "column_stack", "concat"],
    n_range=[2**k for k in range(25)],
    xlabel="len(a)",
    # More optional arguments with their default values:
    # logx="auto",  # set to True or False to force scaling
    # logy="auto",
    # equality_check=np.allclose,  # set to None to disable "correctness" assertion
    # show_progress=True,
    # target_time_per_measurement=1.0,
    # max_time=None,  # maximum time per measurement
    # time_unit="s",  # set to one of ("auto", "s", "ms", "us", or "ns") to force plot units
    # relative_to=1,  # plot the timings relative to one of the measurements
    # flops=lambda n: 3*n,  # FLOPS plots
)

