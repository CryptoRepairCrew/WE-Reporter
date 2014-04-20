def setup():
    '''
        This will import modules config_default and config and move their variables
        into current module (variables in config have higher priority than config_default).
        Thanks to this, you can import settings anywhere in the application and you'll get
        actual application settings.
        
        This config is related to server side. You don't need config.py if you
        want to use client part only.
    '''
    
    def read_values(cfg):
        for varname in cfg.__dict__.keys():
            if varname.startswith('__'):
                continue
            
            value = getattr(cfg, varname)
            yield (varname, value)

    try:
        import config
    except ImportError:
        # Custom config not presented, but we can still use defaults
        config = None
            
    import sys
    module = sys.modules[__name__]
    
    if config:
        for name,value in read_values(config):
            module.__dict__[name] = value

setup()
