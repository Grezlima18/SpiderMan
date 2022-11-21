import cx_Freeze

executables = [cx_Freeze.Executable(
    script="SpiderMan.py",
    icon="assets/black_spider.ico"
)]
cx_Freeze.setup(
    name="SpiderMan",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)

