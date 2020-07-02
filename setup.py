import cx_Freeze

executables = [ cx_Freeze.Executable(script="cobrita.py" ) ]

cx_Freeze.setup(
    name = "GOTY",
    options = {"build_exe": {"packages":["pygame"],
    }}, executables = executables
)