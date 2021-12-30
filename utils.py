
def get_class(func_info):
    class_name = func_info['class']
    module_name = func_info['module_path']
    #kwargs = func_info['kwargs']
    kwargs = func_info.get("kwargs", {})

    module = __import__(module_name, fromlist=True)
    func = getattr(module, class_name)
    return func(**kwargs)


